import streamlit as st
from datetime import datetime

# Set page config for a clean look
st.set_page_config(page_title="Age Calculator", layout="centered")

# Add a custom style for the button and background image
st.markdown(
    """
    <style>
    body {
        background-image: url('https://images.pexels.com/photos/3183197/pexels-photo-3183197.jpeg');
        background-size: cover;
        background-position: center;
        color: white;
    }
    .stButton>button {
        background-color: #ff7f50;
        color: white;
        padding: 15px;
        font-size: 18px;
        font-weight: bold;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        transition: 0.3s ease;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #ff6347;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True
)

# Add title and instructions
st.title("🕒 Age Calculator")
st.write("Enter your Date of Birth to calculate your current age.")

# Get the current year
current_year = datetime.today().year

# Input fields for Day, Month and Dropdown for Year
day = st.number_input("Day of Birth (1-31):", min_value=1, max_value=31, format="%d")
month = st.number_input("Month of Birth (1-12):", min_value=1, max_value=12, format="%d")

# Dropdown for Year (from 2000 to current year)
year = st.selectbox("Year of Birth:", list(range(2000, current_year + 1)))

# Function to calculate age
def calculate_age(dob):
    today = datetime.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

# Button to trigger age calculation
if st.button("Calculate Age"):
    if day and month and year:
        dob = datetime(year, month, day)
        age = calculate_age(dob)
        st.success(f"🎉 Your Age is: {age} years")
    else:
        st.error("Please enter a valid Date of Birth.")