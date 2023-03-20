from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from joblib import load

class Model:
    def __init__(self):
        self.dt : RandomForestClassifier() = load ("job_prevision.joblib")
    
    def prediction_model(self, dataframe: pd):
        prediction = self.dt.predict(dataframe)
        prob = self.dt.predict_proba(dataframe)[:, 1]
        return "Non sarai preso al " + str(prob[0] * 100) + "%", "Sarai preso al "+ str(100 - (prob[0] *100)) +"%"
