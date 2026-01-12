# # def generate_craft_twin(story, attributes):
# #     return "generated content will come here"
# from vertexai.preview.generative_models import GenerativeModel
# import vertexai

# PROJECT_ID = "codeloomers-484010"
# LOCATION = "us-central1"

# vertexai.init(project=PROJECT_ID, location=LOCATION)

# model = GenerativeModel("gemini-1.5-flash")

# def generate_craft_twin(story: str, labels: list):
#     prompt = f"""
# You are an expert in Indian handicrafts.

# Story from artisan:
# {story}

# Detected image labels:
# {", ".join(labels)}

# Generate:
# 1. Product title
# 2. Product description (2 lines)
# 3. Instagram caption with hashtags
# """

#     response = model.generate_content(prompt)

#     return {
#         "ai_output": response.text
#     }

import vertexai
from vertexai.generative_models import GenerativeModel

PROJECT_ID = "codeloomers-484010"
LOCATION = "us-central1"

vertexai.init(project=PROJECT_ID, location=LOCATION)

model = GenerativeModel("gemini-1.5-flash")

def generate_craft_twin(story: str, labels: list):
    prompt = f"""
You are an expert in Indian handicrafts.

Story from artisan:
{story}

Detected image labels:
{", ".join(labels)}

Generate:
1. Product title
2. Product description (2 lines)
3. Instagram caption with hashtags
"""

    response = model.generate_content(prompt)

    return {
        "ai_output": response.text
    }
