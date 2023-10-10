) Make a Veille about :

    Linear regression
        What, how, when
        sklearn > linear_model > LinearRegression
    Error function and metrics.
        what, how, when
        sklearn > metrics > mean_squared_error | r2_score
    Dilemme biais-variance. wtf ?

2) Playground
Dive

    Create a synthetic dataset to experiment with linear regression
    divide this dataset in a training set and un testing set (see sklearn train_test_split)
    Visualize data.
    train your model to fit a linear regression model
    predict data on your test set.
    Visualize the result
    Compute the RMSE score.

Explore

    Right, that was easy ? Add some distorsion to your data to make the problem harder (like some quadratique distorsion)
    fit and predict again. What do you observe ?
    Try to fit a better model. Be creative.

3) Practical example

    Get back our covid data, on dc and hospitalisation.
    do a linear regression on the dc curcve, plot the result and log an error score.
    Impromve your score by spliting the data into several part. Each part will its one linear model.
    Now, because we are lazy, find where to split optimally the dataset automatically (see sklearn DecisionTreeRegresso)

