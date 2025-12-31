import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
df = pd.read_csv("space_missions_dataset.csv")
st.dataframe(df.head())
df["Scientific_ROI"] = (
    df["Scientific Yield (points)"] /
    df["Mission Cost (billion USD)"]
)
X = df[["Scientific_ROI", "Mission Cost (billion USD)", "Mission Success (%)"]]
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)
st.title("Space Mission Recommendation System")

st.sidebar.header("Mission Preferences")
budget = st.sidebar.slider("Budget (Billion USD)", 10, 500, 100)
risk = st.sidebar.selectbox("Risk Tolerance", ["Low", "Medium", "High"])

st.subheader("Dataset Overview")
def Recommend_Mission(budget, risk):
    filtered = df[
        (df["Mission Cost (billion USD)"] <= budget) &
        (df["Cluster"].isin([0, 1, 2]))  # example cluster filtering
    ]
    if risk == "Low":
        filtered = filtered[filtered["Mission Success (%)"] >= 90]
    elif risk == "Medium":
        filtered = filtered[filtered["Mission Success (%)"] >= 70]
    else:
        filtered = filtered[filtered["Mission Success (%)"] >= 50]
    return filtered.head(3)



if st.button("Recommend_Mission"):
    recommendation = Recommend_Mission(budget, risk)
if recommendation:
    st.write(recommendation)















st.write("App loaded successfully")
st.write("Data-Driven Decision Support for Space Mission Planning")
