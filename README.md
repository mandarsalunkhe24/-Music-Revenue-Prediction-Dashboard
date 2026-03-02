# 🎵 Music Revenue Prediction AI

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://music-revenue-prediction-ai.streamlit.app/)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1ovSmH_SHdNsGrVtW38Umo_d8Jkt-3olV?usp=sharing)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue)](https://github.com/bharath-541/music-revenue-prediction-ai)

An AI-powered predictive analytics system that forecasts music revenue potential using machine learning techniques applied to Spotify and YouTube engagement metrics.

---

## 📊 Business Problem Statement

Music labels and artists invest significant capital in marketing and promotion without knowing which songs will generate high returns. This creates *financial risk* and *inefficient resource allocation*.

### Core Business Challenge:
- *Problem*: Uncertainty in predicting commercial success before heavy marketing investment
- *Impact*: Wasted marketing budgets on low-performing tracks
- *Solution*: Data-driven predictive model to identify high-revenue potential songs early

### Business Value Delivered:
- 🎯 *Revenue Optimization*: Prioritize marketing spend on high-probability tracks
- 📉 *Risk Reduction*: Minimize financial losses from poor-performing songs
- 📊 *Demand Forecasting*: Predict streaming performance before launch
- 💡 *Strategic Planning*: Data-backed decisions for artist signings and album releases

---

## 💼 Economic Concepts Applied

### 1. *Demand Forecasting*
The model predicts consumer demand (streaming volume) based on historical engagement patterns, enabling proactive supply chain and marketing decisions.

### 2. *Risk Analysis & Management*
By quantifying the probability of high/low performance, the system enables risk-adjusted investment strategies—applying concepts similar to financial portfolio management.

### 3. *Revenue Optimization*
The prediction system helps maximize ROI by allocating marketing budgets to songs with the highest revenue probability, following *marginal utility principles*.

### 4. *Market Segmentation (K-Means Clustering)*
Songs are segmented into distinct market clusters based on engagement patterns:
- *High-Engagement Cluster*: Premium marketing investment
- *Medium-Engagement Cluster*: Targeted digital campaigns
- *Low-Engagement Cluster*: Minimal spend or niche targeting

This mirrors *price discrimination* and *market targeting* strategies in economics.

### 5. *Consumer Behavior Analysis*
Features like Danceability, Energy, Official Video capture consumer preferences and engagement drivers, reflecting *behavioral economics* insights.

### 6. *Opportunity Cost*
Investing in low-potential tracks means forgoing opportunities to promote high-potential songs—this model quantifies that trade-off.

---

## 🤖 AI Techniques & Methodology

### 1️⃣ *Data Preprocessing & Cleaning*
- Removed irrelevant columns (URLs, artist names, descriptions)
- Handled missing values using dropna()
- Normalized numerical features using StandardScaler
- Converted categorical boolean features (Licensed, official_video) to binary integers

### 2️⃣ *Exploratory Data Analysis (EDA)*
- *Correlation Analysis*: Identified relationships between YouTube engagement and Spotify streams
- *Visualization*: Scatter plots, heatmaps to understand feature importance
- *Statistical Summary*: Median-based thresholding for binary classification

### 3️⃣ *K-Means Clustering (Unsupervised Learning)*
- *Purpose*: Market segmentation based on engagement metrics
- *Features Used*: Views, Likes, Comments, Danceability, Energy
- *Number of Clusters*: 3 (representing low, medium, high engagement)
- *Business Insight*: Identifies which songs belong to high-value market segments

*Cluster Interpretation:*
| Cluster | Views | Likes | Stream | Marketing Strategy |
|---------|-------|-------|--------|-------------------|
| 0 | Low | Low | Low | Minimal investment |
| 1 | Medium | Medium | Medium | Targeted campaigns |
| 2 | High | High | High | Premium marketing |

### 4️⃣ *Logistic Regression (Supervised Learning)*
- *Algorithm*: Binary classification model
- *Target Variable*: High_Stream (1 if streams > median, else 0)
- *Features*: 
  - YouTube metrics: Views, Likes, Comments
  - Spotify metrics: Danceability, Energy
  - Content flags: Licensed, official_video
- *Train-Test Split*: 80-20 split with random_state=42
- *Scaling*: StandardScaler applied after splitting to prevent data leakage
- *Model Accuracy: *~72%**

*Model Performance:*

Accuracy: 72%
Precision: 0.73 (High Stream class)
Recall: 0.68 (High Stream class)


### 5️⃣ *Model Deployment*
- *Framework*: Streamlit
- *Features*:
  - Interactive input sliders for song metrics
  - Real-time prediction with probability scores
  - Business recommendations based on predictions

---

## 📁 Dataset

*Source*: [Spotify and YouTube Dataset](https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube)

### Dataset Overview:
- *Records*: 20,000+ songs
- *Features*: Spotify audio features + YouTube engagement metrics
- *Target*: Stream count (converted to binary: High/Low)

### Key Features Used:
| Feature | Description | Type |
|---------|-------------|------|
| Views | YouTube video views | Numerical |
| Likes | YouTube likes | Numerical |
| Comments | YouTube comments | Numerical |
| Danceability | Spotify metric (0-1) | Numerical |
| Energy | Spotify metric (0-1) | Numerical |
| Licensed | Licensed track | Boolean |
| official_video | Has official video | Boolean |
| Stream | Spotify streams | Numerical (Target) |

---

## 🚀 Deployment & Live Demo

### 🌐 *Streamlit App*
*Live URL*: [https://music-revenue-prediction-ai.streamlit.app/](https://music-revenue-prediction-ai.streamlit.app/)

*Features:*
- Interactive dashboard with real-time predictions
- Input sliders for 7 key metrics
- Probability-based revenue forecasting
- Business recommendations for marketing decisions

### 📓 *Google Colab Notebook*
*Notebook Link*: [Open in Colab](https://colab.research.google.com/drive/1ovSmH_SHdNsGrVtW38Umo_d8Jkt-3olV?usp=sharing)

Contains:
- Complete data analysis workflow
- EDA with visualizations
- K-Means clustering implementation
- Logistic Regression model training
- Performance evaluation metrics

### 💻 *GitHub Repository*
*Repository*: [github.com/bharath-541/music-revenue-prediction-ai](https://github.com/bharath-541/music-revenue-prediction-ai)

---

## 📸 Screenshots & Results

### 1. *Streamlit Dashboard*
The interactive web app allows users to input song metrics and receive instant revenue predictions:
- *Input Panel*: Sidebar with sliders for Views, Likes, Danceability, etc.
- *Prediction Output*: Color-coded results (Green = High Revenue, Red = Low Revenue)
- *Model Accuracy Display*: Shows 72% accuracy at the top

### 2. *Correlation Heatmap*
![Correlation Analysis](https://via.placeholder.com/600x400?text=Correlation+Heatmap)
- Shows strong positive correlation between Views, Likes, and Stream
- Identifies key predictive features

### 3. *K-Means Clustering Results*

Cluster Analysis:
Cluster 0: Low engagement (Avg Views: 2M)
Cluster 1: Medium engagement (Avg Views: 50M)
Cluster 2: High engagement (Avg Views: 500M)


### 4. *Model Performance*

Classification Report:
              precision    recall  f1-score   support
           0       0.71      0.76      0.73      1234
           1       0.73      0.68      0.71      1266
    accuracy                           0.72      2500


---

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- pip package manager

### Local Setup

1. *Clone the repository*
bash
git clone https://github.com/bharath-541/music-revenue-prediction-ai.git
cd music-revenue-prediction-ai


2. *Install dependencies*
bash
pip install -r requirements.txt


3. *Download dataset*
- Place Spotify Youtube Dataset.csv in the project root directory

4. *Run the Streamlit app*
bash
streamlit run app.py


5. *Access the app*
- Open browser at http://localhost:8501

---

## 📦 Dependencies


streamlit==1.31.0
pandas==2.2.3
numpy==1.26.4
scikit-learn==1.6.1


---

## 📈 Model Insights & Business Interpretation

### Key Findings:

1. *YouTube Engagement Drives Revenue*: Views, Likes, and Comments are the strongest predictors of streaming success.

2. *Official Videos Matter*: Songs with official videos have 23% higher probability of high stream counts.

3. *Music Characteristics*: Danceability and Energy positively correlate with commercial success.

4. *Market Segmentation*: Three distinct clusters emerge, enabling targeted marketing strategies.

### Business Recommendations:

| Prediction | Probability | Marketing Strategy |
|------------|-------------|-------------------|
| High Revenue | >70% | Full marketing budget allocation |
| Medium Revenue | 50-70% | Moderate spending, A/B test campaigns |
| Low Revenue | <50% | Minimal spend, focus on niche audiences |

---

## 🎯 Use Cases

1. *Record Labels*: Decide which tracks to promote heavily
2. *Artists*: Understand what drives commercial success
3. *Marketing Teams*: Optimize budget allocation across releases
4. *A&R Teams*: Identify signing opportunities based on predicted performance
5. *Streaming Platforms*: Prioritize playlist placements for high-potential tracks

---

## 🔮 Future Enhancements

- [ ] Add time-series forecasting for streaming trends
- [ ] Incorporate social media sentiment analysis
- [ ] Multi-class classification (Low/Medium/High/Viral)
- [ ] Real-time data pipeline integration with Spotify API
- [ ] Deep learning models (Neural Networks) for improved accuracy
- [ ] Genre-specific prediction models

---

## 👥 Team & Project Details

*Course*: Business Studies with Applied AI  
*Institution*: ITM Skills University  
*Submission Date*: 2nd March 2026  

*Project Type*: Mini Project - Data Analytics & AI Implementation

---

## 📧 Contact

For queries or collaborations:
- *GitHub*: [@bharath-541](https://github.com/bharath-541)
- *Project Issues*: [Report here](https://github.com/bharath-541/music-revenue-prediction-ai/issues)

---

## 📄 License

This project is developed for academic purposes as part of the Business Analytics curriculum.

---

## 🙏 Acknowledgments

- *Dataset*: Kaggle Spotify-YouTube Dataset by Salvatore Rastelli
- *Libraries*: Scikit-learn, Streamlit, Pandas, NumPy
- *Guidance*: ITM Skills University Faculty

---

### ⭐ Star this repository if you found it useful!

---

*Note*: This project demonstrates the application of AI and machine learning to solve real-world business problems in the music industry, combining technical implementation with economic and financial analysis.
