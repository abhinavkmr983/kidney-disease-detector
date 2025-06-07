# -*- coding: utf-8 -*-
"""
Created on Sat Jun  7 03:21:27 2025
@author: abhin
"""

import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load('kidney_disease_model.joblib')

st.set_page_config(page_title="Kidney Disease Detection", layout="centered")
st.title("🩺 AI-Powered Kidney Disease Detection App")

st.markdown("Fill the patient information below to predict the presence of **Chronic Kidney Disease (CKD)**.")

# Create input fields
age = st.number_input("Age", min_value=0, max_value=120, value=30)
bp = st.number_input("Blood Pressure (mm/Hg)", min_value=50, max_value=200, value=80)
sg = st.selectbox("Specific Gravity", options=[1.005, 1.010, 1.015, 1.020, 1.025])
al = st.slider("Albumin", 0, 5, 1)
su = st.slider("Sugar", 0, 5, 0)
rbc = st.selectbox("Red Blood Cells", ["normal", "abnormal"])
pc = st.selectbox("Pus Cell", ["normal", "abnormal"])
pcc = st.selectbox("Pus Cell Clumps", ["present", "notpresent"])
ba = st.selectbox("Bacteria", ["present", "notpresent"])
bgr = st.number_input("Blood Glucose Random (mg/dl)", 0, 500, 100)
bu = st.number_input("Blood Urea (mg/dl)", 0.0, 200.0, 40.0)
sc = st.number_input("Serum Creatinine (mg/dl)", 0.0, 20.0, 1.2)
sod = st.number_input("Sodium (mEq/L)", 100.0, 160.0, 140.0)
pot = st.number_input("Potassium (mEq/L)", 2.0, 10.0, 4.5)
hemo = st.number_input("Hemoglobin (gms)", 3.0, 20.0, 13.0)
pcv = st.number_input("Packed Cell Volume", 15, 60, 40)
wc = st.number_input("White Blood Cell Count", 3000, 20000, 8000)
rc = st.number_input("Red Blood Cell Count", 2.0, 7.0, 5.0)
htn = st.selectbox("Hypertension", ["yes", "no"])
dm = st.selectbox("Diabetes Mellitus", ["yes", "no"])
cad = st.selectbox("Coronary Artery Disease", ["yes", "no"])
appet = st.selectbox("Appetite", ["good", "poor"])
pe = st.selectbox("Pedal Edema", ["yes", "no"])
ane = st.selectbox("Anemia", ["yes", "no"])

# Encode categorical features
rbc = 1 if rbc == "normal" else 0
pc = 1 if pc == "normal" else 0
pcc = 1 if pcc == "present" else 0
ba = 1 if ba == "present" else 0
htn = 1 if htn == "yes" else 0
dm = 1 if dm == "yes" else 0
cad = 1 if cad == "yes" else 0
appet = 1 if appet == "good" else 0
pe = 1 if pe == "yes" else 0
ane = 1 if ane == "yes" else 0

# Prepare input array
input_data = np.array([[age, bp, sg, al, su, rbc, pc, pcc, ba,
                        bgr, bu, sc, sod, pot, hemo, pcv, wc, rc,
                        htn, dm, cad, appet, pe, ane]])

# Predict button
if st.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("❌ Chronic Kidney Disease Detected")
    else:
        st.success("✅ No Kidney Disease Detected")

