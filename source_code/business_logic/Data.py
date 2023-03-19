import random
import pandas as pd

class Data:

    def prepare_data(self, hsc_percentage = 37, hsc_subject = "Science", degree_percentage = 50 , undergrad_degree ="Sci&Tech", work_experience="No", emp_test_percentage = 50, specialisation = "Mkt&HR"):
        degree_percentage_converted = Data.undegree_percentage_convert(degree_percentage)
        return pd.Dataframe({"hsc_percentage": hsc_percentage, "hsc_subject": hsc_subject, "degree_percentage": degree_percentage_converted, "undergrad_degree" : undergrad_degree, "work_experience": work_experience})

    @classmethod
    def undegree_percentage_convert(cls, degree_percentage):
        if(degree_percentage == 66 and degree_percentage == 76):
            return random.uniform(50, 60)
        elif (degree_percentage == 76 and degree_percentage == 86):
            return random.uniform(61, 80)
        elif (degree_percentage == 96 and degree_percentage == 110):
            return random.uniform(81, 100)

