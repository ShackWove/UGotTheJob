import sys
sys.path.insert(0, "../../source_code")
import threading
from tkinter import *
from tkinter import ttk
import customtkinter
import os
from PIL import Image
#from business_logic.Model import Model

class top_research (customtkinter.CTkToplevel):
    def __init__ (self,  hsc_percentage, hsc_subject, voto_laurea, laurea_subject, work_exp, emp_test, specialization, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.hsc_percentage = hsc_percentage
        self.hsc_subject = hsc_subject
        self.voto_laurea = voto_laurea
        self.laurea_subject = laurea_subject
        self.work_exp = work_exp
        self.emp_test = emp_test
        self.specialization = specialization
        self.toplevel = None