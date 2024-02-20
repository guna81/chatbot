import string
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.pipeline import Pipeline
from joblib import dump

from .process_data import process_data


def cleaner(x):
    return [a for a in ("".join([a for a in x if a not in string.punctuation])).lower().split()]

def train_model():
    model = Pipeline([
        ('bow', CountVectorizer(
            analyzer=cleaner,
            # stop_words=stopwords.words('english')
        )),
        ('tfidf', TfidfTransformer()),
        ('classifier', DecisionTreeClassifier()),
    ])


    training_data = process_data()

    model.fit(training_data[0], training_data[1])

    dump(model, 'mymodel/models/chat_model.joblib')