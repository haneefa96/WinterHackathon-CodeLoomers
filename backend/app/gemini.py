import vertexai
from vertexai.generative_models import GenerativeModel, Part
import os

# Initialize Vertex AI
# You should ideally set these via environment variables or rely on default credentials if running in GCP
PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT", "codeloomers-484010") # Default fallback from file check
LOCATION = "us-central1"

try:
    vertexai.init(project=PROJECT_ID, location=LOCATION)
    # Using a model that supports both text and images if needed, though we deal with text description mostly here
    model = GenerativeModel("gemini-1.5-flash") 
    print("✅ Vertex AI Gemini Model Initialized")
except Exception as e:
    print(f"⚠️ Vertex AI Init Error: {e}")
    model = None

def generate_ai_content(story: str, labels: list = None):
    """
    Generates product title, description, and hashtags using Gemini.
    """
    if not model:
        return {
            "title_en": "Error: AI Model Not Loaded",
            "caption_en": "Please check backend configuration.",
            "title_hi": "",
            "caption_hi": ""
        }

    label_str = ", ".join(labels) if labels else "Handcrafted item"

    prompt = f"""
    You are an expert copywriter for Indian artisans selling handmade products.
    
    Artisan's Story/Input: "{story}"
    Detected Visual Tags: {label_str}

    Based on this, generate:
    1. An English Title (short, catchy).
    2. An English Instagram-style Caption (storytelling, engaging, use emojis).
    3. A Hindi Title (translated/transliterated approriately).
    4. A Hindi Caption (emotional, connecting to tradition).
    
    Output strictly in JSON format:
    {{
        "title_en": "...",
        "caption_en": "...",
        "title_hi": "...",
        "caption_hi": "..."
    }}
    """

    try:
        response = model.generate_content(prompt)
        # Clean up code blocks if present
        text = response.text.replace("```json", "").replace("```", "").strip()
        import json
        return json.loads(text)
    except Exception as e:
        print(f"Gemini Generation Error: {e}")
        return {
            "title_en": "Handcrafted Article",
            "caption_en": f"Beautiful handcrafted item. Story: {story}",
            "title_hi": "हस्तनिर्मित वस्तु",
            "caption_hi": f"सुंदर हस्तनिर्मित वस्तु। कहानी: {story}"
        }
