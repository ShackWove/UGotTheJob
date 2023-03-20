import sys
sys.path.insert(0, "../../source_code")
import threading
from tkinter import *
from tkinter import ttk
import customtkinter
import os
from PIL import Image
from topresearch import top_research


class gui_ai(customtkinter.CTk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")
        self.title("UGotTheJob")
        self.geometry(f"700x800")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=4)
        self.resizable(False, False)
        
        # icon path
        icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), ("../../documentation"))
        
        # icon implementation path
        self.logo_icon = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "job_seeking.png")), size=(100, 100))
        self.search_logo = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "search_light.png")), size=(30, 30))
        
        # main font and dim
        main_font = customtkinter.CTkFont(size=18)
        
        self.main_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.main_frame.grid(sticky="nsew")
        self.main_frame.place(relx=0.5, rely=0.5, anchor="c")
        
        self.main_frame_label = customtkinter.CTkLabel(self.main_frame, text=" UGotTheJob", image=self.logo_icon,
                                                       compound="left",
                                                       font=customtkinter.CTkFont(size=40, weight="bold"))
        self.main_frame_label.grid(row=0, column=0, sticky="nsew")
        
        self.center_frame = customtkinter.CTkFrame(self.main_frame)
        self.center_frame.grid(row=1, column=0, sticky="nsew", padx=40, pady=20)
        
        # voti frame form
        self.voti_entry_frame = customtkinter.CTkFrame(self.center_frame, fg_color="transparent")
        self.voti_entry_frame.grid(row=0, column=0, sticky="nsew", padx=20)
        
        self.label_voti_entry = customtkinter.CTkLabel(self.voti_entry_frame, text="Inserire Voto Liceo: ", font=main_font)
        self.label_voti_entry.grid(row=0, column=0, pady=10, sticky="nsew")
        
        self.voti_entry = customtkinter.CTkEntry(master=self.voti_entry_frame, placeholder_text="da 60 a 110", font=main_font)
        self.voti_entry.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        
        # subject liceo
        self.subject_frame = customtkinter.CTkFrame(master=self.center_frame, fg_color="transparent")
        self.subject_frame.grid(row=1, column=0, sticky="nsew", padx=20)
        
        self.subject_label = customtkinter.CTkLabel(self.subject_frame, text="Inserire una delle materie: ", font=main_font)
        self.subject_label.grid(row=0, column=0, sticky="nsew", pady=10)
        
        self.button_var_subject = customtkinter.StringVar(value="Commerce")
        self.button_subject = customtkinter.CTkSegmentedButton(master=self.subject_frame, values=["Commerce", "Science", "Other"], font=main_font, variable=self.button_var_subject)
        self.button_subject.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
        
        # laurea degree
        self.degree_mark_frame = customtkinter.CTkFrame(master=self.center_frame, fg_color="transparent")
        self.degree_mark_frame.grid(row=2, column=0, sticky="nsew", padx=20)
        
        self.degree_label = customtkinter.CTkLabel(self.degree_mark_frame, text="Inserire voto Laurea: ", font=main_font)
        self.degree_label.grid(row=0, column=0, pady=10, sticky="nsew")
        
        self.degree_entry = customtkinter.CTkEntry(master=self.degree_mark_frame, placeholder_text="da 60 a 110", font=main_font)
        self.degree_entry.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
        
        # laurea soggetto
        self.degree_object_frame = customtkinter.CTkFrame(master=self.center_frame, fg_color="transparent")
        self.degree_object_frame.grid(row=3, column=0, sticky="nsew", padx=20)
        
        self.laurea_subject = customtkinter.CTkLabel(self.degree_object_frame, text="Inserire in cosa si è laureati: ", font=main_font)
        self.laurea_subject.grid(row=0, column=0, sticky="nsew", pady=10)
        
        self.button_var_laurea = customtkinter.StringVar(value="Sci&tech")
        self.button_subject_laurea = customtkinter.CTkSegmentedButton(master=self.degree_object_frame, values=["Sci&tech", "Comm&Mgmt", "Others"], font=main_font, variable=self.button_var_laurea)
        self.button_subject_laurea.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
        
        # work exp
        self.work_object_frame = customtkinter.CTkFrame(master=self.center_frame, fg_color="transparent")
        self.work_object_frame.grid(row=4, column=0, sticky="nsew", padx=20)
        
        self.work_subject = customtkinter.CTkLabel(self.work_object_frame, text="Inserire si è lavorato in passato: ", font=main_font)
        self.work_subject.grid(row=0, column=0, sticky="nsew", pady=10)
        
        self.button_var_work = customtkinter.StringVar(value="Si")
        self.button_subject_work = customtkinter.CTkSegmentedButton(master=self.work_object_frame, values=["Si","No"], font=main_font, variable=self.button_var_work)
        self.button_subject_work.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
        
        # voto a lavoro
        self.job_test_frame = customtkinter.CTkFrame(master=self.center_frame, fg_color="transparent")
        self.job_test_frame.grid(row=5, column=0, sticky="nsew", padx=20)
        
        self.job_label = customtkinter.CTkLabel(self.job_test_frame, text="Inserire voto Test a Lavoro: ", font=main_font)
        self.job_label.grid(row=0, column=0, pady=10, sticky="nsew")
        
        self.job_entry = customtkinter.CTkEntry(master=self.job_test_frame, placeholder_text="Qualsiasi", font=main_font)
        self.job_entry.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
        
        # specialistica
        self.specialization_object_frame = customtkinter.CTkFrame(master=self.center_frame, fg_color="transparent")
        self.specialization_object_frame.grid(row=6, column=0, sticky="nsew", padx=20)
        
        self.specialization_subject = customtkinter.CTkLabel(self.specialization_object_frame, text="Inserire si è lavorato in passato: ", font=main_font)
        self.specialization_subject.grid(row=0, column=0, sticky="nsew", pady=10)
        
        self.button_var_specialization = customtkinter.StringVar(value="Mkt&HumanR")
        self.button_subject_specialization = customtkinter.CTkSegmentedButton(master=self.specialization_object_frame,
                                                                              values=["Mkt&HumanR","Mkt&Finance"], font=main_font, variable=self.button_var_specialization)
        self.button_subject_specialization.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
        
        self.scan_button = customtkinter.CTkButton(master=self.main_frame, text="Ricerca ", image=self.search_logo,
                                                       compound="right",
                                                       font=customtkinter.CTkFont(size=30, weight="bold"))
        self.scan_button.grid(row=3, column=0, sticky="ns")
        
        #self.toplevel_window = None
        #
        #def open_scan_toplevel(self):
        #    var1 = self.voti_entry.get()
        #    var2 = self.button_subject.get()
        #    var3 = self.degree_entry.get()
        #    var4 = self.button_subject_laurea.get()
        #    var5 = self.button_subject_work.get()
        #    var6 = self.job_entry.get()
        #    var7 = self.button_subject_specialization.get()
        #    
        #    if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
        #        self.toplevel_window = top_research(self, var1, var2, var3, var4, var5, var6, var7)  # create window if its None or destroyed
        #    else:
        #        self.toplevel_window.focus()  # if window exists focus it
            
        
if __name__ == "__main__":
    
    app = gui_ai()
    app.mainloop()