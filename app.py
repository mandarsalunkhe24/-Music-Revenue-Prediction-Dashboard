import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

@st.cache_data
def load_data():
    df = pd.read_csv("Spotify Youtube Dataset.csv")
    df = df.drop(columns=[
        'Unnamed: 0','Artist','Url_spotify','Track','Album',
        'Album_type','Uri','Url_youtube','Title',
        'Channel','Description'
    ])
    df = df.dropna()
    df['Licensed'] = df['Licensed'].astype(int)
    df['official_video'] = df['official_video'].astype(int)
    df['High_Stream'] = df['Stream'].apply(
        lambda x: 1 if x > df['Stream'].median() else 0
    )
    return df

@st.cache_resource
def train_model(df):
    X = df[['Views','Likes','Comments','Danceability','Energy',
            'Licensed','official_video']]
    y = df['High_Stream']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    model = LogisticRegression(max_iter=3000)
    model.fit(X_train_scaled, y_train)

    accuracy = model.score(X_test_scaled, y_test)

    return model, scaler, accuracy

df = load_data()
model, scaler, accuracy = train_model(df)

# ---------------------------
# Streamlit UI
# ---------------------------
st.title("🎵 Music Revenue Prediction Dashboard")

st.write("Model Accuracy:", round(accuracy * 100, 2), "%")

st.sidebar.header("Enter Song Metrics")

views = st.sidebar.number_input("YouTube Views", value=1000000)
likes = st.sidebar.number_input("YouTube Likes", value=50000)
comments = st.sidebar.number_input("YouTube Comments", value=5000)
danceability = st.sidebar.slider("Danceability", 0.0, 1.0, 0.5)
energy = st.sidebar.slider("Energy", 0.0, 1.0, 0.5)
licensed = st.sidebar.selectbox("Licensed", [0,1])
official_video = st.sidebar.selectbox("Official Video", [0,1])

if st.sidebar.button("Predict Revenue Potential"):

    input_data = np.array([[views, likes, comments,
                            danceability, energy,
                            licensed, official_video]])

    input_scaled = scaler.transform(input_data)

    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1]

    st.subheader("Prediction Result")

    if prediction == 1:
        st.success(f"High Revenue Potential ({round(probability*100,2)}%)")
        st.write("Recommendation: Allocate strong marketing budget.")
    else:
        st.error(f"Low Revenue Potential ({round(probability*100,2)}%)")
        st.write("Recommendation: Moderate or targeted promotion.")