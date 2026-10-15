// Sample web code for the submission_check.py fixture. Not a real app.
export function findNearbyClubs(): void {
  navigator.geolocation.getCurrentPosition((pos) => console.log(pos.coords.latitude));
}
