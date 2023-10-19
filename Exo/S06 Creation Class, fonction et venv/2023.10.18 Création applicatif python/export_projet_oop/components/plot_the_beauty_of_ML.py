import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

def plotting(clean_file_path, model_file_path, save_img_path):
    #openning cleaned data
    df = pd.read_csv(clean_file_path)

    #scaling
    scaler_path = os.path.join(model_file_path, "MinMaxScaler.sav")
    loaded_scaler = joblib.load(scaler_path)
    colonnes = df.columns
    df[colonnes] = loaded_scaler.transform(df)

    # train _ test splitting
    x_train, x_test, y_train, y_test = train_test_split(df.drop(['Survived'], axis=1), 
                                                        df['Survived'], 
                                                        random_state=42)
    
    #loading model
    model_path = os.path.join(model_file_path, "Logistic_Regression_model.sav")
    loaded_model = joblib.load(model_path)
    y_hat = loaded_model.predict(x_test)

    #confusion matrix
    conf_matrix = confusion_matrix(y_test, y_hat)
    conf_matrix = conf_matrix/ conf_matrix.sum(axis = 1) #normalized
    plt.figure(figsize=(8,8))
    fig = sns.heatmap(conf_matrix, cmap='Blues', annot=True)
    fig = fig.get_figure() #changing fig object, allowing us to save it
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    # plt.show(block=False)
    image1_save_path = os.path.join(save_img_path, "Conf_matrix.png")
    fig.savefig(image1_save_path)

    #features importances
    feat_imp = loaded_model.coef_.ravel() #only works for LogReg, might edit latter
    plt.figure(figsize=(8,8))
    fig2 = sns.barplot(y= df.drop(['Survived'], axis=1).columns, x=feat_imp, orient='h')
    fig2 = fig2.get_figure()
    plt.title('Features Importance')
    plt.xlabel('Importances')
    plt.ylabel('Features')
    # plt.show(block=False)
    image2_save_path = os.path.join(save_img_path, "Features_importances.png")
    fig2.savefig(image2_save_path)
    print(f'Plots saved in {save_img_path}')




