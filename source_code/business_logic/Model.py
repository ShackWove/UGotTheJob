from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from joblib import load

class Model:
    def __init__(self):
        self.rf : RandomForestClassifier() = load ("job_prevision.joblib")
    
    def prediction_model(self, dataframe: pd):
        prediction = self.rf.predict(dataframe)
        if prediction[0] == "Not Placed":
            return "Non sarai preso"
        elif prediction[0] == "Placed":
            return "Sarai preso"
