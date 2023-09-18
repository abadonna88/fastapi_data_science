import os
from typing import List, Tuple

import joblib
from sklearn.pipeline import Pipeline


model_file = os.path.join(os.path.dirname(__file__), "newsgroups_model.joblib")
loaded_model: Tuple[Pipeline, List[str]] = joblib.load(model_file)
model, targets = loaded_model

p = model.predict(["computer cpu memory ram"])
print(targets[p[0]])

