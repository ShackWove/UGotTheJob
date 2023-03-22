from Data import Data
from Model import Model
from joblib import load
import random

model = Model()
i = 0
while i < 10:
    i += 1
    ssc_percentage = random.uniform(0, 100)
    ssc_board = random.randint(0, 1)
    hsc_percentage = random.uniform(0, 100)#float(input("hsc_percentage: "))
    hsc_board = random.randint(0, 1)
    hsc_subject = random.randint(0, 2) #float(input("hsc_subject: "))
    degree_percentage = random.uniform(0, 100) #float(input("degree_percentage: "))
    undergrad_degree = random.randint(0, 2)#float(input("undergrad_degree: "))
    work_experience = random.randint(0, 1)#float(input("work_experience: "))
    #emp_test_percentage = float(input("emp_test_percentage: "))
    specialisation = random.randint(0, 1) #float(input("specialisation: "))
    print(ssc_percentage)
    print(ssc_board)
    print(hsc_percentage)
    print(hsc_board)
    print(hsc_subject)
    print(degree_percentage)
    print(undergrad_degree)
    print(work_experience)
    #print(emp_test_percentage)
    print(specialisation)
    data = Data().prepare_data(ssc_percentage, ssc_board, hsc_percentage, hsc_board, hsc_subject, degree_percentage, undergrad_degree, work_experience, specialisation)
    print(model.prediction_model(data))
    print("\n\n")