from ai_brain import AIBrain
from youtube_uploader import YouTubeUploader
from video_generator import VideoGenerator

jarvis = AIBrain()
youtube = YouTubeUploader()
video_gen = VideoGenerator()

print("🤖 Jarvis Auto Mode चालू है (Full Video + Shorts Auto Upload)")

while True:
    topic = input("\n🎬 Enter video topic (or type 'exit'): ")
    if topic.lower() in ["exit", "quit"]:
        print("Jarvis बंद हो रहा है...")
        break

    # Auto Generate Video + Shorts
    video_file, shorts_file = video_gen.generate_video(topic)

    # SEO Auto Title + Description
    title = f"{topic} - Explained in 60 seconds!"
    description = f"This is an auto-generated video about {topic}. Created by Jarvis AI."
    tags = [topic, "AI Generated", "Shorts", "Tech"]

    # Upload Full Video
    youtube.upload_video(video_file, title=title, description=description, tags=tags)

    # Upload Shorts
    shorts_title = f"{topic} #Shorts"
    youtube.upload_video(shorts_file, title=shorts_title, description=description, tags=tags)

    print(f"✅ Both Full Video & Shorts uploaded for: {topic}")
