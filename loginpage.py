import tkinter as tk
import customtkinter as ctk

#My Own Imports
from database import User, session 
from Classes import Window

class LoginPage(Window):
    def __init__(self): 
        super().__init__("Login", 1280, 720, )

        # Widgets
        self.register_text = ctk.CTkLabel(self, text="Learn DSA - Login", font=("Arial", 24, "bold" ))
        self.register_text.pack(pady=20)

        self.input_username = ctk.CTkEntry(self, placeholder_text="Username", width=300, corner_radius=20, height=40)
        self.input_username.pack(pady=10)

        self.input_password = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=300, corner_radius=20, height=40)
        self.input_password.pack(pady=10)

        self.login_button = ctk.CTkButton(self, text="Login", command=self.login_button_handler, fg_color="green", text_color="white", width=300, height=30, corner_radius=20,)
        self.login_button.pack(pady=20, padx=20)

        self.account_exists = ctk.CTkButton(self, text="Need an account? - Register ", font=("Arial",10,"bold"), fg_color="white", border_color="green", text_color="black",command=self.redirect_register)
        self.account_exists.pack()

    # Subroutines 
    def login_button_handler(self):
        username = self.input_username.get()
        password = self.input_password.get() 
        print("Username:", username)
        print("Password:", password)

        user = session.query(User).filter_by(username=username, password=password).first()
       
        if user: 
            self.destroy() 
            from dashboard import Dashboard 
            dashboard = Dashboard(username)
            dashboard.mainloop()

        else: 
            print("Invalid Username or Password")
            
    def redirect_register(self):
        from registerpage import RegisterPage 
        self.after(100, self.destroy)
        register_page = RegisterPage()
        register_page.mainloop() 
         
# Application 
app = LoginPage() 
app.mainloop() 