from Data import Data
from Model import Model
from joblib import load
import random

model = Model()
i = 0
while i < 10:
    i += 1
    ssc_percentage = random.uniform(50, 100)
    ssc_board = random.randint(0, 1) # Others = 1, Central = 0
    hsc_percentage = random.uniform(50, 100)
    hsc_board = random.randint(0, 1) #Others = 1, Central = 0
    hsc_subject = random.randint(0, 2)  #Commerce = 1, Science = 2, Arts = 0
    degree_percentage = random.uniform(50, 100)
    undergrad_degree = random.randint(0, 2)  #Sci&Tech = 2, Comm&Mgmt = 0, Others = 1
    work_experience = random.randint(0, 1)  #No = 0, Yes = 1
    specialisation = random.randint(0, 1)  # Mkt&HR = 1, Mkt&Fin = 0 
    print(ssc_percentage)
    print(ssc_board)
    print(hsc_percentage)
    print(hsc_board)
    print(hsc_subject)
    print(degree_percentage)
    print(undergrad_degree)
    print(work_experience)
    print(specialisation)
    data = Data.prepare_data(ssc_percentage, ssc_board, hsc_percentage, hsc_board, hsc_subject, degree_percentage, undergrad_degree, work_experience, specialisation)
    print(model.prediction_model(data))
    print("\n\n")