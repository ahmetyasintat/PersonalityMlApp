import streamlit as st
import pickle
import numpy as np


def load_model():
    with open("saved_steps.pkl", "rb") as file:
        data = pickle.load(file)
    return data


data = load_model()

model = data["model"]
age = data["age"]
openness = data["openness"]
neuroticism = data["neuroticism"]
conscientiousness = data["conscientiousness"]
agreeableness = data["agreeableness"]
extraversion = data["extraversion"]
gender = data["gender"]


def show_predict_page():
    st.title("Psychology prediction ml app")

    st.write(""" ### We need some information to predict the your psychology""")


    dict_Personality={
        4: "serious",
        3: "responsible",
        2: "lively",
        1: "extraverted",
        0: "dependable",
    }

    Age = st.slider("How old are you", 0, 80, 1)
    Openness = st.slider("How openness are you?(min=0,max=8)", 0, 8, 1)
    Neuroticism = st.slider("How Neuroticism are you?(min=0,max=9)", 0, 9, 1)
    Conscientiousness = st.slider("How Conscientiousness are you?(min=0,max=9)", 0, 9, 1)
    Agreeableness = st.slider("How agreeableness are you?(min=0,max=8)", 0, 8, 1)
    Extraversion = st.slider("How extraversion are you?(min=0,max=8)", 0, 8, 1)
    Sex = st.slider("what is your sex? (Female=0, Male=1)", 0, 1, 1)

    ok = st.button("Your Personality")
    if ok:
        x = [[Age, Openness, Neuroticism, Conscientiousness, Agreeableness, Extraversion, Sex]]
        personality = model.predict(x)

        st.subheader(f"Your personality is {dict_Personality[model.predict(x)[0]]}")