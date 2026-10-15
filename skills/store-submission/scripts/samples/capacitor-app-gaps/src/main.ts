// Sample web code with gaps for the submission_check.py fixture. Not a real app.
export async function startVideoRound(): Promise<void> {
  await navigator.mediaDevices.getUserMedia({ video: true, audio: false });
}
