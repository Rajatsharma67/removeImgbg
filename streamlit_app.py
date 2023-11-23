import io
import streamlit as st
import rembg
from PIL import Image

def remove_background(image):
    input_image = Image.open(image)
    
    # Convert the PIL image to bytes
    input_image_bytes = io.BytesIO()
    input_image.save(input_image_bytes, format='PNG')
    input_image_bytes = input_image_bytes.getvalue()
    
    # Use rembg library to remove the background
    output_image_bytes = rembg.remove(input_image_bytes)

    # Convert the output bytes to a PIL image
    output_image = Image.open(io.BytesIO(output_image_bytes))
    
    return output_image, output_image_bytes


st.title("Remove Image Background")

uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg","jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Image uploaded successfully.", use_column_width=True)

    if st.button("Remove Background"):
            st.text("Removing background from Image...")

            # Remove background
            result, result_bytes = remove_background(uploaded_file)

            # Display the result
            st.write("Background removed successfully...")
            st.image(result, caption="Result", use_column_width=True, channels="RGBA")

            # Add a download button
            st.download_button(
                label="Download Result Image",
                data=result_bytes,
                file_name="result_image.png",
                key="download_button"
            )
    

# Add a footer
footer = """
<hr>
<p style="text-align:center;">Designed by 🆁🅰🅹🅰🆃 🆂🅷🅰🆁🅼🅰 with ❣️</p>
"""
st.markdown(footer, unsafe_allow_html=True)