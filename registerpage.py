import tkinter as tk
import customtkinter as ctk

#My Own Imports
from database import User, session 
from Classes import Window

class RegisterPage(Window):
    def __init__(self): 
        super().__init__("Register", 400, 300, )

        # Widgets
        self.register_text = ctk.CTkLabel(self, text="Learn DSA - Register", font=("Arial", 24, "bold" ))
        self.register_text.pack(pady=20)

        self.input_username = ctk.CTkEntry(self, placeholder_text="Username", width=300, corner_radius=20, height=40)
        self.input_username.pack(pady=10)

        self.input_password = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=300, corner_radius=20, height=40)
        self.input_password.pack(pady=10)

        self.login_button = ctk.CTkButton(self, text="Register", fg_color="green", text_color="white", width=300, height=30, corner_radius=20, command=self.register_button_handler)
        self.login_button.pack(pady=20, padx=20)

        self.account_exists = ctk.CTkButton(self, text="Have an account? - Login", font=("Arial",10,"bold"), fg_color="white", border_color="green", text_color="black", command=self.login_redirect)
        self.account_exists.pack()

    # Subroutines 
    def register_button_handler(self):
        username = self.input_username.get()
        password = self.input_password.get() 
        print("Username:", username)
        print("Password:", password)

        new_user = User(username=username, password=password)
        session.add(new_user)
        session.commit() 

    def login_redirect(self):
        from loginpage import LoginPage 
        self.destroy() 
        login_page = LoginPage() 
        login_page.mainloop() 

# Application 
app = RegisterPage() 
app.mainloop() 