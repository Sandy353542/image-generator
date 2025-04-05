import streamlit as st
import os
from huggingface_hub import InferenceClient


st.title("Image Generation App")

user_prompt = st.text_input("Enter your prompt here:")

api_key = "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"
if user_prompt is not None and st.button("Generate"):

    client = InferenceClient(
        provider="hf-inference",
        api_key=api_key
    )

    # output is a PIL.Image object
    image = client.text_to_image(
        user_prompt,
        model="black-forest-labs/FLUX.1-dev"
    )
    st.image(image)