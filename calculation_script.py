import tkinter as tk
from tkinter import simpledialog, messagebox

class GradeTableApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Class Grade Calculator")

        self.column_names = ["Assignment 1", "Assignment 2"]
        self.data_entries = {}

        self.create_table_layout()

        add_column_button = tk.Button(master, text="Add Column", command=self.add_column)
        add_column_button.grid(row=4, column=0, columnspan=2)

        remove_column_button = tk.Button(master, text="Remove Column", command=self.remove_column)
        remove_column_button.grid(row=4, column=2, columnspan=2)

        calculate_button = tk.Button(master, text="Calculate", command=self.calculate_grades)
        calculate_button.grid(row=5, column=0, columnspan=4)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=6, column=0, columnspan=4)

        gpa_button = tk.Button(master, text="Convert to GPA", command=self.convert_to_gpa)
        gpa_button.grid(row=7, column=0, columnspan=4)

        self.gpa_result_label = tk.Label(master, text="")
        self.gpa_result_label.grid(row=8, column=0, columnspan=4)

    def create_table_layout(self):
        tk.Label(self.master, text="").grid(row=0, column=0)
        for col, column_name in enumerate(self.column_names, start=1):
            tk.Label(self.master, text=column_name).grid(row=0, column=col)

        for row, header_text in enumerate(["Weight", "Grade"], start=1):
            tk.Label(self.master, text=header_text).grid(row=row, column=0)
            for col, _ in enumerate(self.column_names, start=1):
                entry = tk.Entry(self.master, width=10)
                entry.grid(row=row, column=col)
                self.data_entries[(row, col)] = entry

    def add_column(self):
        new_column_name = simpledialog.askstring("Add Column", "Enter Column Name:")
        if new_column_name:
            self.column_names.append(new_column_name)

            tk.Label(self.master, text=new_column_name).grid(row=0, column=len(self.column_names))

            for row, header_text in enumerate(["Weight", "Grade"], start=1):
                entry = tk.Entry(self.master, width=10)
                entry.grid(row=row, column=len(self.column_names))
                self.data_entries[(row, len(self.column_names))] = entry

    def remove_column(self):
        if len(self.column_names) > 2:
            column_to_remove = simpledialog.askstring("Remove Column", "Enter Column Name to Remove:")
            if column_to_remove in self.column_names:
                index = self.column_names.index(column_to_remove)
                self.column_names.pop(index)

                for row in range(1, 3):
                    entry = self.data_entries.pop((row, index + 1))
                    entry.grid_forget()

                for col in range(index + 2, len(self.column_names) + 2):
                    for row in range(1, 3):
                        self.data_entries[(row, col - 1)] = self.data_entries.pop((row, col))
                        self.data_entries[(row, col - 1)].grid(row=row, column=col - 1)
                self.master.grid_columnconfigure(col, weight=1)

            else:
                messagebox.showerror("Error", "Column not found!")

        else:
            messagebox.showerror("Error", "Cannot remove last two columns!")

    def calculate_grades(self):
        try:
            weights = []
            grades = []

            for col, _ in enumerate(self.column_names, start=1):
                weight_entry = self.data_entries[(1, col)]
                grade_entry = self.data_entries[(2, col)]

                weight = float(weight_entry.get())
                grade = float(grade_entry.get())

                if grade > 100:
                    messagebox.showerror("Error", "The highest grade must be 100% .")
                    return 
                weights.append(weight)
                grades.append(grade)

            average_grade = sum(w * grade for w, grade in zip(weights, grades)) / sum(weights)
            self.result_label.config(text=f"Average Grade: {average_grade:.2f}")

            if sum(weights) != 100:
                messagebox.showerror("Error", "The total percentage weight must be 100% .")
        except ValueError:
            messagebox.showerror("Error", "Please input values in empty slot(s).")

    def convert_to_gpa(self):
        try:
            weights = []
            grades = []

            for col, _ in enumerate(self.column_names, start=1):
                weight_entry = self.data_entries[(1, col)]
                grade_entry = self.data_entries[(2, col)]

                weight = float(weight_entry.get())
                grade = float(grade_entry.get())

                weights.append(weight)
                grades.append(grade)

            average_grade = sum(w * grade for w, grade in zip(weights, grades)) / sum(weights)
            gpa = self.calculate_gpa(average_grade)
            self.gpa_result_label.config(text=f"Equivalent GPA: {gpa:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values for weights and grades.")

    def calculate_gpa(self, percentage):
        if 90 <= percentage <= 100:
            return 4.0
        elif 80 <= percentage < 90:
            return 3.7
        elif 70 <= percentage < 80:
            return 3.3
        elif 60 <= percentage < 70:
            return 3.0
        elif 50 <= percentage < 60:
            return 2.7
        elif 40 <= percentage < 50:
            return 2.3
        elif 30 <= percentage < 40:
            return 2.0
        elif 20 <= percentage < 30:
            return 1.7
        elif 10 <= percentage < 20:
            return 1.3
        else:
            return 0.0

def destroy_window(event):
    root.destroy()

# Create the main window
root = tk.Tk()
root.geometry("600x400")  # Set the width and height of the window
app = GradeTableApp(root)
root.bind("<KeyPress-z>", destroy_window)
root.mainloop()
