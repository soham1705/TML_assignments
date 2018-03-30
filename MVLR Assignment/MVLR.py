import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('Bridges_Data.txt',\
                 names=['Id','SRR', 'FRR', 'SUR', 'ERR', 'RiskScore'])
tf = pd.read_csv('Bridges_Test.txt',\
                 names=['Id','SRR', 'FRR', 'SUR', 'ERR', 'RiskScore'])

#training set

X = df[['SRR','FRR','SUR','ERR']]
Y = df['RiskScore']

reg = LinearRegression()

#test set

X_ = tf[['SRR','FRR','SUR','ERR']]
Y_ = tf['RiskScore']

train_errors=[]
test_errors=[]

for i in range(1,7):
    print "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%"
    print "%%%% Multivariate Linear Regression Of Order ",i," %%%%%%%%%"
    print "\n"

    poly = PolynomialFeatures(degree = i)
    X1 = poly.fit_transform(X)
    reg.fit(X1,Y)
    print "Score: ",reg.score(X1,Y)
    Y_p_t=reg.predict(X1)

    X1 = poly.fit_transform(X_)
    Y_p = reg.predict(X1)

    #print "Coefficients: ",reg.coef_
    train_err = mean_squared_error(Y, Y_p_t)
    test_err = mean_squared_error(Y_, Y_p)
    train_errors.append(train_err)
    test_errors.append(test_err)
    print "Train Error: ",  train_err
    print "Test Error: ", test_err
    print "\n\n\n\n\n"

plt.title('Training errors')
plt.ylabel('MMSE')
plt.xlabel('Degree')
plt.plot(np.arange(1,7),train_errors)
plt.plot(np.arange(1,7),train_errors,'o')
plt.savefig('Training errors.png')
plt.clf()

plt.title('Testing errors')
plt.ylabel('MMSE')
plt.xlabel('Degree')
plt.plot(np.arange(1,7),test_errors)
plt.plot(np.arange(1,7),test_errors,'o')
plt.savefig('Testing errors.png')
