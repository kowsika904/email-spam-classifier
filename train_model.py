import pandas as pd
import pickle
import string

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import nltk

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC

from sklearn.metrics import accuracy_score

nltk.download('stopwords')

# LOAD DATASET
df = pd.read_csv('spam.csv', encoding='latin-1')

# KEEP REQUIRED COLUMNS
df = df[['v1', 'v2']]

df.columns = ['label', 'message']

# CONVERT LABELS
df['label'] = df['label'].map({
    'ham': 0,
    'spam': 1
})

# STEMMER
ps = PorterStemmer()

# TEXT CLEANING FUNCTION
def transform_text(text):

    text = text.lower()

    words = nltk.word_tokenize(text)

    cleaned = []

    for word in words:

        if word.isalnum():

            if word not in stopwords.words('english'):

                cleaned.append(ps.stem(word))

    return " ".join(cleaned)


# APPLY CLEANING
df['transformed'] = df['message'].apply(transform_text)

# TF-IDF
tfidf = TfidfVectorizer(max_features=3000)

X = tfidf.fit_transform(df['transformed']).toarray()

y = df['label'].values

# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# MODELS
nb = MultinomialNB()
lr = LogisticRegression()
svm = LinearSVC()

# TRAIN
nb.fit(X_train, y_train)
lr.fit(X_train, y_train)
svm.fit(X_train, y_train)

# PREDICT
nb_pred = nb.predict(X_test)
lr_pred = lr.predict(X_test)
svm_pred = svm.predict(X_test)

# ACCURACY
nb_acc = accuracy_score(y_test, nb_pred)
lr_acc = accuracy_score(y_test, lr_pred)
svm_acc = accuracy_score(y_test, svm_pred)

print("\nMODEL ACCURACIES:\n")

print(f"Naive Bayes Accuracy : {round(nb_acc*100,2)}%")
print(f"Logistic Regression Accuracy : {round(lr_acc*100,2)}%")
print(f"SVM Accuracy : {round(svm_acc*100,2)}%")

# BEST MODEL
best_model = svm

# SAVE MODEL
pickle.dump(best_model, open('model.pkl', 'wb'))
pickle.dump(tfidf, open('vectorizer.pkl', 'wb'))

print("\nBest model saved successfully!")