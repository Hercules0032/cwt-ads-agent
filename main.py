import os
import json
import shutil
import subprocess

def run_production_pipeline(story_id, hook, pain, cta, image_name="bg.png", audio_name="voice.mp3"):
   
    root_dir = os.path.dirname(os.path.abspath(__file__))
    remotion_dir = os.path.join(root_dir, "cwt-remotion")
    content_dir = os.path.join(remotion_dir, "public", "content", story_id)
    img_dir = os.path.join(content_dir, "images")
    aud_dir = os.path.join(content_dir, "audio")
    
  
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(aud_dir, exist_ok=True)
    
 
    try:
        src_image = os.path.join(root_dir, image_name)
        src_audio = os.path.join(root_dir, audio_name)

        if os.path.exists(src_image):
            shutil.copy(src_image, os.path.join(img_dir, image_name))
            print(f"✅ Image deployed: {img_dir}/{image_name}")
        else:
            print(f"❌ CRITICAL: Missing {src_image}")

        if os.path.exists(src_audio):
            shutil.copy(src_audio, os.path.join(aud_dir, audio_name))
            print(f"✅ Audio deployed: {aud_dir}/{audio_name}")
        else:
            print(f"❌ CRITICAL: Missing {src_audio}")
    except Exception as e:
        print(f"⚠️ Asset Error: {e}")


    timeline = {
        "shortTitle": "CWT TRADING",
        "lengthFrames": 360,
        "elements": [{"startMs": 0, "endMs": 12000, "image": image_name}],
        "text": [
            {"text": hook, "startMs": 0, "endMs": 4000},
            {"text": pain, "startMs": 4000, "endMs": 8000},
            {"text": cta, "startMs": 8000, "endMs": 12000}
        ],
        "audio": [{"audioUrl": audio_name, "startMs": 0, "endMs": 12000}]
    }
    
    with open(os.path.join(content_dir, "timeline.json"), "w") as f:
        json.dump(timeline, f, indent=2)
    
    print(f"✅ JSON written for {story_id}")
    
   
    print("🚀 Starting Render...")
    subprocess.run([
        "npx", "remotion", "render", "src/index.ts", 
        story_id, f"../output/{story_id}.mp4", 
        "--force", "--bundle-cache=false"
    ], cwd=remotion_dir)

if __name__ == "__main__":
   
    run_production_pipeline(
        "cwt-automated-render",
        "Stop losing money.",
        "Trade with data.",
        "Join CWT now."
    )