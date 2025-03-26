# AI-Powered Travel Planner

## 📌 Project Overview
The **AI-Powered Travel Planner** is a web-based application built using **Streamlit** and **Google's Gemini AI**. This application generates personalized travel itineraries based on user preferences, such as destination, duration, budget, travel purpose, and interests.

## 🚀 Features
- Users input their **Google Gemini API key** at the beginning.
- Collects user preferences (**budget, duration, interests, etc.**).
- Generates a **personalized travel itinerary** using **Google Gemini AI**.
- Provides **top attractions, dining recommendations, and estimated costs**.
- Simple **web-based UI using Streamlit**.

## 🛠️ Technologies Used
- **Python** (Core programming language)
- **Streamlit** (Web UI framework)
- **Google Gemini AI** (AI-based itinerary generation)
- **Google AI Studio API** (Access to Gemini models)

---

## 💻 Installation & Setup
### 1️⃣ Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install streamlit google-generativeai
```

### 2️⃣ Get Your Google API Key
You need an API key from Google AI Studio to use the Gemini model.
#### How to Get Your API Key from Google AI Studio:
```text
1. Go to Google AI Studio: https://aistudio.google.com/
2. Sign in with your Google account.
3. Click on "API Access" (Top-right corner).
4. Click "Generate API Key".
5. Copy the generated API Key.
```

### 3️⃣ Run the Application
Save the **`AI-Powered Travel Planner.py`** file and run:
```bash
streamlit AI-Powered Travel Planner .py
```

### 4️⃣ Enter Your Google API Key
```text
- When prompted, enter your Google Gemini API Key.
- If you do not provide an API key, the application will stop execution.
```

---

## 🎯 How It Works
```text
1️⃣ User enters travel details: 
   - Starting location, destination, duration, budget, and preferences.
2️⃣ AI generates an itinerary: 
   - Based on user input, Google Gemini AI suggests a structured day-by-day travel plan.
3️⃣ User receives a detailed itinerary: 
   - Includes attractions, dining spots, and estimated costs per day.
```

---

## 📌 Example Output
### User Input:
```text
{
  "destination": "Paris",
  "duration": 3,
  "budget": "Moderate",
  "purpose": "Leisure",
  "interests": ["History", "Food"]
}
```

### Generated Itinerary Output:
```text
Day 1:
- Morning: Visit the Eiffel Tower
- Afternoon: Lunch at Café de Flore
- Evening: Seine River Cruise

Day 2:
- Morning: Louvre Museum Tour
- Afternoon: Explore Montmartre
- Evening: Hidden Wine Bar Experience

Day 3:
- Morning: Palace of Versailles
- Afternoon: Walk through Jardin du Luxembourg
- Evening: Dinner at a classic French bistro
```

---

## 📌 Hosting the Application
To deploy the app online, use **Streamlit Cloud**:
```text
1. Upload `travel_planner.py` to GitHub.
2. Go to Streamlit Cloud: https://streamlit.io/cloud
3. Connect your GitHub repository.
4. Deploy your app for public access.
```

---

## 📌 Troubleshooting
### ❌ API Key Not Found Error
Ensure you:
```text
- Generated the API key from Google AI Studio.
- Entered the correct API key in the Streamlit app.
```

### ❌ Model Not Found (404 Error)
Update the model name in `travel_planner.py`. Try:
```python
model = genai.GenerativeModel("models/gemini-1.5-pro")
```

---

## 📌 Conclusion
This AI-powered travel planner helps users create detailed travel plans **instantly** using Google Gemini AI. With an easy-to-use interface and AI-generated suggestions, planning a trip has never been easier! 🎉

---

🔹 **Developed by:** Dogga Pavan Sekhar
🔹 **Project Repository:** [https://github.com/dpavansekhar/AI-Powered-Travel-Planner]
🔹 **Demo:** [Streamlit Hosted Link]  
