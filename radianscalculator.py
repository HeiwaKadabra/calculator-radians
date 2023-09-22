import tkinter as tk
from math import radians, degrees

def calculate_radians_from_degrees():
    try:
        degrees_value = float(degrees_entry.get())
        radians_result = degrees_value * (3.14159265358979323846 / 180.0) 
        result_label.config(text=f"{degrees_value} degrés équivaut à {radians_result:.4f} radians")
        explanation_label.config(text="Méthode : degrés * (π / 180)")
    except ValueError:
        result_label.config(text="Entrée invalide. Veuillez entrer un nombre valide en degrés.")
        explanation_label.config(text="")

def calculate_degrees_from_radians():
    try:
        radians_value = float(radians_entry.get())
        degrees_result = radians_value * (180.0 / 3.14159265358979323846)  
        result_label.config(text=f"{radians_value:.4f} radians équivaut à {degrees_result} degrés")
        explanation_label.config(text="Méthode : radians * (180 / π)")
    except ValueError:
        result_label.config(text="Entrée invalide. Veuillez entrer un nombre valide en radians.")
        explanation_label.config(text="")

window = tk.Tk()
window.title("Conversion degrés-radians")
window.resizable(False, False) 

degrees_label = tk.Label(window, text="Degrés:")
degrees_entry = tk.Entry(window)
radians_label = tk.Label(window, text="Radians:")
radians_entry = tk.Entry(window)
convert_to_radians_button = tk.Button(window, text="Convertir en radians", command=calculate_radians_from_degrees)
convert_to_degrees_button = tk.Button(window, text="Convertir en degrés", command=calculate_degrees_from_radians)
result_label = tk.Label(window, text="Résultat ici")
explanation_label = tk.Label(window, text="", font=("Helvetica", 10), wraplength=300)

degrees_label.grid(row=0, column=0)
degrees_entry.grid(row=0, column=1)
radians_label.grid(row=1, column=0)
radians_entry.grid(row=1, column=1)
convert_to_radians_button.grid(row=2, column=0)
convert_to_degrees_button.grid(row=2, column=1)
result_label.grid(row=3, columnspan=2)
explanation_label.grid(row=4, columnspan=2)

developer_label = tk.Label(window, text="Développeur: @heiwafr", anchor="e") 
developer_label.grid(row=5, column=1, sticky="e")

window.mainloop()
