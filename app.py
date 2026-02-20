import streamlit as st
from rembg import remove
from PIL import Image
import io

# --- Page Config ---
st.set_page_config(page_title="Magic BG Remover", page_icon="✂️", layout="centered")

# --- Custom Styling ---
st.markdown("""
    <style>
    .main { text-align: center; }
    .stButton>button { width: 100%; border-radius: 20px; background-color: #FF4B4B; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("✂️ AI Background Remover")
st.write("Upload an image and watch the background disappear instantly!")

# --- Sidebar / Options ---
st.sidebar.header("Settings")
add_transparency = st.sidebar.checkbox("Maximize Contrast", value=True)

# --- File Uploader ---
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Load Image
    input_image = Image.open(uploaded_file)
    
    # Create Columns for Layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Original")
        st.image(input_image, use_container_width=True)
        
    with col2:
        st.subheader("Result")
        # Process the image
        with st.spinner("AI is thinking..."):
            # Convert uploaded file to bytes for rembg
            img_bytes = uploaded_file.getvalue()
            output_bytes = remove(img_bytes)
            output_image = Image.open(io.BytesIO(output_bytes))
            
            st.image(output_image, use_container_width=True)

    # --- Download Button ---
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()
    
    st.markdown("---")
    st.download_button(
        label="🚀 Download Cleaned Image",
        data=byte_im,
        file_name="rembg_result.png",
        mime="image/png"
    )

else:
    st.info("Please upload an image to get started.")

# --- Footer ---
st.markdown("---")
st.caption("Powered by rembg and Streamlit")
