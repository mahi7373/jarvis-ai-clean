import schedule
import time
from pytrends.request import TrendReq
from video_generator import VideoGenerator
from youtube_uploader import YouTubeUploader

# Fetch Marvel trending topics from Google Trends
def fetch_marvel_trending():
    pytrends = TrendReq(hl='en-US', tz=330)
    pytrends.build_payload(kw_list=["Marvel"])
    trending_data = pytrends.related_queries()
    
    if "Marvel" in trending_data and trending_data["Marvel"]["top"] is not None:
        marvel_trends = trending_data["Marvel"]["top"]["query"].tolist()
        return marvel_trends[:5]  # Top 5 trending Marvel topics
    return ["Marvel latest news", "Marvel movies update"]

# Generate and upload Marvel video
def auto_generate_upload():
    topics = fetch_marvel_trending()
    if not topics:
        print("❌ No Marvel trending topics found.")
        return

    topic = topics[0]
    print(f"🎬 Today's Marvel Topic: {topic}")

    # Video + Shorts Generate
    video_gen = VideoGenerator()
    video_file, shorts_file = video_gen.generate_video(topic)

    # SEO Auto Title + Description
    title = f"{topic} - Marvel Explained in 60 seconds!"
    description = f"This is an auto-generated Marvel video about {topic}. Created by Jarvis AI."
    tags = [topic, "Marvel", "MCU", "Shorts"]

    # Upload Videos
    youtube = YouTubeUploader()
    youtube.upload_video(video_file, title=title, description=description, tags=tags)
    youtube.upload_video(shorts_file, title=f"{topic} #Shorts", description=description, tags=tags)

    print(f"✅ Auto Uploaded Marvel Video: {topic}")

# ----------------------------
# ✅ Test Mode (Immediate Run)
# ----------------------------
if __name__ == "__main__":
    print("🚀 Jarvis Marvel Test Mode Running...")
    auto_generate_upload()

    # ----------------------------
    # ✅ Schedule Multiple Daily Runs
    # ----------------------------
    schedule.every().day.at("10:00").do(auto_generate_upload)  # Morning
    schedule.every().day.at("15:00").do(auto_generate_upload)  # Afternoon
    schedule.every().day.at("20:00").do(auto_generate_upload)  # Evening

    print("🤖 Auto Scheduler Active (3 videos per day at 10 AM, 3 PM, 8 PM)...")

    while True:
        schedule.run_pending()
        time.sleep(60)
