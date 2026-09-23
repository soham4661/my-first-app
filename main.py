import streamlit as st
import time
from google import genai
from dotenv import load_dotenv

load_dotenv(r"C:\Users\Soham Pawar\OneDrive\Desktop\Train_python\Training_Python_Beginner\Gen_Ai\google_gemini\.env")
client = genai.Client()



st.markdown("# 🛫 **Travel Assistant** `v1.0` ")
st.caption("🚀 Plan trips • 📍 Discover spots • 🧳 Packing checklists")
st.divider()
st.subheader("Plan your trip with ease and convenience")

location = st.text_input("Enter your destination:")
days = st.number_input("Enter the number of days for your trip:", min_value=1, max_value=30)

budget = st.selectbox("Select your budget range:", ["Luxury", "Moderate", "Budgeted"])
travel_type = st.radio("Select your preferred travel type:", ["Family","Solo","friends"])
prompt = """You are a travel planner, user is saying he wants to go to {location} for {days} days, please give answer in bullet points, he is on the budget of {budget} and prefers {travel_type} travel."""

if st.button("Plan the trip"):
    interaction = client.interactions.create(
          model="gemini-3.5-flash-lite",
          input= prompt
      )
    with st.spinner("Wait for it...", show_time=True):
         time.sleep(5)
    st.success("Trip plan generated successfully!")
    st.write(interaction.output_text)
  