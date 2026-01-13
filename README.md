 # Project Name

## Description
Briefly explain what your project does, the problem it solves, and who it is for.
Craftora is an AI-powered platform that helps Indian artisans bring their traditional crafts into the digital marketplace easily. Many artisans face challenges such as low digital literacy, language barriers, weak branding, and complex online selling platforms, which limit their reach to modern buyers.
Craftora solves this by creating a digital identity for each artisan. Using AI, it converts product images and voice stories into clear, multilingual product listings and buyer-ready content, allowing artisans to focus on crafting while Craftora manages their digital presence.


# Demo Video Link: https://drive.google.com/file/d/1ijY9-Tp_ibmHeYEXaanfSeBn0SKBUjyL/view?usp=drivesdk

## Features
-AI-generated listings from images and voice
-Multi-language content support
-Artisan & Buyer interfaces
-Story-based product discovery
-AI-powered search 

## Tech Stack
List the technologies, frameworks, and tools used in the project.
Frontend
-Streamlit / React web app
-Artisan: image upload, voice/story input, content generation
-Buyer: search or chat by theme or story

AI & ML (Google Cloud)
-Gemini Vision (Vertex AI): image understanding
-Speech-to-Text API: voice to text (Hindi, Kannada, etc.)
-Gemini Flash / Pro: listings, stories, captions, FAQs, multilingual output

Backend
-Python with FastAPI
-Deployed on Google Cloud Run

Data Storage
-Firestore & Cloud Storage
-Craftora profiles, tags, stories, media

Search
-Firestore retrieval
-Gemini-based re-ranking with explanations

Deployment
-Google Cloud Run, Vertex AI, Firestore

## Google Technologies Used
> ⚠️ Using Google products is **mandatory** for this hackathon.

List the Google technologies you used and clearly explain **why** you chose them.

**Example:**
- **Firebase Authentication** – For secure and easy user authentication
- **Firebase Firestore** – To store and manage real-time data
- **Google Maps API** – To enable location-based features

Vertex AI (Gemini Pro / Flash, multimodal) – Used for core text and image understanding and AI-based content generation.

Vertex AI Vision / Multimodal Gemini – Chosen to extract product attributes such as type, colors, and patterns from images.

Cloud Speech-to-Text – Converts local-language voice notes into text, enabling voice-first input for artisans.

Firestore & Cloud Storage – Stores Craftora digital profiles, product images, and generated content securely and efficiently.

Google Cloud Run – Hosts the backend as a containerized service with automatic scaling and simple deployment.

BigQuery / Looker Studio (Optional) – Enables future analysis of content and story performance to improve recommendations.




## Setup Instructions
Steps to run the project locally:
1. Clone the repository
2. Install dependencies
3. check assets
4. Run the project

## Team Members
-Haneefa Riham - backend
-Melria Smitha Gonsalves-Documentation and presentation
-Rifa Nashwa-frontend and UI design
-S Vaishnavi-AI and google integration
