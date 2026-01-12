# def generate_artisan_content(story, labels=None, vision_data=None):
#     """
#     Placeholder for Gemini text generation
#     """
#     return {
#         "title": f"Handcrafted {labels or 'Artisan Product'}",
#         "description": f"{story}. This product reflects traditional craftsmanship.",
#         "caption": "Made with care by Indian artisans"
#     }

# # PROJECT_ID = "codeloomers-484010"
# # LOCATION = "us-central1"

# # vertexai.init(project=PROJECT_ID, location=LOCATION)

# # model = GenerativeModel("gemini-1.5-flash")

# # def generate_craft_twin(story: str, labels: list):
# #     prompt = f"""
# # You are an expert in Indian handicrafts.

# # Story from artisan:
# # {story}

# # Detected image labels:
# # {", ".join(labels)}

# # Generate:
# # 1. Product title
# # 2. Product description (2 lines)
# # 3. Instagram caption with hashtags
# # """

# #     response = model.generate_content(prompt)

# #     return {
# #         "ai_output": response.text
# #     }

def generate_ai_content(story, labels=None, vision_data=None):
    """
    Placeholder for Gemini AI content generation
    """
    return {
        "title": f"Handcrafted {labels or 'Artisan Product'}",
        "description": f"{story}. This product reflects traditional craftsmanship.",
        "caption": "Made with care by Indian artisans"
    }


# import vertexai
# from vertexai.preview.generative_models import GenerativeModel

# PROJECT_ID = "your-gcp-project-id"
# LOCATION = "us-central1"

# def generate_ai_content(story: str, labels: str):
#     vertexai.init(project=PROJECT_ID, location=LOCATION)

#     model = GenerativeModel("gemini-1.5-flash")

#     prompt = f"""
#     You are helping an artisan sell handmade products.

#     Story:
#     {story}

#     Labels:
#     {labels}

#     Generate:
#     1. A short title
#     2. A marketing caption
#     """

#     response = model.generate_content(prompt)

#     return {
#         "output": response.text
#     }
