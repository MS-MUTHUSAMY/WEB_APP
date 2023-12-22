import requests
import json

import streamlit as st

st.title('Image Creator')

API_URL="https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
headers ={"Authorization": "Bearer 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"}

def query(payload):

    response = requests.post(API_URL, headers=headers, json=payload)

    return response.content

prompt = st.text_input("Enter your Prompt")

confirm= st.button('Enter')


if confirm:
    st.spinner("Generating Image...")

    image_bytes=query({
        "inputs": prompt,
    })

    

    #You can access the image with PIL.Image for example
     
    import io
    from PIL import Image
    images = Image.open(io.BytesIO(image_bytes))

    st.image(images,output_format="PNG")

    st.write("Download Image to click on the button")
    down=st.download_button("Download", image_bytes, file_name="image.png")
    if down:
        st.success("Go to download and see the image")