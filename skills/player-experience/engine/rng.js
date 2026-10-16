// Seeded randomness for the player experience engine (pxe 0.1).
//
// Everything here is unsigned 32 bit integer arithmetic, so a port to Swift,
// Kotlin, C# or Python reproduces the same sequence bit for bit. Floats appear
// only in next(), as uint32 / 2^32, which is exact in IEEE 754 doubles. Game
// logic that must match across platforms should use int(n) or nextUint32().
//
// No Math.random, no Date.now: the same seed gives the same sequence everywhere.

const TWO_POW_32 = 4294967296;
const FNV_OFFSET_BASIS = 0x811c9dc5;
const FNV_PRIME = 0x01000193;
const MULBERRY_INCREMENT = 0x6d2b79f5;

const utf8 = new TextEncoder();

/**
 * FNV-1a 32 bit hash of the UTF-8 bytes of a string.
 * h = 2166136261; for each byte b: h = (h XOR b) * 16777619 mod 2^32.
 * @param {string} str
 * @returns {number} unsigned 32 bit integer
 */
export function fnv1a32(str) {
  if (typeof str !== 'string') throw new TypeError('fnv1a32 expects a string');
  let h = FNV_OFFSET_BASIS;
  for (const byte of utf8.encode(str)) {
    h ^= byte;
    h = Math.imul(h, FNV_PRIME); // low 32 bits of the product, as in C
  }
  return h >>> 0;
}

/**
 * Turns any string (a level id, a day id, an install id) into a uint32 seed.
 * Identical to fnv1a32; the separate name says what the value is for.
 * @param {string} str
 * @returns {number}
 */
export function seedFromString(str) {
  return fnv1a32(str);
}

/**
 * One mulberry32 step. Returns the next internal state and the output word.
 * The state is kept to 32 bits on every step; the popular snippet lets it grow
 * as a double and drifts after about 4.9 million draws.
 * @param {number} state uint32
 * @returns {[number, number]} [nextState, outputUint32]
 */
export function mulberry32Step(state) {
  const next = (state + MULBERRY_INCREMENT) >>> 0;
  let t = Math.imul(next ^ (next >>> 15), next | 1);
  t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
  return [next, (t ^ (t >>> 14)) >>> 0];
}

/**
 * @typedef {object} Rng
 * @property {number} seed the uint32 seed the generator started from
 * @property {() => number} nextUint32 next raw output, an integer in [0, 2^32)
 * @property {() => number} next next float in [0, 1)
 * @property {(n: number) => number} int next integer in [0, n), unbiased
 */

/**
 * Creates a mulberry32 generator.
 * @param {number | string} seed an integer in [0, 2^32), or a string hashed with seedFromString
 * @returns {Rng}
 */
export function createRng(seed) {
  const start = typeof seed === 'string' ? seedFromString(seed) : seed;
  if (!Number.isInteger(start) || start < 0 || start >= TWO_POW_32) {
    throw new RangeError('seed must be a string or an integer in [0, 2^32)');
  }
  let state = start;

  const nextUint32 = () => {
    const [nextState, out] = mulberry32Step(state);
    state = nextState;
    return out;
  };

  return {
    seed: start,
    nextUint32,
    next: () => nextUint32() / TWO_POW_32,
    // Rejection sampling: draw u until u < limit (the largest multiple of n
    // that fits in 2^32), then return u mod n. No modulo bias, integers only.
    int(n) {
      if (!Number.isInteger(n) || n < 1 || n > TWO_POW_32) {
        throw new RangeError('int(n) needs an integer n in [1, 2^32]');
      }
      const limit = TWO_POW_32 - (TWO_POW_32 % n);
      let u = nextUint32();
      while (u >= limit) u = nextUint32();
      return u % n;
    },
  };
}

/**
 * @template T
 * @typedef {object} Bag
 * @property {() => T} next deals the next item, reshuffling when the bag is empty
 * @property {() => number} remaining items left in the current bag
 * @property {number} size items per bag
 */

/**
 * Bag randomizer: shuffles a copy of the items, deals each one once, then
 * reshuffles. An item never waits more than 2n minus 2 draws between two
 * appearances, which caps droughts. The shuffle happens lazily, when next()
 * finds the bag empty, so the rng is consumed at the same points on every port.
 * Shuffle: Fisher Yates (Durstenfeld), for i from n minus 1 down to 1,
 * j = rng.int(i + 1), swap items i and j.
 * @template T
 * @param {readonly T[]} items one entry per slot; repeat an item to weight it
 * @param {Rng} rng
 * @returns {Bag<T>}
 */
export function createBag(items, rng) {
  if (!Array.isArray(items) || items.length === 0) {
    throw new TypeError('createBag needs a non empty array of items');
  }
  if (!rng || typeof rng.int !== 'function') throw new TypeError('createBag needs an rng from createRng');
  const source = items.slice();
  /** @type {T[]} */
  let bag = [];
  let index = 0;

  const refill = () => {
    bag = source.slice();
    for (let i = bag.length - 1; i > 0; i -= 1) {
      const j = rng.int(i + 1);
      const tmp = bag[i];
      bag[i] = bag[j];
      bag[j] = tmp;
    }
    index = 0;
  };

  return {
    size: source.length,
    remaining: () => bag.length - index,
    next() {
      if (index >= bag.length) refill();
      const item = bag[index];
      index += 1;
      return item;
    },
  };
}
