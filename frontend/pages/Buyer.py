import streamlit as st

st.set_page_config(page_title="Buyer - Craftora", layout="wide")

# ================= CSS =================
st.markdown("""
<style>
.stApp {
    background-color: #f3e6cf;
}

.buyer-container {
    text-align: center;
    margin-top: 120px;
}

.buyer-title {
    font-family: 'Playfair Display', serif;
    font-size: 60px;
    color: #6b442e;
    margin-bottom: 0px;   /* subtitle very close */
}

.buyer-subtitle {
    font-family: 'Playfair Display', serif;
    font-size: 26px;
    color: #9c7b60;
    margin-top: 0px;
    margin-bottom: 40px;  /* space before search button */
}

/* FULL WIDTH SEARCH BUTTON */
.search-btn {
    background-color: #3e2f22;  /* dark brown */
    color: #f3e6cf;  /* beige text */
    padding: 16px 0;       /* vertical padding */
    font-size: 26px;
    font-family: 'Playfair Display', serif;
    border-radius: 40px;
    border: none;
    cursor: pointer;
    width: 50%;           /* <-- makes it really wide */
    max-width: 500px;     /* optional max width */
    display: block;
    margin: 0 auto;       /* center the button */
    transition: 0.3s ease;
}

.search-btn:hover {
    background-color: #2a1d14;  /* darker on hover */
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# ================= PAGE CONTENT =================
st.markdown("""
<div class="buyer-container">
    <div class="buyer-title">Welcome</div>
    <div class="buyer-subtitle">Quality You Can Trust</div>
</div>
""", unsafe_allow_html=True)

# ================= SEARCH BUTTON =================
st.markdown("""
<div>
    <button class="search-btn">🔍 Search</button>
</div>
""", unsafe_allow_html=True)