import streamlit as st
import pandas as pd
import numpy as np
df = pd.read_csv("space_missions_dataset.csv")
st.dataframe(df.head())
X = df[["Scientific_ROI", "Mission Cost (billion USD)", "Mission Success (%)"]]
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)
st.title("Space Mission Recommendation System")

st.sidebar.header("Mission Preferences")
budget = st.sidebar.slider("Budget (Billion USD)", 10, 500, 100)
risk = st.sidebar.selectbox("Risk Tolerance", ["Low", "Medium", "High"])

st.subheader("Dataset Overview")

recommendation = None
if st.button("Recommend Mission"):
    recommendation = recommend_mission(budget, risk)
if recommendation:
    st.write(recommendation)















st.write("App loaded successfully")
st.write("Data-Driven Decision Support for Space Mission Planning")
