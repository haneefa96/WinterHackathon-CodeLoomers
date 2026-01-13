import streamlit as st
import requests

st.set_page_config(page_title="Buyer - Craftora", layout="wide")

# ================== STYLES ==================
st.markdown("""
<style>
.stApp {
    background-color: #f3e6cf;
}

.buyer-container {
    text-align: center;
    margin-top: 60px;
}

.buyer-title {
    font-family: 'Playfair Display', serif;
    font-size: 60px;
    color: #6b442e;
}

.buyer-subtitle {
    font-family: 'Playfair Display', serif;
    font-size: 24px;
    color: #9c7b60;
    margin-bottom: 40px;
}

.search-box {
    width: 60%;
    font-size: 22px;
    padding: 12px;
    border-radius: 20px;
    border: none;
    margin-bottom: 20px;
}

.search-btn {
    background-color: #3e2f22;
    color: #f3e6cf;
    padding: 14px 40px;
    font-size: 22px;
    border-radius: 30px;
    border: none;
    cursor: pointer;
}
</style>
""", unsafe_allow_html=True)

# ================== UI ==================
st.markdown("""
<div class="buyer-container">
    <div class="buyer-title">Welcome</div>
    <div class="buyer-subtitle">Quality You Can Trust</div>
</div>
""", unsafe_allow_html=True)

query = st.text_input("What are you looking for?", placeholder="eg. Sarees, Pottery, Handmade jewelry")

if st.button("🔍 Search"):
    if query:
        try:
            response = requests.post(
                "http://127.0.0.1:8000/api/generate",
                json={"prompt": query}
            )

            if response.status_code == 200:
                result = response.json()["response"]
                st.success("✨ AI Found This:")
                st.write(result)
            else:
                st.error("Backend error")

        except:
            st.error("Backend not reachable")
