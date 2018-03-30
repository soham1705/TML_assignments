import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
import seaborn as sns
import sklearn
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('Bridges_Data.txt',\
                 names=['Id','SRR', 'FRR', 'SUR', 'ERR', 'RiskScore'])
tf = pd.read_csv('Bridges_Test.txt',\
                 names=['Id','SRR', 'FRR', 'SUR', 'ERR', 'RiskScore'])

X = df[['SRR','FRR','SUR','ERR']]
Y = df['RiskScore']

reg = LinearRegression()

X_ = tf[['SRR','FRR','SUR','ERR']]
Y_ = tf['RiskScore']

for i in range(1,7):
    print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    print "%%%% Multivariate Linear Regression Of Order ",i," %%%%%%%%%"
    print "\n"
    poly = PolynomialFeatures(degree = i)
    X1 = poly.fit_transform(X)
    reg.fit(X1,Y)
    print "Score: ",reg.score(X1,Y)
    X1 = poly.fit_transform(X_)
    Y_p = reg.predict(X1)
    print "Coefficients: ",reg.coef_
    m_sq_err = mean_squared_error(Y_, Y_p)
    print "Mean Squared Error: ", m_sq_err
    print "\n\n\n\n\n"
