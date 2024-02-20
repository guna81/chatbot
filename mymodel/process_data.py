import numpy as np
import pandas as pd

def process_data():
    df = pd.read_csv('mymodel/datasets/dialogs.txt', sep='\t')
    df.columns = ["Questions", "Answers"]

    df['Questions'] = df['Questions'].apply(lambda x: x.lower())
    df['Answers'] = df['Answers'].apply(lambda x: x.lower())

    X = df['Questions'].values
    Y = df['Answers'].values

    return (X, Y)