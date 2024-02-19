import tkinter as tk
from tkinter import simpledialog, messagebox


class GradeTableApp:
    def __init__(self, master):
        self.master = master
        self.master.title(" Class Grade Calculator")

        self.column_names = ["Assignment 1", "Assignment 2"]
        self.data_entries = {}

        self.create_table_layout()

        add_column_button = tk.Button(master, text="Add Column", command=self.add_column)
        add_column_button.grid(row=4, column=0, columnspan=3)

        calculate_button = tk.Button(master, text="Calculate", command=self.calculate_grades)
        calculate_button.grid(row=5, column=0, columnspan=3)

        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=6, column=0, columnspan=3)

        gpa_button = tk.Button(master, text="Convert to GPA", command=self.convert_to_gpa)
        gpa_button.grid(row=7, column=0, columnspan=3)

        self.gpa_result_label = tk.Label(master, text="")
        self.gpa_result_label.grid(row=8, column=0, columnspan=3)

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

    def calculate_grades(self):
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

            average_grade = sum(grades) / len(grades)
            self.result_label.config(text=f"Average Grade: {average_grade:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Please note the total percentage weight must be 100%.")

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

            average_grade = sum(grades) / len(grades)
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
app = GradeTableApp(root)
root.bind("<KeyPress-z>", destroy_window)
root.mainloop()
