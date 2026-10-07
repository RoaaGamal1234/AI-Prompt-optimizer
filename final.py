import streamlit as st
import requests

# API URL
URL = "https://unthawed-rambling-reuse.ngrok-free.dev/generate"

headers = {
    "Authorization": "Bearer secret123"
}

# Function to send prompt to API
def get_optimized_prompt(user_prompt):
    payload = {
        "prompt": user_prompt
    }

    res = requests.post(
        URL,
        headers=headers,
        json=payload
    )

    return res.json()["response"]


# ---------------- GUI ----------------

st.title("🤖 AI Prompt Optimizer")

st.write("Enter your prompt and let the AI optimize it.")

# User input
user_prompt = st.text_area(
    "Enter your prompt:",
    placeholder="Write your prompt here..."
)

# Button
if st.button("Optimize Prompt"):

    if user_prompt.strip() == "":
        st.warning("Please enter a prompt.")

    else:
        with st.spinner("Optimizing your prompt..."):

            try:
                answer = get_optimized_prompt(user_prompt)

                st.subheader("Optimized Prompt")
                st.text_area(
                    "AI Response:",
                    value=answer,
                    height=200
                )

            except Exception as e:
                st.error(f"Error: {e}")