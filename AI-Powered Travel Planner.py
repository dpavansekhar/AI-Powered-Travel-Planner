pip install google-generativeai
import streamlit as st
import google.generativeai as genai

def generate_itinerary(destination, start_location, budget, duration, purpose, interests, api_key):
    """Generates a personalized travel itinerary using Google Gemini AI."""
    
    genai.configure(api_key=api_key)
    prompt = f"""
    Generate a personalized {duration}-day travel itinerary for a trip from {start_location} to {destination}.
    The budget is {budget}, and the purpose of the trip is {purpose}.
    The traveler is interested in {', '.join(interests)}.
    Include top attractions, dining suggestions, and estimated costs per day.
    """
    
    model = genai.GenerativeModel("models/gemini-1.5-pro")  # Ensure correct model name
    response = model.generate_content(prompt)
    
    return response.text

# Streamlit UI
st.title("✈️ AI-Powered Travel Planner")
st.write("Get a personalized travel itinerary based on your preferences.")

# User API Key Input
api_key = st.text_input("Enter your Google Gemini API Key:", type="password")
if not api_key:
    st.warning("Please enter your API key to proceed.")
    st.stop()

# User Inputs
start_location = st.text_input("Enter your starting location:", placeholder="e.g., New York")
destination = st.text_input("Enter your destination:", placeholder="e.g., Paris")
duration = st.number_input("Number of travel days:", min_value=1, max_value=30, value=5)
budget = st.selectbox("Select your budget:", ["Low", "Moderate", "Luxury"])
purpose = st.selectbox("Purpose of Travel:", ["Leisure", "Adventure", "Business", "Relaxation", "Cultural"])
interests = st.multiselect("Select your interests:", ["Food", "History", "Nature", "Nightlife", "Shopping", "Beaches", "Museums"])

if st.button("Generate Itinerary"):
    if not (start_location and destination and duration and budget and purpose and interests):
        st.warning("Please fill in all fields before generating an itinerary.")
    else:
        with st.spinner("Creating your personalized travel plan..."):
            itinerary = generate_itinerary(destination, start_location, budget, duration, purpose, interests, api_key)
        st.success("Here is your personalized itinerary:")
        st.write(itinerary)

# Run the app using: streamlit run travel_planner.py
