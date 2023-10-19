import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import  MinMaxScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def create_model(clean_file_path, save_files_path):
    '''create a model pipeline, 
    takes the prior cleaned file path and the output files path as input,
    save the fitted scaler and model in save_file_path'''
    #read the clean csv
    df = pd.read_csv(clean_file_path)
    # scaling data
    colonnes = df.columns
    scaler = MinMaxScaler()
    df[colonnes] = scaler.fit_transform(df)
    #saving my scaler
    scaler_filename = 'MinMaxScaler.sav'
    scaler_filepath = os.path.join(os.path.dirname(save_files_path), 
                                   scaler_filename)
    joblib.dump(scaler, 
                scaler_filepath)

    # train _ test splitting
    x_train, x_test, y_train, y_test = train_test_split(df.drop(['Survived'], axis=1), 
                                                        df['Survived'], 
                                                        random_state=42)
    
    #fitting a logistic regression on the train set
    model = LogisticRegression()
    model.fit(x_train, y_train)
    #Testing the model to display accuracy, just for eyes candy
    y_hat = model.predict(x_test)
    accuracy = accuracy_score(y_test, y_hat)
    print(f'Accuracu of the Logistic Regression Model : {accuracy.round(3)}')
    #saving my fitted model
    model_filename = 'Logistic_Regression_model.sav'
    model_filepath = os.path.join(os.path.dirname(save_files_path), model_filename)
    joblib.dump(model, model_filepath)
    print(f'Scaler and model saved in {os.path.dirname(save_files_path)}')

