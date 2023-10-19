import pandas as pd
from sklearn.preprocessing import  MinMaxScaler

def csv_clean(file_name):
    ''' Opening file_name dataset, cleaning it up, and preprocessing it for fitting '''
    #import data in an dataframe
    df = pd.read_csv(file_name)
    #cleaning
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    df = df.drop(['Cabin', 'Name', 'PassengerId','Ticket'], axis=1)
    df = df.dropna(axis=0)
    #encoding
    df= pd.get_dummies(data=df, columns=['Pclass', 'SibSp', 'Parch', 'Sex', 'Embarked'], dtype=int)
    #scaling
    colonnes = df.columns
    scaler = MinMaxScaler()
    df[colonnes] = scaler.fit_transform(df)
    df.to_csv('data/data_cleaned.csv')


