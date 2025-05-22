import streamlit as st

st.markdown("""
    <style>
        .stApp {
            background-color: #C7DB9C;
            font-family: 'Segoe UI', sans-serif;
        }
        .main-title {
            text-align: center;
            font-size: 40px;
            color: #2c3e50;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .result {
            background-color: #e0f7fa;
            padding: 15px;
            margin-bottom: 20px;
            border-radius: 10px;
            color: #006064;
            font-size: 18px;
            font-weight: bold;
        }
        .bmi-category {
            background-color: #fce4ec;
            padding: 10px;
            border-radius: 8px;
            color: #880e4f;
            margin-top: 10px;
            font-size: 16px;
        }
        .footer{
            margin-top: 20px;
            font-size: 14px;
            color: black;
            font-style: italic;
        }
        .bold{
            font-weight: bold;
            }
    </style>
""", unsafe_allow_html=True)

st.markdown("<div class='main-title'>💪 BMI Calculator</div>", unsafe_allow_html=True)

st.markdown("<div class='bold'> Enter your height in cm:</div>", unsafe_allow_html=True)
height = st.number_input("", min_value=0.0, max_value=300.0, value=170.0)

# Convert cm to inches and feet
height_in = height / 2.54
feet = int(height_in // 12)
inches = round(height_in % 12)

st.markdown(f"<div class='result'> Your height is approximately: <b>{feet} feet {inches} inches</b></div>", unsafe_allow_html=True)


st.markdown("<div class='bold'> Enter your weight in kg:</div>", unsafe_allow_html=True)
weight = st.number_input("", min_value=0.0, max_value=300.0, value=70.0)


bmi = weight / ((height / 100) ** 2)
st.markdown(f"<div class='result'> Your BMI is: <b>{bmi:.2f}</b></div>", unsafe_allow_html=True)

st.markdown("""
<div class='bmi-category'>
    📊 <b>BMI Categories:</b><br>
    - Underweight: Less than 18.5<br>
    - Normal weight: 18.5–24.9<br>
    - Overweight: 25–29.9<br>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='footer'>This app calculates your BMI based on your height and weight. For medical advice, consult a professional.</div>", unsafe_allow_html=True)
