import tkinter as tk
from tkinter import messagebox

# Fungsi untuk memprediksi prodi
def hasil_prediksi():
    # Menampilkan hasil prediksi
    hasil_label.config(text="Prodi yang diprediksi: Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("400x500")  # Mengatur ukuran jendela

# Membuat label judul
judul_label = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan", font=("Arial", 16, "bold"))
judul_label.pack(pady=10)

# Membuat input nilai mata pelajaran
input_labels = []
input_entries = []

for i in range(10):
    label = tk.Label(root, text=f"Nilai Mata Pelajaran {i+1}:")
    label.pack(anchor="w", padx=20)
    entry = tk.Entry(root)
    entry.pack(padx=20, pady=5, fill="x")
    input_labels.append(label)
    input_entries.append(entry)

# Membuat tombol prediksi
prediksi_button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi)
prediksi_button.pack(pady=20)

# Membuat label untuk hasil prediksi
hasil_label = tk.Label(root, text="", font=("Arial", 12))
hasil_label.pack(pady=10)

# Menjalankan loop utama
root.mainloop()