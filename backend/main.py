from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow Streamlit to talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ====== Request format Streamlit sends ======
class GenerateRequest(BaseModel):
    prompt: str
    image: str | None = None

# ====== API endpoint ======
@app.post("/api/generate")
def generate_listing(req: GenerateRequest):
    text = req.prompt.lower()

    if "saree" in text:
        return {
            "title": "Handmade Cotton Saree",
            "description": "Beautiful handcrafted cotton saree made with traditional South Indian weaving and eco-friendly dyes.",
            "price": "₹1,299",
            "tags": ["handmade", "cotton", "saree", "eco-friendly", "craftora"]
        }

    return {
        "title": "Handcrafted Product",
        "description": f"Artisan-made product based on: {req.prompt}",
        "price": "₹999",
        "tags": ["handmade", "craft", "craftora"]
    }