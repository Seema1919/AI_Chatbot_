import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    st.error("GROQ_API_KEY not found in environment variables.")
    st.stop()

def main():
    st.title("Medical Chatbot")

    groq_chat = ChatGroq(
        groq_api_key=groq_api_key,
    )

    user_question = st.text_area("Ask a medical question:")

    if st.button("Send"):
        if user_question.strip():
            medical_prompt = f"You are a medical assistant. Provide accurate and helpful medical information. Question: {user_question}"
            response = groq_chat.invoke(medical_prompt)
            message = response.content
            st.write(f"**You:** {user_question}")
            st.write(f"**Medical Assistant:** {message}")
        else:
            st.warning("Please enter a valid medical question.")

if __name__ == "__main__":
    main()
