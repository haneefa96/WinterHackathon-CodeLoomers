# import streamlit as st
# import requests
# from audiorecorder import audiorecorder

# st.set_page_config(
#     page_title="CodeLoomers",
#     page_icon="🧙‍♀️",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# st.markdown("""
#     <style>
#     .big-button {font-size: 24px; height: 60px;}
#     </style>
# """, unsafe_allow_html=True)

# # Backend URL
# BACKEND_URL = "http://localhost:8000"

# # Header
# st.title("🧙‍♀️ CodeLoomers")
# st.markdown("**Press green buttons. Speak your story. No typing needed.**")

# # Sidebar tabs
# tab = st.sidebar.radio("Choose:", ["🏠 Home", "👩‍🎨 Artisan", "🧵 Buyer"])

# if tab == "🏠 Home":
#     st.header("🎤 Tell Your Story")
#     st.markdown("**Press the green button and start speaking.**")
    
#     # Big mic button
#     if st.button("🎤 Start Talking", key="home_mic", use_container_width=True, help="One tap to record"):
#         st.balloons()
#         st.success("✅ Go to Artisan tab to upload photos!")
    
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button("👂 My Stories", use_container_width=True):
#             st.rerun()
#     with col2:
#         if st.button("❓ Voice Help", use_container_width=True):
#             st.info("🗣️ This app records your voice, makes craft listings, helps buyers find you.")


# elif tab == "👩‍🎨 Artisan":
#     st.header("👩‍🎨 Record & Create Listings")
    
#     # 1. Record story (FIXED)
#     st.subheader("1️⃣ Record Your Story") 
#     audio_file = st.file_uploader("📱 Upload voice note (WAV/MP3)", type=["wav", "mp3"])
#     story_text = st.text_area("✍️ Or type your story", placeholder="My family weaves silk sarees...", height=100)

#     # Story ready button (FIXED)
#     if st.button("✅ Story Ready!", use_container_width=True) and (audio_file or story_text.strip()):
#         st.success("✅ Story processed!")

#     # 2. Photos
#     st.subheader("2️⃣ Add Photos")
#     photos = st.file_uploader(
#         "Drag craft photos here (1-5)",
#         type=["jpg", "png", "jpeg"],
#         accept_multiple_files=True
#     )
#     photo_count = len(photos) if photos else 0
    
#     # 3. Generate (FIX - use story_text variable)
#     st.subheader("3️⃣ ✨ Generate Content")
#     if st.button("✨ Create My Listings", use_container_width=True) and story_text.strip():
#         try:
#             resp = requests.post(f"{BACKEND_URL}/artisan/generate", 
#                                data={"story": story_text.strip(), "photo_count": photo_count})
#             data = resp.json()
            
#             st.success("✅ Generated!")
#             col1, col2 = st.columns(2)
#             with col1:
#                 st.metric("🇺🇸 English Title", data["title_en"])
#                 st.info(data["caption_en"])
#             with col2:
#                 st.metric("🇮🇳 Local Title", data["title_hi"])
#                 st.info(data["caption_hi"])
                
#             st.download_button("💾 Download CSV", 
#                              f"title,caption\n{data['title_en']},{data['caption_en']}")
#         except:
#             st.error("Backend not running? Start: cd backend && uvicorn main:app --reload")

# # elif tab == "👩‍🎨 Artisan":
# #     st.header("👩‍🎨 Record & Create Listings")
    
# #     # # 1. Record story
# #     # st.subheader("1️⃣ Record Your Story")
# #     # audio = audiorecorder("Click to speak", "Click to stop")
# #     # 1. Record story (Real Speech-to-Text ready)
# #     st.subheader("1️⃣ Record Your Story") 
# #     audio_file = st.file_uploader("📱 Upload voice note (WAV/MP3)", type=["wav", "mp3"])
# #     story_text = st.text_area("✍️ Or type your story", placeholder="My family weaves silk sarees...", height=100)

# #     # Mock button for demo (real audio upload works)
# #     if st.button("✅ Story Ready!", use_container_width=True) and (audio_file or story_text.strip()):
# #         st.success("✅ Story processed!")

# #     story_text = ""
    
# #     if len(audio) > 0:
# #         # Save audio (mock send to backend)
# #         st.audio(audio.export().read())
# #         story_text = "My family makes beautiful sarees in village."  # Mock STT
# #         st.success("✅ Story recorded!")
    
# #     # 2. Photos
# #     st.subheader("2️⃣ Add Photos")
# #     photos = st.file_uploader(
# #         "Drag craft photos here (1-5)",
# #         type=["jpg", "png", "jpeg"],
# #         accept_multiple_files=True
# #     )
# #     photo_count = len(photos) if photos else 0
    
# #     # 3. Generate (PPT core)
# #     st.subheader("3️⃣ ✨ Generate Content")
# #     if st.button("✨ Create My Listings", use_container_width=True) and story_text:
# #         try:
# #             resp = requests.post(f"{BACKEND_URL}/artisan/generate", 
# #                                data={"story": story_text, "photo_count": photo_count})
# #             data = resp.json()
            
# #             st.success("✅ Generated!")
# #             col1, col2 = st.columns(2)
# #             with col1:
# #                 st.metric("🇺🇸 English Title", data["title_en"])
# #                 st.info(data["caption_en"])
# #             with col2:
# #                 st.metric("🇮🇳 Local Title", data["title_hi"])
# #                 st.info(data["caption_hi"])
            
# #             st.download_button("💾 Download CSV", "title,caption\n" + data["title_en"] + "," + data["caption_en"])
# #         except:
# #             st.error("Backend not running? Start: uvicorn main:app --reload")

# elif tab == "🧵 Buyer":
#     st.header("🧵 Discover Artisan Stories")
    
#     query = st.text_input("🔍 Search stories/themes", placeholder="Karnataka silk...")
    
#     if st.button("Search", use_container_width=True):
#         try:
#             resp = requests.get(f"{BACKEND_URL}/buyer/search", params={"q": query})
#             data = resp.json()
            
#             for result in data["results"]:
#                 with st.container():
#                     st.markdown("---")
#                     st.subheader(result.get("title_en", "Artisan Story"))
#                     st.caption(result.get("story", ""))
#                     if st.button("👂 Listen", key=result.get("story", "")):
#                         st.balloons()
#         except:
#             st.info("💡 Record some artisans first in Artisan tab!")

# # Footer
# st.markdown("---")
# st.markdown("*Powered by Gemini AI. One-tap voice-first for artisans.*")



# # import streamlit as st
# # import requests

# # st.set_page_config(
# #     page_title="CodeLoomers",
# #     page_icon="🧙‍♀️",
# #     layout="wide",
# #     initial_sidebar_state="expanded"
# # )

# # st.markdown("""
# #     <style>
# #     .big-button {font-size: 24px; height: 60px;}
# #     </style>
# # """, unsafe_allow_html=True)

# # BACKEND_URL = "http://localhost:8000"

# # st.title("🧙‍♀️ CodeLoomers")
# # st.markdown("**Press green buttons. Speak your story. No typing needed.**")

# # tab = st.sidebar.radio("Choose:", ["🏠 Home", "👩‍🎨 Artisan", "🧵 Buyer"])

# # if tab == "🏠 Home":
# #     st.header("🎤 Tell Your Story")
# #     st.markdown("**Press the green button and start speaking.**")
    
# #     if st.button("🎤 Start Talking", key="home_mic", use_container_width=True):
# #         st.balloons()
# #         st.success("✅ Go to Artisan tab to upload photos!")
    
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         if st.button("👂 My Stories", use_container_width=True):
# #             st.rerun()
# #     with col2:
# #         if st.button("❓ Voice Help", use_container_width=True):
# #             st.info("🗣️ This app records your voice, makes craft listings, helps buyers find you.")

# # elif tab == "👩‍🎨 Artisan":
# #     st.header("👩‍🎨 Record & Create Listings")
    
# #     # 1. Mock audio with button (native Streamlit)
# #     st.subheader("1️⃣ Record Your Story")
# #     story_text = st.text_area("Paste/type your story (voice coming soon)", 
# #                              placeholder="My family makes sarees...")
    
# #     if st.button("🎤 Story Recorded ✅", use_container_width=True):
# #         st.success("✅ Story ready!")
    
# #     # 2. Photos
# #     st.subheader("2️⃣ Add Photos")
# #     photos = st.file_uploader(
# #         "Drag craft photos here (1-5)",
# #         type=["jpg", "png", "jpeg"],
# #         accept_multiple_files=True
# #     )
# #     photo_count = len(photos) if photos else 0
    
# #     # 3. Generate
# #     st.subheader("3️⃣ ✨ Generate Content")
# #     if st.button("✨ Create My Listings", use_container_width=True) and story_text:
# #         try:
# #             resp = requests.post(f"{BACKEND_URL}/artisan/generate", 
# #                                data={"story": story_text, "photo_count": photo_count})
# #             data = resp.json()
            
# #             st.success("✅ Generated!")
# #             col1, col2 = st.columns(2)
# #             with col1:
# #                 st.metric("🇺🇸 English", data["title_en"])
# #                 st.info(data["caption_en"])
# #             with col2:
# #                 st.metric("🇮🇳 Hindi", data["title_hi"])
# #                 st.info(data["caption_hi"])
            
# #             st.download_button("💾 CSV", 
# #                              f"title,caption\n{data['title_en']},{data['caption_en']}")
# #         except:
# #             st.error("Start backend: cd backend && uvicorn main:app --reload")

# # elif tab == "🧵 Buyer":
# #     st.header("🧵 Discover Stories")
    
# #     query = st.text_input("🔍 Search", placeholder="Karnataka silk...")
    
# #     if st.button("Search", use_container_width=True):
# #         try:
# #             resp = requests.get(f"{BACKEND_URL}/buyer/search", params={"q": query})
# #             data = resp.json()
            
# #             for result in data["results"]:
# #                 st.markdown("---")
# #                 st.subheader(result.get("title_en", "Story"))
# #                 st.caption(result.get("story", ""))
# #                 if st.button("👂 Listen", key=result.get("story", "")):
# #                     st.balloons()
# #         except:
# #             st.info("Record artisans first!")

# # st.markdown("---")
# # st.markdown("*Powered by Gemini AI*")


# # import streamlit as st
# # import requests
# # from audiorecorder import audiorecorder

# # st.set_page_config(
# #     page_title="Craftora",
# #     page_icon="🧵",
# #     layout="wide",
# #     initial_sidebar_state="expanded"
# # )

# # # Background styling with plain texture
# # def add_bg_from_url():
# #     st.markdown(
# #         """
# #         <style>
# #         .stApp {
# #             background: linear-gradient(135deg, #f5f1ed 0%, #ede8e3 100%);
# #             background-attachment: fixed;
# #         }
        
# #         /* Sidebar styling */
# #         [data-testid="stSidebar"] {
# #             background: rgba(245, 241, 237, 0.95);
# #             border-right: 1px solid rgba(158, 130, 111, 0.1);
# #         }
        
# #         /* Main content card - hanging style */
# #         .main-card {
# #             background: #9b8b7e;
# #             border-radius: 8px;
# #             padding: 40px;
# #             color: white;
# #             position: relative;
# #             box-shadow: 0 12px 32px rgba(0, 0, 0, 0.15);
# #             min-height: 500px;
# #             display: flex;
# #             flex-direction: column;
# #             justify-content: center;
# #         }
        
# #         .main-card::before {
# #             content: '';
# #             position: absolute;
# #             top: -16px;
# #             left: 50%;
# #             transform: translateX(-50%);
# #             width: 4px;
# #             height: 16px;
# #             background: #2d2d2d;
# #             border-radius: 2px;
# #         }
        
# #         /* Button styling */
# #         .stButton > button {
# #             background: linear-gradient(135deg, #32a89f 0%, #218078 100%);
# #             color: white;
# #             border: none;
# #             border-radius: 8px;
# #             font-weight: 600;
# #             transition: all 0.3s ease;
# #             box-shadow: 0 4px 12px rgba(50, 168, 159, 0.3);
# #             padding: 12px 24px !important;
# #             font-size: 16px !important;
# #         }
        
# #         .stButton > button:hover {
# #             background: linear-gradient(135deg, #2a9a91 0%, #1a6d6a 100%);
# #             box-shadow: 0 6px 16px rgba(50, 168, 159, 0.4);
# #             transform: translateY(-2px);
# #         }
        
# #         /* Title styling */
# #         h1 {
# #             color: #3f3530;
# #             font-weight: 700;
# #             letter-spacing: -0.5px;
# #         }
        
# #         h2 {
# #             color: #5a4a40;
# #             font-weight: 600;
# #         }
        
# #         h3 {
# #             color: #6b5b51;
# #             font-weight: 600;
# #         }
        
# #         /* Centered card title */
# #         .card-title {
# #             color: white;
# #             font-size: 28px;
# #             font-weight: 700;
# #             margin-bottom: 20px;
# #             text-align: center;
# #         }
        
# #         .card-subtitle {
# #             color: rgba(255, 255, 255, 0.9);
# #             font-size: 16px;
# #             line-height: 1.6;
# #             text-align: center;
# #             margin-bottom: 30px;
# #         }
        
# #         .card-tagline {
# #             color: rgba(255, 255, 255, 0.8);
# #             font-size: 14px;
# #             text-align: center;
# #             margin-top: 20px;
# #             font-style: italic;
# #         }
        
# #         /* Button container */
# #         .button-container {
# #             display: flex;
# #             flex-direction: column;
# #             gap: 12px;
# #             margin-top: 30px;
# #         }
        
# #         /* Text input styling */
# #         .stTextInput > div > div > input {
# #             background: rgba(255, 255, 255, 0.9);
# #             border: 1.5px solid rgba(158, 130, 111, 0.2);
# #             border-radius: 8px;
# #             color: #3f3530;
# #         }
        
# #         .stTextInput > div > div > input:focus {
# #             border-color: rgba(50, 168, 159, 0.5);
# #             box-shadow: 0 0 0 2px rgba(50, 168, 159, 0.1);
# #         }
        
# #         /* Radio button styling */
# #         [role="radio"] {
# #             accent-color: #32a89f;
# #         }
        
# #         /* Success/Info message styling */
# #         .stSuccess {
# #             background: rgba(34, 197, 94, 0.1);
# #             border: 1px solid rgba(34, 197, 94, 0.3);
# #             border-radius: 8px;
# #         }
        
# #         .stInfo {
# #             background: rgba(59, 130, 246, 0.1);
# #             border: 1px solid rgba(59, 130, 246, 0.3);
# #             border-radius: 8px;
# #         }
        
# #         .stError {
# #             background: rgba(239, 68, 68, 0.1);
# #             border: 1px solid rgba(239, 68, 68, 0.3);
# #             border-radius: 8px;
# #         }
        
# #         /* Hide default streamlit elements for home page */
# #         .home-page .stMetric {
# #             background: transparent;
# #         }
# #         </style>
# #         """,
# #         unsafe_allow_html=True
# #     )

# # add_bg_from_url()

# # # Backend URL
# # BACKEND_URL = "http://localhost:8000"

# # # Header
# # st.title("🧵 Craftora")
# # st.markdown("**Press green buttons. Speak your story. No typing needed.**")

# # # Sidebar tabs
# # tab = st.sidebar.radio("Choose:", ["🏠 Home", "👩‍🎨 Artisan", "🧵 Buyer"])

# # if tab == "🏠 Home":
# #     # Hide header for cleaner look
# #     st.markdown("""
# #         <style>
# #         [data-testid="stHeaderActionElements"] {display: none;}
# #         </style>
# #     """, unsafe_allow_html=True)
    
# #     # Create two-column layout
# #     col1, col2 = st.columns([1.1, 0.9])
    
# #     with col1:
# #         # Display pottery image on the left
# #         st.image(
# #             "https://agi-prod-file-upload-public-main-use1.s3.amazonaws.com/adf91dda-4568-492d-a7f2-92363af089b5",
# #             use_column_width=True
# #         )
    
# #     with col2:
# #         # Main card on the right
# #         st.markdown(
# #             """
# #             <div class="main-card">
# #                 <div class="card-title">Welcome to Craftora</div>
                
# #                 <div class="card-subtitle">
# #                     Press the green button and share your craft story. Our AI will help you create beautiful listings that connect you with buyers who appreciate your work.
# #                 </div>
                
# #                 <div class="card-tagline">✨ No typing. Just speak. We handle the rest.</div>
# #             </div>
# #             """,
# #             unsafe_allow_html=True
# #         )
        
# #         # Buttons below the card
# #         st.markdown("<div class='button-container'>", unsafe_allow_html=True)
        
# #         if st.button("🎤 Start Talking", key="home_mic", use_container_width=True):
# #             st.balloons()
# #             st.success("✅ Go to Artisan tab to upload photos!")
        
# #         col_a, col_b = st.columns(2)
# #         with col_a:
# #             if st.button("👂 My Stories", use_container_width=True):
# #                 st.rerun()
# #         with col_b:
# #             if st.button("❓ Voice Help", use_container_width=True):
# #                 st.info("🗣️ Record your craft story → Add photos → Get AI-generated listings in English & local language")
        
# #         st.markdown("</div>", unsafe_allow_html=True)

# # elif tab == "👩‍🎨 Artisan":
# #     st.header("👩‍🎨 Record & Create Listings")
    
# #     # 1. Record story
# #     st.subheader("1️⃣ Record Your Story")
    
# #     st.markdown(
# #         """
# #         <div style="background: rgba(255,255,255,0.7); border-radius: 12px; padding: 16px; border: 1px solid rgba(158,130,111,0.15); margin-bottom: 16px;">
# #             <p style="color: #6b5b51; margin: 0;">Click the microphone to record your craft story in your own words.</p>
# #         </div>
# #         """,
# #         unsafe_allow_html=True
# #     )
    
# #     audio = audiorecorder("Click to speak", "Click to stop")
# #     story_text = ""
    
# #     if len(audio) > 0:
# #         st.audio(audio.export().read())
# #         story_text = "My family makes beautiful sarees in village."  # Mock STT
# #         st.success("✅ Story recorded! Proceeding to photo upload...")
    
# #     # 2. Photos
# #     st.subheader("2️⃣ Add Your Craft Photos")
    
# #     st.markdown(
# #         """
# #         <div style="background: rgba(255,255,255,0.7); border-radius: 12px; padding: 16px; border: 1px solid rgba(158,130,111,0.15); margin-bottom: 16px;">
# #             <p style="color: #6b5b51; margin: 0;">Upload 1-5 photos of your handcrafted items. High-quality images work best!</p>
# #         </div>
# #         """,
# #         unsafe_allow_html=True
# #     )
    
# #     photos = st.file_uploader(
# #         "Drag craft photos here (1-5)",
# #         type=["jpg", "png", "jpeg"],
# #         accept_multiple_files=True,
# #         label_visibility="collapsed"
# #     )
# #     photo_count = len(photos) if photos else 0
    
# #     if photos:
# #         st.success(f"✅ {photo_count} photo(s) uploaded")
# #         cols = st.columns(min(3, len(photos)))
# #         for idx, photo in enumerate(photos[:3]):
# #             with cols[idx % 3]:
# #                 st.image(photo, use_column_width=True)
    
# #     # 3. Generate
# #     st.subheader("3️⃣ ✨ Generate Content")
    
# #     st.markdown(
# #         """
# #         <div style="background: rgba(255,255,255,0.7); border-radius: 12px; padding: 16px; border: 1px solid rgba(158,130,111,0.15); margin-bottom: 16px;">
# #             <p style="color: #6b5b51; margin: 0;">Our AI will create professional listings in English and your local language.</p>
# #         </div>
# #         """,
# #         unsafe_allow_html=True
# #     )
    
# #     if st.button("✨ Create My Listings", use_container_width=True):
# #         if story_text:
# #             try:
# #                 resp = requests.post(f"{BACKEND_URL}/artisan/generate", 
# #                                    data={"story": story_text, "photo_count": photo_count})
# #                 data = resp.json()
                
# #                 st.success("✅ Generated!")
                
# #                 col1, col2 = st.columns(2)
                
# #                 with col1:
# #                     st.markdown(
# #                         f"""
# #                         <div style="background: rgba(255,255,255,0.7); border-radius: 12px; padding: 20px; border: 1px solid rgba(158,130,111,0.15);">
# #                             <h4 style="color: #32a89f; margin-top: 0;">🇺🇸 English</h4>
# #                             <p style="font-weight: 600; color: #3f3530;">{data.get('title_en', 'Artisan Craft')}</p>
# #                             <p style="color: #6b5b51; font-size: 0.95em;">{data.get('caption_en', '')}</p>
# #                         </div>
# #                         """,
# #                         unsafe_allow_html=True
# #                     )
                
# #                 with col2:
# #                     st.markdown(
# #                         f"""
# #                         <div style="background: rgba(255,255,255,0.7); border-radius: 12px; padding: 20px; border: 1px solid rgba(158,130,111,0.15);">
# #                             <h4 style="color: #32a89f; margin-top: 0;">🇮🇳 Local</h4>
# #                             <p style="font-weight: 600; color: #3f3530;">{data.get('title_hi', 'शिल्प')}</p>
# #                             <p style="color: #6b5b51; font-size: 0.95em;">{data.get('caption_hi', '')}</p>
# #                         </div>
# #                         """,
# #                         unsafe_allow_html=True
# #                     )
                
# #                 st.download_button(
# #                     "💾 Download CSV",
# #                     "title,caption\n" + data.get("title_en", "") + "," + data.get("caption_en", ""),
# #                     file_name="craftora_listing.csv"
# #                 )
# #             except Exception as e:
# #                 st.error("⚠️ Backend not running? Start: uvicorn main:app --reload")
# #         else:
# #             st.warning("🎤 Please record a story first!")

# # elif tab == "🧵 Buyer":
# #     st.header("🧵 Discover Artisan Stories")
    
# #     st.markdown(
# #         """
# #         <div style="background: rgba(255,255,255,0.7); border-radius: 12px; padding: 16px; border: 1px solid rgba(158,130,111,0.15); margin-bottom: 16px;">
# #             <p style="color: #6b5b51; margin: 0;">Search for handcrafted items by theme, location, or craft type.</p>
# #         </div>
# #         """,
# #         unsafe_allow_html=True
# #     )
    
# #     query = st.text_input(
# #         "🔍 Search",
# #         placeholder="e.g., Karnataka silk, handwoven, pottery...",
# #         label_visibility="collapsed"
# #     )
    
# #     if st.button("Search", use_container_width=True):
# #         if query:
# #             try:
# #                 resp = requests.get(f"{BACKEND_URL}/buyer/search", params={"q": query})
# #                 data = resp.json()
                
# #                 if data.get("results"):
# #                     for result in data["results"]:
# #                         st.markdown(
# #                             f"""
# #                             <div style="background: rgba(255,255,255,0.7); border-radius: 12px; padding: 20px; border: 1px solid rgba(158,130,111,0.15); margin-bottom: 16px;">
# #                                 <h3 style="margin-top: 0; color: #5a4a40;">{result.get('title_en', 'Artisan Story')}</h3>
# #                                 <p style="color: #6b5b51; line-height: 1.6;">{result.get('story', '')}</p>
# #                             </div>
# #                             """,
# #                             unsafe_allow_html=True
# #                         )
                        
# #                         col1, col2 = st.columns([1, 3])
# #                         with col1:
# #                             if st.button("👂 Listen", key=result.get("story", "")[:50]):
# #                                 st.balloons()
# #                                 st.info("🎧 Audio playing...")
# #                 else:
# #                     st.info("💡 No results found. Try a different search or record some artisans first!")
# #             except Exception as e:
# #                 st.error("⚠️ Search unavailable. Check backend connection.")
# #         else:
# #             st.info("💡 Enter a search term to discover artisan stories!")

# # # Footer
# # st.markdown("---")
# # st.markdown(
# #     """
# #     <div style="text-align: center; color: #8b7b6b; font-size: 0.9em;">
# #     <p>🧵 <b>Craftora</b> • Powered by Gemini AI</p>
# #     <p><em>One-tap voice-first platform connecting artisans with buyers worldwide</em></p>
# #     </div>
# #     """,
# #     unsafe_allow_html=True
# # )

import streamlit as st
import base64

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="Craftora",
    page_icon="🎨",
    layout="wide"
)

# ================= LOAD IMAGES =================
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

bg_image = get_base64("background.jpeg")
seller_icon = get_base64("Seller.jpeg")
buyer_icon = get_base64("Buyer.jpeg")

# ================= CSS =================
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;800&display=swap');

    .stApp {{
        background-image: url("data:image/png;base64,{bg_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        min-height: 100vh;
    }}

    [data-testid="stAppViewContainer"],
    [data-testid="stMain"] {{
        background: transparent;
    }}

    .hero-container {{
        text-align: center;
        margin-top: 60px;   /* MOVED UP (was 110px) */
    }}

    .title {{
        font-family: 'Playfair Display', serif;
        font-size: 88px;
        font-weight: 700;
        color: #6b442e;
        margin-bottom: 10px;
    }}

    .subtitle {{
        font-family: 'Playfair Display', serif;
        font-size: 30px;
        color: #6b442e;
        margin-bottom: 6px;
    }}

    .tagline {{
        font-family: 'Playfair Display', serif;
        font-size: 20px;
        color: #6b442e;
        margin-bottom: 30px;   /* slightly reduced */
        line-height: 1.5;
    }}

    /* ICON BUTTONS */
    .btn-container {{
        display: flex;
        justify-content: center;
        gap: 80px;
        margin-top: 10px;   /* moved up a bit */
    }}

    .custom-btn {{
        display: flex;
        align-items: center;
        gap: 16px;
        background-color: #8b5a34;
        padding: 12px 30px;
        border-radius: 40px;
        text-decoration: none !important;
        font-family: 'Playfair Display', serif;
        font-size: 27px;
        font-weight: 700;
        transition: 0.3s ease;
        cursor: pointer;
        color: #f3e6cf !important;
    }}

    .custom-btn:visited {{
        color: #f3e6cf !important;
    }}

    .custom-btn:hover {{
        background-color: #734626;
        color: #f3e6cf !important;
        transform: scale(1.03);
    }}

    .custom-btn:active {{
        color: #f3e6cf !important;
    }}

    /* ROUND BIG ICONS */
    .custom-btn img {{
        width: 60px;
        height: 60px;
        border-radius: 50%;
        object-fit: cover;
        border: 2px solid #fff;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ================= HERO CONTENT =================
st.markdown(
    """
    <div class="hero-container">
        <div class="title">Craftora</div>
        <div class="subtitle">Where Every Craft Tells a Story</div>
        <div class="tagline">
            Speak Your Craft • Share Your Story • Connect with Buyers
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# ================= ICON BUTTONS =================
st.markdown(
    f"""
    <div class="btn-container">
        <a class="custom-btn" href="/Seller">
            <img src="data:image/png;base64,{seller_icon}">
            Seller
        </a>
        <a class="custom-btn" href="/Buyer">
            <img src="data:image/png;base64,{buyer_icon}">
            Buyer
        </a>
    </div>
    """,
    unsafe_allow_html=True
)