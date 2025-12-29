import streamlit as st
import pickle
import pandas as pd
import base64

# --------------------------------
# Load trained PIPELINE model
# --------------------------------
with open("dt.pkl", "rb") as f:
    model = pickle.load(f)

# --------------------------------
# Background Image Function
# --------------------------------
def set_bg_image(img_path):
    with open(img_path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background
set_bg_image("Image.jpeg")

# --------------------------------
# App Title
# --------------------------------
st.title("🎓 Student Placement Prediction")

st.write("Enter student details below:")

# --------------------------------
# User Inputs (KEEP RAW VALUES)
# --------------------------------
IQ = st.number_input("IQ", min_value=0, max_value=100, value=70)

Prev_Sem_Result = st.number_input(
    "Previous Semester Result (%)",
    min_value=0.0,
    max_value=10.0,
    value=7.0
)

CGPA = st.number_input(
    "CGPA",
    min_value=0.0,
    max_value=10.0,
    value=7.0
)

Academic_Performance = st.number_input(
    "Academic Performance",
    min_value=1,
    max_value=10,
    value=7
)

Internship_Experience = st.selectbox(
    "Internship Experience",
    ["Yes", "No"]
)

Extra_Curricular_Score = st.number_input(
    "Extra Curricular Score",
    min_value=0,
    max_value=10,
    value=5
)

Communication_Skills = st.number_input(
    "Communication Skills",
    min_value=1,
    max_value=10,
    value=6
)

Projects_Completed = st.number_input(
    "Projects Completed",
    min_value=0,
    max_value=10,
    value=4
)

# --------------------------------
# Prediction Button
# --------------------------------
if st.button("🔮 Predict Placement"):

    # Convert categorical input to EXACT training format
    input_df = pd.DataFrame([{
        "IQ": IQ,
        "Prev_Sem_Result": Prev_Sem_Result,
        "CGPA": CGPA,
        "Academic_Performance": Academic_Performance,
        "Internship_Experience": Internship_Experience,  # Yes / No
        "Extra_Curricular_Score": Extra_Curricular_Score,
        "Communication_Skills": Communication_Skills,
        "Projects_Completed": Projects_Completed
    }])

    # --------------------------------
    # Model Prediction
    # --------------------------------
    prediction = model.predict(input_df)[0]

    # --------------------------------
    # Output
    # --------------------------------
    if prediction == 1 or prediction == "Yes":
        st.markdown(
            "<h2 style='color:#006400; background:#90EE90; padding:12px; border-radius:10px;'>"
            " Prediction: PLACED</h2>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<h2 style='color:#8B0000; background:#FFCCCC; padding:12px; border-radius:10px;'>"
            " Prediction: NOT PLACED</h2>",
            unsafe_allow_html=True
        )


