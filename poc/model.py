import pandas as pd
import numpy as np
import phe as paillier
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score


class LinearModel:
    dataset_filename = "diabetes.csv"

    def __init__(self):
        self.df = pd.read_csv(self.dataset_filename)
        self.y = self.df.Diabetes_binary
        self.X = self.df.drop("Diabetes_binary", axis=1)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=0.2, random_state=0
        )
        pass

    def getResults(self):
        reg = LinearRegression().fit(self.X_train, self.y_train)
        y_pred = reg.predict(self.X_test)
        RMSE = pow(mean_squared_error(y_pred, self.y_test), 0.5)
        R = r2_score(y_pred, self.y_test)
        return reg, y_pred, RMSE, R

    def getCoef(self):
        return self.getResults()[0].coef_
    
    def getTestData(self):
        return self.X_test, self.y_train


def main():
    lin = LinearModel()
    cof = lin.getCoef()
    print("Linear Regression model trained on `{}` dataset\n".format(lin.dataset_filename))
    print("The trained weights are: \n", cof)


if __name__ == "__main__":
    main()
