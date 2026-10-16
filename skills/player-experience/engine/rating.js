// Elo style ratings for a player against a level (pxe 0.1).
//
// A level is treated as an opponent: winning the level is a win for the player
// and a loss for the level. Player and level ratings share one scale, so
// rating_gap = level_rating minus skill_rating reads directly as "how much
// harder than this player the level is".
//
//   expected(P, L) = 1 / (1 + 10 ^ ((L - P) / 400))   chance the player wins
//   S              = 1 for a win, 0 for a fail
//   P' = P + k      * (S - expected(P, L))
//   L' = L - levelK * (S - expected(P, L))
//
// levelK defaults to a quarter of k: a level's rating comes from thousands of
// attempts in the offline calibration table, so one player should barely move
// it. With k equal to levelK the sum of both ratings is conserved.

export const DEFAULT_RATING = 1500;
export const DEFAULT_K = 32;
export const DEFAULT_LEVEL_K = 8;
const SCALE = 400;

/** @param {unknown} x @returns {x is number} */
const isFiniteNumber = (x) => typeof x === 'number' && Number.isFinite(x);

/**
 * Probability that a player rated `player` wins a level rated `level`.
 * @param {number} player
 * @param {number} level
 * @returns {number} in (0, 1)
 */
export function expected(player, level) {
  if (!isFiniteNumber(player) || !isFiniteNumber(level)) {
    throw new TypeError('expected() needs two finite ratings');
  }
  return 1 / (1 + 10 ** ((level - player) / SCALE));
}

/**
 * New ratings for both sides after one finished attempt.
 * @param {number} player
 * @param {number} level
 * @param {boolean} won
 * @param {{ k?: number, levelK?: number }} [options]
 * @returns {{ player: number, level: number, expected: number }}
 */
export function update(player, level, won, options = {}) {
  if (typeof won !== 'boolean') throw new TypeError('update() needs won as a boolean');
  const k = options.k ?? DEFAULT_K;
  const levelK = options.levelK ?? DEFAULT_LEVEL_K;
  if (!isFiniteNumber(k) || k < 0 || !isFiniteNumber(levelK) || levelK < 0) {
    throw new RangeError('k and levelK must be finite and not negative');
  }
  const e = expected(player, level);
  const delta = (won ? 1 : 0) - e;
  return { player: player + k * delta, level: level - levelK * delta, expected: e };
}
