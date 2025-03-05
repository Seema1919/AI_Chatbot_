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
    st.title("Gym Trainer & Nutritionist Chatbot")

    st.write("This chatbot provides fitness and nutrition advice to help users achieve their health goals.")

    groq_chat = ChatGroq(
        groq_api_key=groq_api_key,
    )

    user_question = st.text_area("Ask a fitness or nutrition question:")

    if st.button("Send"):
        if user_question.strip():
            gym_prompt = f"You are a certified gym trainer and nutritionist. Provide expert advice on workouts, diets, and healthy lifestyle habits. Question: {user_question}"
            response = groq_chat.invoke(gym_prompt)
            message = response.content
            st.write(f"**You:** {user_question}")
            st.write(f"**Trainer & Nutritionist:** {message}")
        else:
            st.warning("Please enter a valid fitness or nutrition question.")

    st.subheader("Get a Personalized Diet Plan")
    if st.button("Easy Plan"):
        st.write(
            "### Easy Diet Plan\n- Breakfast: Oatmeal with fruits and nuts\n- Lunch: Grilled chicken with rice and veggies\n- Snack: Greek yogurt with honey\n- Dinner: Baked fish with steamed vegetables")
    if st.button("Medium Plan"):
        st.write(
            "### Medium Diet Plan\n- Breakfast: Scrambled eggs with whole-grain toast\n- Lunch: Quinoa salad with grilled salmon\n- Snack: Protein shake with banana\n- Dinner: Stir-fried tofu with brown rice and greens")
    if st.button("Hard Plan"):
        st.write(
            "### Hard Diet Plan\n- Breakfast: Egg whites with spinach and avocado\n- Lunch: Grilled chicken with sweet potatoes and steamed broccoli\n- Snack: Handful of almonds and a protein shake\n- Dinner: Lean beef with quinoa and asparagus")


if __name__ == "__main__":
    main()
