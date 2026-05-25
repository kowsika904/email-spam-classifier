from flask import Flask, render_template, request
import pickle
import nltk

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

app = Flask(__name__)

# LOAD MODEL + VECTORIZER
model = pickle.load(open('model.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

ps = PorterStemmer()

# DOWNLOAD NLTK DATA
nltk.download('punkt')
nltk.download('stopwords')


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



# HOME PAGE
@app.route('/')
def home():

    return render_template(
        'index.html',
        result=None,
        desc=None,
        status=None,
        accuracies={
            "Naive Bayes": "96%",
            "Logistic Regression": "97%",
            "SVM": "98%"
        }
    )



# PREDICTION
@app.route('/predict', methods=['POST'])
def predict():

    message = request.form['message']

    transformed_message = transform_text(message)

    vector_input = vectorizer.transform([transformed_message])

    prediction = model.predict(vector_input)[0]


    # RESULT

    if prediction == 1:

        result = "⚠ Spam Mail"

        desc = "This message is identified as spam or unwanted content."

        status = "spam"

    else:

        result = "✔ Ham Mail"

        desc = "This message is identified as legitimate and non-spam content."

        status = "safe"



    return render_template(

        'index.html',

        result=result,

        desc=desc,

        status=status,

        accuracies={
            "Naive Bayes": "96%",
            "Logistic Regression": "97%",
            "SVM": "98%"
        }
    )



# RUN APP
if __name__ == '__main__':

    app.run(debug=True)