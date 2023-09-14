from sklearn.datasets import load_digits
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import GaussianNB

digits = load_digits()

data = digits.data
targets = digits.target

model = GaussianNB()

score = cross_val_score(model, data, targets)

print(score)
print(score.mean())
