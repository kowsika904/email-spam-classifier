# 📧 Email Detection — AI Powered Spam Classifier

pre-Final Year Mini Project | Machine Learning + NLP Based Web Application

Python · Flask · Scikit-learn · NLTK · HTML · CSS · JavaScript


# 🏗 System Architecture

```text
┌──────────────────────┐
│      User Input      │
│  Enter Email Message │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   Frontend Interface │
│ HTML • CSS • JS UI   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│     Flask Backend    │
│       app.py         │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   NLP Preprocessing  │
│ Tokenization         │
│ Stopword Removal     │
│ Stemming             │
│ TF-IDF Vectorization │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Machine Learning     │
│ Spam Classification  │
│ Naive Bayes          │
│ Logistic Regression  │
│ SVM                  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│ Prediction Result    │
│ Spam Mail / Ham Mail │
└──────────────────────┘
```

---

# 🔄 Workflow

1. User enters email content in the frontend interface

2. Flask backend receives user input

3. NLP preprocessing cleans the email text

4. TF-IDF converts text into vectors

5. Machine Learning model predicts the category

6. Final result is displayed instantly

---

# 📌 Key Highlights

✅ Real-time spam prediction

✅ NLP-based preprocessing pipeline

✅ Multiple ML algorithm comparison

✅ Professional responsive frontend UI

✅ Lightweight and scalable system

✅ Accurate spam classification

---

# 📊 Performance Analysis

The trained machine learning models were evaluated using accuracy metrics.

| Model | Accuracy |
|-------|------------|
| Naive Bayes | 96% |
| Logistic Regression | 97% |
| Support Vector Machine (SVM) | 98% |

The SVM model achieved the highest performance and was selected as the final prediction model.

---

# 🎯 Objectives of the Project

- Detect spam emails automatically
- Reduce unwanted email traffic
- Improve email security
- Classify emails efficiently
- Provide fast real-time predictions
- Build a user-friendly ML application

---

# 🔐 Security Benefits

- Helps identify malicious content
- Reduces phishing risks
- Minimizes spam advertisements
- Improves digital communication safety
- Enhances user productivity
---

# 📌 Project Overview

Email Detection is a Machine Learning-based web application developed to identify whether an email message is Spam or Ham (Legitimate Email).

The system uses Natural Language Processing (NLP) and supervised Machine Learning algorithms to analyze email content and classify messages accurately in real time.

The application provides a modern frontend interface with instant prediction results, professional UI design, and high classification accuracy.

---

# 🚀 Features

✅ Real-time email spam detection

✅ Detects Spam and Ham emails instantly

✅ NLP-based text preprocessing

✅ Modern responsive frontend UI

✅ Machine Learning prediction system

✅ Fast and lightweight application

✅ High accuracy with low false-positive rate

✅ Interactive result display

✅ Professional dashboard-style interface

---

# 🧠 Machine Learning Algorithms Used

| Algorithm | Accuracy |
|------------|------------|
| Naive Bayes | 96% |
| Logistic Regression | 97% |
| Support Vector Machine (SVM) | 98% |

---

# 🛠 Technologies Used

## Frontend
- HTML5
- CSS3
- JavaScript

## Backend
- Python
- Flask

## Machine Learning & NLP
- scikit-learn
- NLTK
- pandas
- NumPy

## Data Visualization
- Matplotlib
- Seaborn

---

# 📂 Project Structure

```bash
EmailSpamClassifier/
│
├── app.py
├── train_model.py
├── spam.csv
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# ⚙️ Working Process

1. User enters email content

2. Email text is preprocessed using NLP

3. Text is converted into numerical vectors

4. Machine Learning model analyzes patterns

5. System predicts:
   - Spam Mail
   - Ham Mail

6. Prediction result is displayed instantly

---

# 📊 Dataset Used

The project uses publicly available datasets:

- UCI SMS Spam Collection Dataset
- Kaggle Spam Email Dataset
- SpamAssassin Dataset

Dataset Link:

https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset

---

# 🔍 NLP Techniques Used

- Tokenization
- Stopword Removal
- Stemming
- TF-IDF Vectorization

---

# 💻 Installation & Setup

## Clone Repository

```bash
git clone https://github.com/kowsika904/email-spam-classifier.git
```

## Open Project

```bash
cd email-spam-classifier
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Train Model

```bash
python train_model.py
```

## Run Application

```bash
python app.py
```

---

# 🌐 Application Preview

The frontend interface allows users to:

- Enter email content
- Analyze email messages
- Detect spam instantly
- View prediction results
- View model accuracy comparison

---

# 📈 Advantages

- Automated spam filtering
- High prediction accuracy
- Real-time email analysis
- Lightweight system
- Easy integration
- User-friendly interface

---

# 🔮 Future Enhancements

- Phishing email detection
- Deep Learning integration
- Cloud deployment
- Multi-language spam detection
- Email attachment scanning

---

# 📚 Learning Outcomes

This project helped in understanding:

- Machine Learning workflows
- NLP preprocessing techniques
- Text classification
- Flask web development
- Frontend-backend integration
- Model training and deployment

---

# 👩‍💻 Developed By

Kowsika S

Artificial Intelligence and Data Science

pre-Final Year Mini Project

---

# 📄 License

This project is developed for educational and academic purposes.
