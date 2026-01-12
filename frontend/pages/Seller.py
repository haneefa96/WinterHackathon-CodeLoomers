import streamlit as st

st.set_page_config(page_title="Seller - Craftora", layout="wide")

# ================= PAGE STYLE =================
st.markdown("""
    <style>
    .stApp {
        background-color: #f3e6cf;
    }

    .seller-container {
        text-align: center;
        margin-top: 80px;
    }

    .seller-title {
        font-family: 'Playfair Display', serif;
        font-size: 60px;
        color: #6b442e;
        margin-bottom: 10px;
    }

    .tagline {
        font-size: 20px;
        color: #5a4a42;
        margin-bottom: 40px;
    }

    .section-box {
        background-color: #fff7e6;
        padding: 25px;
        border-radius: 15px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# ================= CONTENT =================
st.markdown("""
    <div class="seller-container">
        <div class="seller-title">Welcome</div>
        <div class="tagline">Create • Upload • Sell your handmade crafts</div>
    </div>
""", unsafe_allow_html=True)

# ================= INPUT MODE =================
st.markdown("### Choose input method")

col1, col2 = st.columns(2)

with col1:
    voice_btn = st.button("🎤 Voice Input")

with col2:
    text_btn = st.button("⌨️ Text Input")

if voice_btn:
    st.info("🎤 Voice input selected (backend integration pending)")
    # BACKEND HOOK: Voice recognition logic here

if text_btn:
    text_prompt = st.text_area("Enter product details")
    # BACKEND HOOK: Use this text as input

# ================= IMAGE UPLOAD =================
st.markdown("### Upload Product Image")

uploaded_image = st.file_uploader(
    "Upload an image of your craft",
    type=["png", "jpg", "jpeg"]
)

if uploaded_image:
    st.image(uploaded_image, caption="Uploaded Image", width=300)
    # BACKEND HOOK: Save image / send to model

# ================= GENERATE CONTENT =================
st.markdown("### Generate Content")

generate_btn = st.button("✨ Generate Content")

if generate_btn:
    st.success("Generating content...")
    
    # BACKEND HOOK (IMPORTANT)
    # Example:
    # result = generate_description(text_prompt, uploaded_image)
    # st.write(result)

    st.write("""
    📝 **Sample Output**
    - Product Name: Handmade Terracotta Vase  
    - Description: Crafted by skilled artisans using traditional techniques...
    - Tags: #Handmade #EcoFriendly #Craftora
    """)