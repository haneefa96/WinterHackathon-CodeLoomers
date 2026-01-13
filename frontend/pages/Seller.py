import streamlit as st
import requests
import base64

st.set_page_config(page_title="Seller - Craftora", layout="wide")

# ================= PAGE STYLE =================
st.markdown("""
    <style>
    .stApp {
        background-color: #f3e6cf;
    }

    .seller-container {
        text-align: center;
        margin-top: 60px;
    }

    .seller-title {
        font-family: 'Playfair Display', serif;
        font-size: 60px;
        color: #6b442e;
        margin-bottom: 5px;
    }

    .tagline {
        font-size: 20px;
        color: #5a4a42;
        margin-bottom: 30px;
    }

    .section-box {
        background-color: #fff7e6;
        padding: 25px;
        border-radius: 15px;
        margin-top: 20px;
    }

    /* Only requested text → black */
    .black-text {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("""
    <div class="seller-container">
        <div class="seller-title">Welcome</div>
        <div class="tagline">Create • Upload • Sell your handmade crafts</div>
    </div>
""", unsafe_allow_html=True)

# ================= INPUT =================
st.markdown('<h3 class="black-text">📝 Enter product details</h3>', unsafe_allow_html=True)

text_prompt = st.text_area(
    "Describe your product",
    placeholder="Eg: Handmade cotton saree with traditional patterns, eco friendly dye, festive wear"
)

# force only label to black
st.markdown("""
    <style>
    label:has(+ textarea) { color: black !important; }
    </style>
""", unsafe_allow_html=True)

# ================= IMAGE =================
st.markdown('<h3 class="black-text">🖼 Upload product image</h3>', unsafe_allow_html=True)

uploaded_image = st.file_uploader("Upload image", type=["png", "jpg", "jpeg"])

# force upload text to black
st.markdown("""
    <style>
    div[data-testid="stFileUploader"] label {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

if uploaded_image:
    st.image(uploaded_image, width=300)

# ================= GENERATE =================
st.markdown('<h3 class="black-text">✨ Generate AI Listing</h3>', unsafe_allow_html=True)

generate_btn = st.button("Generate Listing")

# force button text to black
st.markdown("""
    <style>
    button[kind="primary"] span, button span {
        color: black !important;
    }
    </style>
""", unsafe_allow_html=True)

if generate_btn:
    if not text_prompt:
        st.error("Please enter product details")
    else:
        with st.spinner("AI is creating your product listing..."):

            img_base64 = ""
            if uploaded_image:
                img_bytes = uploaded_image.read()
                img_base64 = base64.b64encode(img_bytes).decode()

            payload = {
                "prompt": text_prompt,
                "image": img_base64
            }

            try:
                res = requests.post(
                    "http://127.0.0.1:8000/api/generate",
                    json=payload,
                    timeout=120
                )

                if res.status_code != 200:
                    st.error("Backend Error")
                    st.error(res.text)

                else:
                    data = res.json()

                    st.success("Listing generated successfully!")

                    st.markdown("### 🛍 Product Title")
                    st.write(data["title"])

                    st.markdown("### 📄 Description")
                    st.write(data["description"])

                    st.markdown("### 📢 Marketing Caption")
                    st.write(data["caption"])

                    st.markdown("### 🏷 Tags")
                    st.write(", ".join(data["tags"]))

            except Exception as e:
                st.error("Backend not connected")
                st.error(str(e))