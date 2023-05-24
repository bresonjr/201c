import tkinter as tk

def calculate_interest():
    p = float(principal_entry.get())
    r = float(rate_entry.get())
    t = float(time_entry.get())
    result = (p * r * t) / 100
    result = round(result, 2)
    result_label.config(text="The interest is: $" + str(result))

root = tk.Tk()
root.geometry("300x200")
root.title("Interest Calculator")
root.configure(bg="white")

heading_label = tk.Label(root, text="Interest Calculator", font=("Arial", 16))
heading_label.place(x=75, y=10)

principal_label = tk.Label(root, text="Principal:")
principal_label.place(x=30, y=50)

principal_entry = tk.Entry(root)
principal_entry.place(x=120, y=50)

rate_label = tk.Label(root, text="Rate of Interest:")
rate_label.place(x=30, y=80)

rate_entry = tk.Entry(root)
rate_entry.place(x=120, y=80)

time_label = tk.Label(root, text="Time:")
time_label.place(x=30, y=110)

time_entry = tk.Entry(root)
time_entry.place(x=120, y=110)

calculate_button = tk.Button(root, text="Calculate", command=calculate_interest)
calculate_button.place(x=130, y=140)

result_frame = tk.LabelFrame(root, text="Result", padx=10, pady=10)
result_frame.place(x=30, y=180)

result_label = tk.Label(result_frame, text="")
result_label.pack()

root.mainloop()
