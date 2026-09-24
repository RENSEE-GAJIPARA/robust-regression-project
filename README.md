<div align="center">

<a href="https://github.com/RENSEE-GAJIPARA">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=800&color=764ABA&center=true&vCenter=true&width=650&lines=Ridge+%7C+Lasso+%7C+Decision+Tree+%7C+Random+Forest+%7C+SVR;Cross-Validated+%7C+Regularized+%7C+Production-Ready;Deployed+as+an+Interactive+Streamlit+App" alt="Typing SVG" />
</a>

<br/>

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Pandas](https://img.shields.io/badge/Pandas-Data-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![Model](https://img.shields.io/badge/Best%20Model-Random%20Forest-blueviolet?style=flat-square)](#-results)


</div>

<br/>

## 📖 Table of Contents

- [Overview](#-overview)
- [Live App & Demo](#-live-app--demo)
- [Dataset](#-dataset)
- [Methodology](#-methodology)
- [Results](#-results)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Theory Document](#-theory-document)
- [Author](#-author)

<br/>

## 🎯 Overview

**Robust Regression Engine** is an end-to-end regression project that predicts **house prices (INR)** from property attributes. It compares regularized linear models, tree-based ensembles, and kernel-based regressors across multiple cross-validation strategies, then ships the winning model inside an interactive **Streamlit** web app.

> 💡 The project doesn't just pick "a model" — it systematically evaluates *why* one model generalizes better than another, backed by a full theory document explaining regularization, bias-variance trade-offs, and cross-validation design.

<br/>

## 🚀 Live App & Demo

<div align="center">

[![Streamlit App](https://img.shields.io/badge/🚀_Launch_Streamlit_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](#)

</div>

| Resource | Link |
|---|---|
| 🌐 **Streamlit Live App** | `<add your deployed Streamlit app URL here — e.g. https://your-app-name.streamlit.app>` |
| 🎥 **Demo Video** | `<add your walkthrough video URL here — e.g. YouTube / Loom link>` |

<br/>

## 📊 Dataset

The model is trained on a synthetic housing dataset of **3,800 property records** with the following attributes:

| Feature | Description |
|---|---|
| `area_sqft` | Built-up area of the property (sq. ft.) |
| `bedrooms` / `bathrooms` | Room counts |
| `location_score` | Composite location desirability score (1–10) |
| `property_age` | Age of the property (years) |
| `distance_city_km` | Distance from city center (km) |
| `near_school` / `near_metro` | Binary proximity flags |
| `crime_rate_index` | Local crime rate index (0 = safest) |
| `house_price_inr` | **Target** — sale price in INR |

<div align="center">
<img src="https://img.shields.io/badge/Rows-3%2C800-informational?style=flat-square"/>
<img src="https://img.shields.io/badge/Features-9-informational?style=flat-square"/>
<img src="https://img.shields.io/badge/Target-house__price__inr-informational?style=flat-square"/>
</div>

<br/>

## 🧪 Methodology

<details open>
<summary><b>1. Exploratory Analysis — Feature Correlation</b></summary>
<br/>

`area_sqft`, `bedrooms`, and `bathrooms` show strong positive correlation with price, while `location_score` correlates positively and `distance_city_km` negatively — matching real-world intuition.

![Feature Correlation Heatmap](Images/1.Feature_Correlation_Heatmap.png)
</details>

<details>
<summary><b>2. Regularization — Ridge vs Lasso</b></summary>
<br/>

Both penalize large coefficients, but Lasso's L1 penalty drives weak features to exactly zero, acting as built-in feature selection.

![Ridge vs Lasso Coefficients](Images/2.Ridge_vs_Lasso_Coefficients.png)
</details>

<details>
<summary><b>3. Cross-Validation Strategy Comparison</b></summary>
<br/>

Evaluated across **K-Fold**, **Stratified K-Fold**, **LOOCV**, and **Time Series Split** to confirm score stability regardless of validation design.

![CV Strategies](Images/3.Mean_R2_across_Cross-Validation_Strategies.png)
</details>

<details>
<summary><b>4. Tree-Based Models — Decision Tree vs Random Forest</b></summary>
<br/>

Random Forest reduces the train/test R² gap seen in a single Decision Tree, indicating stronger generalization through ensembling.

</details><img width="700" height="500" alt="4 Decision Tree vs Random Forest" src="https://github.com/user-attachments/assets/fa9c3325-be93-4469-a1d3-9614e50ee453" />


<br/>

## 🏆 Results

Six regressors were benchmarked on a held-out test set: **Ridge, Lasso, Decision Tree, Random Forest, SVR (Linear), SVR (RBF)**.

<img width="1400" height="500" alt="5 Model Performance Comparison" src="https://github.com/user-attachments/assets/69d2e8bb-83da-4bca-90dc-fb250ab68799" />


<div align="center">

| Model | Test R² | Relative RMSE |
|---|:---:|:---:|
| 🥇 **Random Forest** | **Highest** | **Lowest** |
| 🥈 Lasso | High | Low |
| 🥉 Ridge | High | Low |
| Decision Tree | Moderate | Moderate |
| SVR (Linear) | Poor | High |
| SVR (RBF) | Poor | High |

</div>

**Winner: Random Forest Regressor** — tuned via cross-validated hyperparameter search (`max_depth=8`, `min_samples_split=5`, `n_estimators=200`) — selected for the smallest train/test R² gap alongside the best absolute score, and deployed as the production model in the Streamlit app.

<br/>

## 🛠️ Tech Stack

<div align="center">

![Python](https://img.shields.io/badge/-Python-black?style=flat-square&logo=python)
![NumPy](https://img.shields.io/badge/-NumPy-013243?style=flat-square&logo=numpy)
![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas)
![scikit-learn](https://img.shields.io/badge/-scikit--learn-F7931E?style=flat-square&logo=scikitlearn)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=flat-square)
![Seaborn](https://img.shields.io/badge/-Seaborn-3776AB?style=flat-square)
![Streamlit](https://img.shields.io/badge/-Streamlit-FF4B4B?style=flat-square&logo=streamlit)
![Jupyter](https://img.shields.io/badge/-Jupyter-F37626?style=flat-square&logo=jupyter)

</div>

<br/>

## 📂 Project Structure

```
Robust-Regression-Engine/
├── Notebook
│   └── Robust_Regression_Engine.ipynb     # Full training & evaluation notebook
├── app.py                                 # Streamlit prediction app
├── requirements.txt                       # Python dependencies
├── Dataset
│   └── house_price_dataset.csv            # Source dataset
├── Theory_Document.pdf                    # Concepts write-up (regularization, CV, etc.)
├── Models/
│   └── best_model.pkl                     # Serialized best model bundle
├── Theory_Document.pdf
├── Images/
│   ├── 1_Feature_Correlation_Heatmap.png
│   ├── 2_Ridge_vs_Lasso_Coefficients.png
│   ├── 3_Mean_R2_across_Cross-Validation_Strategies.png
│   ├── 4_Decision_Tree_vs_Random_Forest.png
│   └── 5_Model_Performance_Comparison.png
└── README.md
```

<br/>

## ⚙️ Getting Started

```bash
# 1. Clone the repository
git clone https://github.com/RENSEE-GAJIPARA/Robust-Regression-Engine.git
cd Robust-Regression-Engine

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the Streamlit app
streamlit run app.py
```

<br/>

## 📘 Theory Document

A companion PDF (`Theory_Document.pdf`) covers the concepts behind the project in depth:

- Regularization (why models need it)
- Ridge (L2) vs Lasso (L1) — mechanics and trade-offs
- Cross-validation strategies: K-Fold, Stratified K-Fold, LOOCV, Time Series Split
- Why tree-based models are scale-invariant
- Final business interpretation of results

<br/>

## 👤 Author

<div align="center">

**RENSEE GAJIPARA**

[![GitHub](https://img.shields.io/badge/GitHub-RENSEE--GAJIPARA-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/RENSEE-GAJIPARA)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/rensee-gajipara)

<sub>B.Tech in Artificial Intelligence & Data Science · SCET, Surat</sub>

</div>

<br/>

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:667eea,100:764ba2&height=100&section=footer" width="100%"/>

⭐ **If this project helped you, consider giving it a star!** ⭐

</div>
