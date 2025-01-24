import tkinter as tk
import customtkinter as ctk
import time

# My Own Imports
from database import User, session 
from Classes import Window

class BubbleSortMain(Window):
    def __init__(self, username):
        super().__init__("BubbleSortMain", 1280, 720)   
        self.current_page = "simulation"  # Track the current page

        # Initialize StringVars here
        self.q1_var = tk.StringVar(value="")
        self.q2_var = tk.StringVar(value="")
        self.q3_var = tk.StringVar(value="")

        # Create a frame for the simulation
        self.simulation_frame = ctk.CTkFrame(self)
        self.simulation_frame.pack(side="left", fill="both", expand=True, padx=(20, 10), pady=20)

        self.canvas = tk.Canvas(self.simulation_frame, width=600, height=600, bg="#e0e0e0")
        self.canvas.pack()

        self.play_button = ctk.CTkButton(self.simulation_frame, text="Play", command=self.bubble_sort, fg_color="#4CAF50", text_color="white")
        self.play_button.pack(pady=(10, 0))

        # Create a frame for the information
        self.info_frame = ctk.CTkFrame(self)
        self.info_frame.pack(side="right", fill="both", expand=True, padx=(10, 20), pady=20)

        self.info_label = ctk.CTkLabel(self.info_frame, text="What is Bubble Sort?", font=("Arial", 24, "bold"))
        self.info_label.pack(pady=(20, 10))

        self.placeholder_text = ctk.CTkLabel(self.info_frame, text="Bubble sort is a simple sorting algorithm that repeatedly steps through the list, compares adjacent elements, and swaps them if they are in the wrong order. The pass through the list is repeated until the list is sorted.", wraplength=400, justify="left")
        self.placeholder_text.pack(pady=(0, 20))

        # Navigation Buttons Frame
        self.navigation_frame = ctk.CTkFrame(self.info_frame)
        self.navigation_frame.pack(side="bottom", anchor="se", padx=20, pady=(10, 20))

        self.next_button = ctk.CTkButton(self.navigation_frame, text="Next", command=self.go_to_next_page, fg_color="#2196F3", text_color="white")
        self.next_button.pack(side="right", padx=(10, 0))

        self.array = [50, 20, 30, 10, 40]  
        self.bars = []  
        self.draw_array()

    def draw_array(self):
        self.canvas.delete("all")  
        bar_width = 50
        for i, value in enumerate(self.array):
            self.canvas.create_rectangle(i * bar_width, 600, (i + 1) * bar_width, 600 - value * 10, fill="blue")
            self.bars.append((i * bar_width, 600, (i + 1) * bar_width, 600 - value * 10))

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    self.draw_array()  
                    self.canvas.update()  
                    time.sleep(0.5)  
        self.play_button.configure(state="normal") 

    def go_to_next_page(self):
        if self.current_page == "simulation":
            self.current_page = "questions"
            self.clear_frames()
            self.create_questions_page()
        elif self.current_page == "questions":
            self.current_page = "how_to_code"
            self.clear_frames()
            self.create_how_to_code_page()

    def clear_frames(self):
        for widget in self.winfo_children():
            widget.destroy()

    def create_questions_page(self):
        questions_frame = ctk.CTkFrame(self)
        questions_frame.pack(fill="both", expand=True, padx=20, pady=20)

        #Question 1
        question1 = ctk.CTkLabel(questions_frame, text="1. What is the worst-case time complexity of bubble sort?", font=("Arial", 18))
        question1.pack(anchor="w", pady=(10, 5))
        ctk.CTkRadioButton(questions_frame, text="A) O(n log n)", variable=self.q1_var, value="A").pack(anchor="w")
        ctk.CTkRadioButton(questions_frame, text="B) O(n^2)", variable=self.q1_var, value="B").pack(anchor="w")
        ctk.CTkRadioButton(questions_frame, text="C) O(n)", variable=self.q1_var, value="C").pack(anchor="w")

        #Question 2
        question2 = ctk.CTkLabel(questions_frame, text="2. Which of the following is true about bubble sort?", font=("Arial", 18))
        question2.pack(anchor="w", pady=(10, 5))
        ctk.CTkRadioButton(questions_frame, text="A) It is a stable sort.", variable=self.q2_var, value="A").pack(anchor="w")
        ctk.CTkRadioButton(questions_frame, text="B) It is not a stable sort.", variable=self.q2_var, value="B").pack(anchor="w")
        ctk.CTkRadioButton(questions_frame, text="C) It is a divide and conquer algorithm.", variable=self.q2_var, value="C").pack(anchor="w")

        #Question 3
        question3 = ctk.CTkLabel(questions_frame, text="3. What is the best-case time complexity of bubble sort?", font=("Arial", 18))
        question3.pack(anchor="w", pady=(10, 5))
        ctk.CTkRadioButton(questions_frame, text="A) O(n)", variable=self.q3_var, value="A").pack(anchor="w")
        ctk.CTkRadioButton(questions_frame, text="B) O(n^2)", variable=self.q3_var, value="B").pack(anchor="w")
        ctk.CTkRadioButton(questions_frame, text="C) O(log n)", variable=self.q3_var, value="C").pack(anchor="w")

        # Navigation Buttons Frame
        self.navigation_frame = ctk.CTkFrame(questions_frame)
        self.navigation_frame.pack(side="bottom", anchor="se", padx=20, pady=(10, 20))

        previous_button = ctk.CTkButton(self.navigation_frame, text="Previous", command=self.go_to_previous_page, fg_color="#FF5722", text_color="white")
        previous_button.pack(side="left", padx=(10, 0))

        self.submit_button = ctk.CTkButton(self.navigation_frame, text="Submit", command=self.submit_answers, fg_color="#4CAF50", text_color="white")
        self.submit_button.pack(side="right", padx=(0, 10))

    def create_how_to_code_page(self):
        how_to_code_frame = ctk.CTkFrame(self)
        how_to_code_frame.pack(fill="both", expand=True, padx=20, pady=20)

        title_label = ctk.CTkLabel(how_to_code_frame, text="How to Code Bubble Sort", font=("Arial", 28, "bold"))
        title_label.pack(pady=(20, 10))
        
        code_example = [
            "def bubble_sort(arr):",
            "   n = len(arr)",
            "   for i in range(n):",
            "      for j in range(0, n-i-1):",
            "         if arr[j] > arr[j+1]:",
            "            arr[j], arr[j+1] = arr[j+1], arr[j]",
        ]

        # Create a frame for the code
        code_frame = ctk.CTkFrame(how_to_code_frame)
        code_frame.pack(pady=(10, 20))

        # Explanation area
        explanation_area = ctk.CTkLabel(how_to_code_frame, text="", wraplength=600, justify="left", font=("Arial", 14))
        explanation_area.pack(pady=(10, 20))

        # Create buttons for each line of code
        for index, line in enumerate(code_example):
            button = ctk.CTkButton(code_frame, text=f"{index + 1}. {line}", command=lambda line_num=index: self.show_explanation(line_num, explanation_area), text_color="black", fg_color="transparent", hover_color="#dbffd9", font=("Courier New", 20))
            button.pack(anchor="w", pady=2)

        # Navigation Buttons Frame
        self.navigation_frame = ctk.CTkFrame(how_to_code_frame)
        self.navigation_frame.pack(side="bottom", anchor="se", padx=20, pady=(10, 20))

        previous_button = ctk.CTkButton(self.navigation_frame, text="Previous", command=self.go_to_previous_page, fg_color="#FF5722", text_color="white")
        previous_button.pack(side="left", padx=(10, 0))

        finish_button = ctk.CTkButton(self.navigation_frame, text="Finish", command=self.finish, fg_color="#4CAF50", text_color="white")
        finish_button.pack(side="right", padx=(0, 10))

    def show_explanation(self, line_num, explanation_area):
        explanations = [
            "This line defines a function named `bubble_sort` that takes one parameter, `arr`, which is the list to be sorted.",
            "This line calculates the length of the array and stores it in the variable `n`.",
            "This outer loop runs `n` times, where `i` represents the current pass through the array.",
            "This inner loop compares adjacent elements. The `n-i-1` ensures that the last `i` elements are already sorted and do not need to be checked again.",
            "This condition checks if the current element is greater than the next element.",
            "If the condition is true, this line swaps the two elements to put them in the correct order.",
            "Finally, the sorted array is returned."
        ]
        explanation_area.configure(text=explanations[line_num])

    def finish(self):
        print("Quiz finished!")

    def go_to_previous_page(self):
        if self.current_page == "how_to_code":
            self.current_page = "questions"
            self.clear_frames()
            self.create_questions_page()
        else:
            self.current_page = "simulation"
            self.clear_frames()
            self.create_simulation_page()

    def submit_answers(self):
        score = 0
        if self.q1_var.get() == "B":  
            score += 1
        if self.q2_var.get() == "A":  
            score += 1
        if self.q3_var.get() == "A":  
            score += 1

        # Displays score
        score_label = ctk.CTkLabel(self, text=f"Your score: {score}/3", font=("Arial", 18))
        score_label.pack(pady=(20, 10))

        
        self.after(500, self.change_to_next_button)  

    def change_to_next_button(self):
        self.submit_button.configure(text="Next", command=self.go_to_next_page)
