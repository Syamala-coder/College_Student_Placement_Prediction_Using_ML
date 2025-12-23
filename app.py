import streamlit as st
import pickle
import numpy as np
import pandas as pd
import base64

with open("dt.pkl","rb") as f:
    best_dt=pickle.load(f)



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

# CALL background function
set_bg_image(r"Image.jpeg")











st.title("Student Placement Prediction")

IQ=int(st.number_input("IQ",value=0))
Prev_Sem_Result=int(st.number_input("Prev_Sem_Result",value=0.00))
CGPA=int(st.number_input("CGPA",value=0.00))
Academic_Performance=int(st.number_input("Academic_Performance",value=0))
Internship_Experience=st.selectbox("Internship_Experience",["Yes","No"])
Extra_Curricular_Score=int(st.number_input("Extra_Curricular_Score",value=0))
Communication_Skills=int(st.number_input("Communication_Skills",value=0))
Projects_Completed=int(st.number_input("Projects_Completed",value=0))

if st.button("Placed or not"):
    input_df=pd.DataFrame([{
        "IQ":IQ,
        "Prev_Sem_Result":Prev_Sem_Result,
        "CGPA":CGPA,
        "Academic_Performance":Academic_Performance,
        "Internship_Experience":Internship_Experience,
        "Extra_Curricular_Score":Extra_Curricular_Score,
        "Communication_Skills":Communication_Skills,
        "Projects_Completed":Projects_Completed


    }])

    result =best_dt.predict(input_df)[0]


    st.markdown(
            "<h2 style='color:#006400; background:#90EE90; padding:10px; border-radius:10px;'>"
            "Prediction: Placed</h2>",
        unsafe_allow_html=True
        )