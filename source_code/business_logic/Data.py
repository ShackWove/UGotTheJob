import random
import pandas as pd

class Data:

    def prepare_data(self, hsc_percentage = 37, hsc_subject = "Science", degree_percentage = 50 , undergrad_degree ="Sci&Tech", work_experience="No",  specialisation = "Mkt&HR"):
        degree_percentage_converted = degree_percentage - 10
        return pd.DataFrame({"hsc_percentage": [hsc_percentage], "hsc_subject": [hsc_subject], 
                                                "degree_percentage": [degree_percentage_converted], "undergrad_degree" : [undergrad_degree], 
                                                "work_experience": [work_experience], 
                                                "specialisation": [specialisation]})



