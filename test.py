import os
from instagrapi import Client

# Instagram credentials
USERNAME = "wreck._.it._.ralph"
PASSWORD = "vapoursaintgood@2"
RECIPIENT_USERNAME = "maheen_lakhvera"
VIDEO_FOLDER = "D:/media"  # Folder where videos are stored
SENT_FILE = "sent.txt"  # File to track sent videos

# Login to Instagram
cl = Client()
cl.login(USERNAME, PASSWORD)

# Load already sent videos
if os.path.exists(SENT_FILE):
    with open(SENT_FILE, "r") as f:
        sent_videos = set(f.read().splitlines())
else:
    sent_videos = set()

# Get list of videos in the directory
videos = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith((".mp4", ".mov"))]
videos_to_send = [v for v in videos if v not in sent_videos]

for video in videos_to_send:
    video_path = os.path.join(VIDEO_FOLDER, video)
    try:
        cl.direct_send_video(video_path, [cl.user_id_from_username(RECIPIENT_USERNAME)])
        print(f"Sent: {video}")
        
        # Log the sent video
        with open(SENT_FILE, "a") as f:
            f.write(video + "\n")
    except Exception as e:
        print(f"Failed to send {video}: {e}")

print("Task Completed!")
