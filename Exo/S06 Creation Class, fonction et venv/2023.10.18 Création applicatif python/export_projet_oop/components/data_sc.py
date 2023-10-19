import pandas as pd
import os

def csv_clean(file_path):
    ''' Opening the titanic dataset, cleaning it up, and preprocessing it for fitting
     take the dataset filepath as input,
      output the path of the cleaned filed '''
    #import data in an dataframe
    df = pd.read_csv(file_path)
    #cleaning
    df['Age'] = df['Age'].fillna(df['Age'].mean())
    df = df.drop(['Cabin', 'Name', 'PassengerId','Ticket'], axis=1)
    df = df.dropna(axis=0)
    #encoding
    df= pd.get_dummies(data=df, columns=['Pclass', 'SibSp', 'Parch', 'Sex', 'Embarked'], dtype=int)
    #saving cleaning files
    exit_filepath = os.path.join(os.path.dirname(file_path), 'data_cleaned.csv')
    df.to_csv(exit_filepath, index=False)

    return exit_filepath


