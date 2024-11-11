import tkinter as tk

# Initialize the main window
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")

# Title label
title_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 14))
title_label.pack(pady=10)

# Create 10 input fields for subject scores
inputs = []
for i in range(10):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}")
    label.pack()
    entry = tk.Entry(root)
    entry.pack(pady=5)
    inputs.append(entry)

# Function to show the prediction result
def show_prediction():
    result_label.config(text="Teknologi Informasi")

# Prediction button
predict_button = tk.Button(root, text="Hasil Prediksi", command=show_prediction)
predict_button.pack(pady=20)

# Output label for the prediction result
result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)

# Run the main event loop
root.mainloop()
