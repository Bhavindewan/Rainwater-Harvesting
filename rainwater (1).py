import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Function to calculate harvested rainwater
def calculate_rainwater_harvesting():
    try:
        roof_area = int(roof_area_slider.get())
        rainfall = int(rainfall_slider.get())
        tank_size = int(tank_size_slider.get())

        harvested_rainwater = (roof_area * rainfall) / 1000  # in liters
        tanks_required = harvested_rainwater / tank_size

        result_label.config(text=f"Harvested Rainwater: {harvested_rainwater:.2f} liters\nTanks Required: {tanks_required:.2f} tanks")

    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# Function to update slider value labels
def update_slider_value_labels(event):
    roof_area_value_label.config(text=f"{int(roof_area_slider.get()):d} m^2")
    rainfall_value_label.config(text=f"{int(rainfall_slider.get()):d} mm")
    tank_size_value_label.config(text=f"{int(tank_size_slider.get()):d} liters")

# Create the main window
root = tk.Tk()
root.title("Rainwater Harvesting Calculator")

# Create a frame for sliders
frame = ttk.Frame(root)
frame.pack(padx=20, pady=20)

# Roof Area Slider
roof_area_label = ttk.Label(frame, text="Roof Area:")
roof_area_label.grid(row=0, column=0, padx=10)
roof_area_slider = ttk.Scale(frame, from_=50, to=500, length=300, orient="horizontal")
roof_area_slider.set(200)
roof_area_slider.grid(row=0, column=1)

roof_area_value_label = ttk.Label(frame, text=f"{int(roof_area_slider.get()):d} m^2")
roof_area_value_label.grid(row=0, column=2)

# Rainfall Slider
rainfall_label = ttk.Label(frame, text="Rainfall:")
rainfall_label.grid(row=1, column=0, padx=10)
rainfall_slider = ttk.Scale(frame, from_=0, to=500, length=300, orient="horizontal")
rainfall_slider.set(100)
rainfall_slider.grid(row=1, column=1)

rainfall_value_label = ttk.Label(frame, text=f"{int(rainfall_slider.get()):d} mm")
rainfall_value_label.grid(row=1, column=2)

# Tank Size Slider
tank_size_label = ttk.Label(frame, text="Tank Size:")
tank_size_label.grid(row=2, column=0, padx=10)
tank_size_slider = ttk.Scale(frame, from_=1000, to=10000, length=300, orient="horizontal")
tank_size_slider.set(2000)
tank_size_slider.grid(row=2, column=1)

tank_size_value_label = ttk.Label(frame, text=f"{int(tank_size_slider.get()):d} liters")
tank_size_value_label.grid(row=2, column=2)

# Calculate Button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_rainwater_harvesting)
calculate_button.pack()

# Result Label
result_label = ttk.Label(root, text="")
result_label.pack()

# Bind the slider update function to the slider movement
roof_area_slider.bind("<Motion>", update_slider_value_labels)
rainfall_slider.bind("<Motion>", update_slider_value_labels)
tank_size_slider.bind("<Motion>", update_slider_value_labels)

# Start the main loop
root.mainloop()
