import tkinter as tk
import customtkinter as ctk

# My Own Imports
from database import User, session 
from Classes import Window
from bubblesortmain import BubbleSortMain

class Dashboard(Window):
    def __init__(self, username):
        super().__init__("Dashboard", 1280, 720)
        self.username = username

        # Configure grid weights for the main window
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_rowconfigure(0, weight=1)

        # Create sidebar with fixed width
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=0, fg_color="#f0f0f0")
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.sidebar.grid_propagate(False)

        # Welcome message at the top
        self.welcome_label = ctk.CTkLabel(self, text=f"Welcome Back to LearnDSA, {username}", font=("Arial", 24, "bold"))
        self.welcome_label.grid(row=0, column=1, padx=20, pady=20, sticky="n")

        # Content area - initially empty
        self.content_frame = ctk.CTkFrame(self)
        self.content_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=(80, 20))

        # Add sidebar content
        self.logo_label = ctk.CTkLabel(self.sidebar, text="LearnDSA", font=("Arial", 24, "bold"))
        self.logo_label.grid(row=0, column=0, pady=(20, 30), padx=20)

        # Navigation buttons
        self.dashboard_btn = ctk.CTkButton(
            self.sidebar,
            text="Dashboard",
            anchor="w",
            fg_color="transparent",
            text_color="black",
            hover_color="#e0e0e0",
            font=("Arial", 14),
            command=self.show_dashboard
        )
        self.dashboard_btn.grid(row=1, column=0, padx=10, pady=5, sticky="ew")

        self.learn_btn = ctk.CTkButton(
            self.sidebar,
            text="Learn",
            anchor="w",
            fg_color="transparent",
            text_color="black",
            hover_color="#e0e0e0",
            font=("Arial", 14),
            command=self.show_learn_content
        )
        self.learn_btn.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

        self.track_btn = ctk.CTkButton(
            self.sidebar,
            text="Track Revision",
            anchor="w",
            fg_color="transparent",
            text_color="black",
            hover_color="#e0e0e0",
            font=("Arial", 14)
        )
        self.track_btn.grid(row=3, column=0, padx=10, pady=5, sticky="ew")

        self.settings_btn = ctk.CTkButton(
            self.sidebar,
            text="Settings",
            anchor="w",
            fg_color="transparent",
            text_color="black",
            hover_color="#e0e0e0",
            font=("Arial", 14)
        )
        self.settings_btn.grid(row=4, column=0, padx=10, pady=5, sticky="ew")

        # Configure sidebar for profile section
        self.sidebar.grid_rowconfigure(5, weight=1)

        # Profile section
        self.profile_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        self.profile_frame.grid(row=6, column=0, padx=10, pady=20, sticky="ew")

        self.profile_pic = ctk.CTkLabel(
            self.profile_frame,
            text="",
            width=40,
            height=40,
            fg_color="#FF0000",
            corner_radius=20
        )
        self.profile_pic.grid(row=0, column=0, padx=5)

        self.username_label = ctk.CTkLabel(
            self.profile_frame,
            text=username,
            font=("Arial", 14)
        )
        self.username_label.grid(row=0, column=1, padx=5)

    def clear_content(self):
        """Clear all widgets from the content frame"""
        for widget in self.content_frame.winfo_children():
            widget.destroy()

    def show_dashboard(self):
        """Show dashboard content (blank for now)"""
        self.clear_content()
        # You can add dashboard-specific content here in the future

    def show_learn_content(self):
        """Show the learning materials and courses"""
        self.clear_content()

        # Configure content frame grid
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        # Create frames for left and right columns
        self.leftsubject_frame = ctk.CTkFrame(self.content_frame)
        self.rightsubject_frame = ctk.CTkFrame(self.content_frame)
        
        self.leftsubject_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.rightsubject_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Configure the subject frames
        for frame in [self.leftsubject_frame, self.rightsubject_frame]:
            frame.grid_columnconfigure(0, weight=1)
            for i in range(4):
                frame.grid_rowconfigure(i, weight=1)

        # Add buttons to left frame
        subjects_left = ["Linked Lists", "Red-Black Graphs", "Calculus in CS", "The Taylor Series"]
        for i, subject in enumerate(subjects_left):
            btn = ctk.CTkButton(
                self.leftsubject_frame,
                text=subject,
                width=500,
                height=50,
                fg_color="white",
                text_color="black",
                font=("Arial", 14)
            )
            btn.grid(row=i, column=0, padx=10, pady=5)

        # Add buttons to right frame
        subjects_right = ["Merge Sort", "Graph Traversal", "Bubble Sort"]
        for i, subject in enumerate(subjects_right):
            btn = ctk.CTkButton(
                self.rightsubject_frame,
                text=subject,
                width=500,
                height=50,
                fg_color="white",
                text_color="black",
                font=("Arial", 14)
            )
            if subject == "Bubble Sort":
                btn.configure(command=self.redirect_bubble)
            btn.grid(row=i, column=0, padx=10, pady=5)

    def redirect_bubble(self):
        """Handle navigation to the Bubble Sort page"""
        self.destroy()
        from bubblesortmain import BubbleSortMain
        bubble_sort = BubbleSortMain(self.username)
        bubble_sort.mainloop()