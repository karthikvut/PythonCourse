from sklearn import datasets, linear_model
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.metrics import accuracy_score
diabetes = datasets.load_diabetes()

diabetes_X = diabetes.data[:,np.newaxis , 2]

diabetes_X_train = diabetes_X[:-35]
diabetes_X_test = diabetes_X[-35:]

diabetes_y_train = diabetes.target[:-35]
diabetes_y_test = diabetes.target[-35:]

regr = linear_model.LinearRegression()

regr.fit(diabetes_X_train, diabetes_y_train)

diabetes_y_pred = regr.predict(diabetes_X_test)

print("Coefficients: \n", regr.coef_)
print("Mean Square Error %.2f",mean_squared_error(diabetes_y_test,diabetes_y_pred))
print("Variance Score: %.2f", r2_score(diabetes_y_test,diabetes_y_pred))
print("Intercept", regr.intercept_)
plt.scatter(diabetes_X_test,diabetes_y_test, color='black')
plt.plot(diabetes_X_test,diabetes_y_pred, color='blue', linewidth=3)

plt.xticks(())
plt.yticks(())

plt.show()

reg = linear_model.Ridge(alpha=0.5)

reg.fit(diabetes_X_train,diabetes_y_train)

diabetes_y_pred_ridge = reg.predict(diabetes_X_test)
print("Mean squared for Ridge %.2f", mean_squared_error(diabetes_y_test,diabetes_y_pred_ridge))
print("Coefficients:", reg.coef_)
print("Intercept:", reg.intercept_)



