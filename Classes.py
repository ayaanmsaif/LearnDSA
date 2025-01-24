import customtkinter as ctk

class Window(ctk.CTk):
    def __init__(self, title, height, width):
       
       super().__init__()

       ctk.set_default_color_theme("green")
       ctk.set_appearance_mode("light")

       self._title = title 
       self.height = height
       self.width = width 

       self.geometry(str(self.height)+"x"+str(self.width))
       self.title(self._title)
       self.resizable(width=False, height = False)

    def close(self):
        self.window.destroy() 