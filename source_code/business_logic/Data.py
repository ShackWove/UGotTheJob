import random
import pandas as pd

class Data:

    def prepare_data(self,ssc_percentage=50, ssc_board= 0,  hsc_percentage = 40, hsc_board=0,  hsc_subject = 0, degree_percentage = 50 , undergrad_degree =0, work_experience=0,  specialisation =0):
        return pd.DataFrame({"ssc_percentage": [ssc_percentage], "ssc_board": [ssc_board],"hsc_percentage": [hsc_percentage], "hsc_board" : hsc_board,"hsc_subject": [hsc_subject], 
                                                "degree_percentage": [degree_percentage], "undergrad_degree" : [undergrad_degree], 
                                                "work_experience": [work_experience], 
                                                "specialisation": [specialisation]})



