from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from joblib import load

class Model:
    def __init__(self):
        self.dt : RandomForestClassifier() = load ("../../job_prevision.joblib")
    
    def prediction_model(self, dataframe: pd):
        prediction = self.dt.predict(dataframe)
        if prediction[0] == "Placed" :
            prob = self.dt.predict_proba(dataframe)[:, 1]
            return "Placed at " + str(prob[0] * 100) +"%"
        else:
            prob = self.dt.predict_proba(dataframe)[:, 0]
            return "Not Placed at " + str(prob[0] * 100)  + "%"