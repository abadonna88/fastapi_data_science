from sklearn.datasets import load_digits
from sklearn.model_selection import cross_val_score
from sklearn.svm import SVC

digits = load_digits()

data = digits.data
targets = digits.target

model = SVC()

score = cross_val_score(model, data, targets)

print(score)
print(score.mean())

