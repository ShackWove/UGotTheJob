import sys
sys.path.insert(0, "../../source_code")
import threading
from tkinter import *
from tkinter import ttk
import customtkinter
import os
from PIL import Image


class GuiAi(customtkinter.CTk):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.title("UGotTheJob")
        self.geometry(f"700x800")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=4)
        self.resizable(False, False)
        
        # icon path
        icon_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), ("../../documentation"))
        
        # icon implementation path
        self.logo_icon = customtkinter.CTkImage(Image.open(os.path.join(icon_path, "job_seeking.png")), size=(100, 110))
        
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
        
        
        
        
if __name__ == "__main__":
    
    app = GuiAi()
    app.mainloop()