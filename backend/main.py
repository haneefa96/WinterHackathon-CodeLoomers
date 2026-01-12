
# from fastapi import FastAPI, Form
# from fastapi.middleware.cors import CORSMiddleware  # Fixed import
# import os
# from google.cloud import firestore
# import google.auth

# # Service account (auto-detects serviceAccountKey.json)
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "serviceAccountKey.json"

# app = FastAPI(title="CodeLoomers Backend")

# # CORS Fixed - proper parameters
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Fixed: list format
#     allow_credentials=True,
#     allow_methods=["*"],  # Fixed: list format
#     allow_headers=["*"],  # Fixed: list format
# )

# # Initialize GCP (with fallback)
# model = None
# db = None

# try:
#     # Firestore only (simpler, works 100%)
#     db = firestore.Client()
#     print("✅ Firestore Connected!")
    
#     # Test Firestore
#     db.collection("test").document("ping").set({"status": "ok"})
#     print("✅ Firestore Test OK!")
    
# except Exception as e:
#     print(f"⚠️ Firestore Error: {e}")

# @app.get("/")
# def root():
#     return {"status": "CodeLoomers Backend - Firestore Ready"}

# @app.post("/artisan/generate")
# async def generate(story: str = Form(...)):
#     title = f"Handwoven Artisan Craft: {story[:50]}"  # Mock Gemini for stability
    
#     if db:
#         # REAL FIRESTORE SAVE
#         profile = {
#             "story": story, 
#             "title_en": title,
#             "created": firestore.SERVER_TIMESTAMP
#         }
#         db.collection("artisans").add(profile)
#         print(f"✅ Saved artisan to Firestore: {title}")
    
#     return {
#         "title_en": title,
#         "title_hi": "हाथ से बुना शिल्प",
#         "caption_en": "Crafted with tradition by local artisans", 
#         "story": story
#     }

# @app.get("/buyer/search")
# async def search(q: str):
#     if db:
#         # REAL FIRESTORE SEARCH
#         artisans = db.collection("artisans").limit(5).stream()
#         results = []
#         for artisan in artisans:
#             data = artisan.to_dict()
#             if q.lower() in data.get("story", "").lower():
#                 results.append({
#                     "title_en": data.get("title_en", "Artisan Craft"),
#                     "story": data.get("story", "")
#                 })
#     else:
#         results = []
    
#     return {"results": resfrom app.vision import generate_story_from_vision
from app.gemini import generate_artisan_content
from app.vision import generate_story_from_vision
from app.gemini import generate_ai_content


from fastapi import FastAPI, Form
from typing import Dict
from google.cloud import firestore
from app.config import db
from fastapi import UploadFile, File
from app.speech import transcribe

app = FastAPI(
    title="CodeLoomers Backend",
    version="0.1.0"
)

@app.get("/", response_model=Dict[str, str])
def root():
    return {"status": "Backend running"}

@app.post("/artisan/generate", response_model=Dict[str, str])
def generate_artisan(story: str = Form(...)):
    title = f"Handwoven Craft: {story[:40]}"

    db.collection("artisans").add({
        "story": story,
        "title_en": title,
        "created": firestore.SERVER_TIMESTAMP
    })

    return {
        "title_en": title,
        "caption_en": "Crafted with tradition by local artisans",
        "story": story
    }
@app.post("/artisan/voice")
async def upload_voice(audio: UploadFile = File(...)):
    """
    Receives an audio file and returns transcribed text
    """

    audio_bytes = await audio.read()

    text = transcribe(audio_bytes)

    return {
        "transcription": text
    }
# from fastapi import UploadFile, File
# from app.vision import analyze_image

# @app.post("/artisan/image")
# async def upload_image(image: UploadFile = File(...)):
#     image_bytes = await image.read()

#     result = analyze_image(image_bytes)

#     return {
#         "labels": result["labels"],
#         "objects": result["objects"],
#         "description": result["description"]
#     }
from fastapi import UploadFile, File
from app.vision import analyze_image
print(">>> IMAGE ROUTE LOADED <<<")

# @app.post("/artisan/image")
# async def upload_image(image: UploadFile = File(...)):
#     image_bytes = await image.read()
#     result = analyze_image(image_bytes)
#     return result
# from app.gemini import generate_craft_twin

# @app.post("/artisan/image")
# async def analyze_artisan_image(image: UploadFile = File(...)):
#     vision_result = analyze_image(image)

#     labels = vision_result["labels"]
#     objects = vision_result["objects"]

#     # NEW: Generate story
#     story = generate_story_from_image(labels, objects)

#     # Reuse your existing generator logic
#     generated = generate_artisan_content(story)

#     return {
#         "labels": labels,
#         "objects": objects,
#         "story": story,
#         "title_en": generated["title_en"],
#         "caption_en": generated["caption_en"]
#     }


from fastapi import UploadFile, File

@app.post("/artisan/image")
def analyze_artisan_image(image: UploadFile = File(...)):
    try:
        image_bytes = image.file.read()
        vision_data = generate_story_from_vision(image_bytes)
        return vision_data
    except Exception as e:
        print("Image error:", e)
        return {"error": str(e)}

# @app.post("/artisan/generate-ai")
# def generate_ai_content(
#     story: str = Form(...),
#     labels: str = Form(...)
# ):
#     labels_list = [l.strip() for l in labels.split(",")]

#     result = generate_craft_twin(story, labels_list)
#     return result
# from app.artisan_story import generate_story_from_image

from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from google.cloud import firestore
from app.config import db

app = FastAPI()

# @app.post("/artisan/generate")
# def generate_artisan(story: str = Form(...)):
#     try:
#         title = f"Handwoven Craft: {story[:40]}"

#         db.collection("artisans").add({
#             "story": story,
#             "title_en": title,
#             "created": firestore.SERVER_TIMESTAMP
#         })

#         return {
#             "title_en": title,
#             "caption_en": "Crafted with tradition by local artisans",
#             "story": story
#         }

#     except Exception as e:
#         print("ERROR in /artisan/generate:", e)
#         return {"error": str(e)}

@app.post("/artisan/generate-ai")
def generate_ai(
    story: str = Form(...),
    labels: str = Form(...)
):
    try:
        content = generate_ai_content(story, labels)
        return content
    except Exception as e:
        print("AI ERROR:", e)
        return {"error": str(e)}

