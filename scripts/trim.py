
import subprocess
import os

INPUT_VIDEO = "videos/input.mp4"
OUTPUT_VIDEO = "videos/trimmed.mp4"

START_TIME = "00:00:05"   # يبدأ من الثانية 5
DURATION = "30"           # مدة 30 ثانية

def trim_video():
    if not os.path.exists(INPUT_VIDEO):
        print("❌ input.mp4 غير موجود")
        return

    command = [
        "ffmpeg",
        "-y",
        "-i", INPUT_VIDEO,
        "-ss", START_TIME,
        "-t", DURATION,
        "-c", "copy",
        OUTPUT_VIDEO
    ]

    subprocess.run(command)
    print("✅ تم قص الفيديو بنجاح")

if __name__ == "__main__":
    trim_video()
