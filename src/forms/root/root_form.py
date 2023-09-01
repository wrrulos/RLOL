import customtkinter

from src.forms.home.home_form import HomeForm
from src.utilities.ctk_utilities import CTKUtilities
from src.automation.script import Script

customtkinter.set_appearance_mode("dark")


class RootForm:
    def __init__(self, thread) -> None:
        self.root = customtkinter.CTk()
        self.thread = thread
        self.root.title('RLOL / By @wrrulos')
        self.root.iconbitmap('./assets/icon.ico')
        self.root.geometry('500x600+350+20')
        self.root.minsize(400, 500)
        self.root.config(bg='#010101')
        self.root.resizable(width=False, height=False)
        self.root.protocol('WM_DELETE_WINDOW', self.on_window_closed)
        HomeForm(self.root)
        self.root.mainloop()

    def on_window_closed(self):
        Script.stop() 
        self.thread.join()
        self.root.destroy()