import random
import pandas as pd

class Data:

    def prepare_data(self, hsc_percentage = 37, hsc_subject = "Science", degree_percentage = 50 , undergrad_degree ="Sci&Tech", work_experience="No", emp_test_percentage = 50, specialisation = "Mkt&HR"):
        degree_percentage_converted = Data.undegree_percentage_convert(degree_percentage)
        return pd.DataFrame({"hsc_percentage": [hsc_percentage], "hsc_subject": [hsc_subject], 
                                                "degree_percentage": [degree_percentage_converted], "undergrad_degree" : [undergrad_degree], 
                                                "work_experience": [work_experience], "emp_test_percentage": [emp_test_percentage], 
                                                "specialisation": [specialisation]})

    @classmethod
    def undegree_percentage_convert(cls, degree_percentage):
        return degree_percentage - 10

