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
            <img src="data:image/jpeg;base64,{seller_icon}">
            Seller
        </a>
        <a class="custom-btn" href="/Buyer">
            <img src="data:image/jpeg;base64,{buyer_icon}">
            Buyer
        </a>
    </div>
    """,
    unsafe_allow_html=True
)