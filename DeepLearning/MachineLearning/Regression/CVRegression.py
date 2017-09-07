from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

lr = linear_model.Ridge(alpha=0.9)
boston = datasets.load_boston()
y = boston.target

predicted = cross_val_predict(lr,boston.data, y, cv=30)

print("Score: %.2f",r2_score(y,predicted))
fig, ax = plt.subplots()

ax.scatter(y, predicted, edgecolors=(0,0,0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw =4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()

