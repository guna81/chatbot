import numpy as np
import pandas as pd
from dataset.data import intents

def process_data():
    df = pd.read_csv('dataset/dialogs.txt', sep='\t')
    df.columns = ["Questions", "Answers"]

    return (df['Questions'], df['Answers'])


# def process_data():
#     X_train = []
#     y_train = []

#     for intent, examples in intents.items():
#         X_train.extend(examples)
#         y_train.extend([intent] * len(examples))

#     return (X_train, y_train)