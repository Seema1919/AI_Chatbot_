import streamlit as st
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()
groq_api_key = os.getenv("GROQ_API_KEY")


if not groq_api_key:
    st.error("GROQ_API_KEY.env")
    st.stop()

def main():
    st.title("Groq Chatbot")

    groq_chat = ChatGroq(
        groq_api_key=groq_api_key,

    )
    user_question = st.text_area("Ask a question:")

    if st.button("Send"):
        if user_question.strip():
            response = groq_chat.invoke(user_question)
            st.write(f"**You:** {user_question}")
            st.write(f"**Groq:** {response}")
        else:
            st.warning("Please enter a valid question.")

if __name__ == "__main__":
