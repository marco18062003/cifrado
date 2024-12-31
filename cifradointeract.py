import tkinter as tk
from tkinter import messagebox

# Secuencia de caracteres que vas a usar (incluyendo letras minúsculas de a-z, mayúsculas y símbolos especiales)
sequence = "PQ⇔l-∃$i#W~∵∪>¬y√∑∂∬a8VbD\\Mx∈HSq≠∉7R÷4`v[KF∆Yd%.E≡,U⊂z*+⊆&⊃⊄t@∞:∩J×∀9_I∇]N≤j0'p∴∝∏{6Lo≈g}‖⊇∧)2?^=B13∨≥cZmk|⊥X<nA∮⇒uC5rs!Ohw;GT∫fe/("

# Crear el mapeo de la secuencia (circular)
mapping = {sequence[i]: sequence[(i + 1) % len(sequence)] for i in range(len(sequence))}
reverse_mapping = {sequence[i]: sequence[(i - 1) % len(sequence)] for i in range(len(sequence))}

# Función para cifrar la palabra
def encrypt(word, shift_count):
    encrypted_word = list(word)  # Convertir la palabra en una lista de caracteres para manipularla
    shift_count = shift_count % len(sequence)  # Reducir el desplazamiento con módulo
    for _ in range(shift_count):
        encrypted_word = [mapping.get(char, char) for char in encrypted_word]  # Usar .get para evitar KeyError
    return "".join(encrypted_word)

# Función para descifrar la palabra
def decrypt(word, shift_count):
    decrypted_word = list(word)  # Convertir la palabra en una lista de caracteres para manipularla
    shift_count = shift_count % len(sequence)  # Reducir el desplazamiento con módulo
    for _ in range(shift_count):
        decrypted_word = [reverse_mapping.get(char, char) for char in decrypted_word]  # Usar .get para evitar KeyError
    return "".join(decrypted_word)

# Función que se ejecuta cuando el botón de cifrar es presionado
def on_encrypt():
    word = entry_word.get()
    try:
        shift_count = int(entry_shift.get())
        encrypted_word = encrypt(word, shift_count)
        label_result.config(text=f"Palabra cifrada: {encrypted_word}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido para los desplazamientos.")

# Función que se ejecuta cuando el botón de descifrar es presionado
def on_decrypt():
    word = entry_word.get()
    try:
        shift_count = int(entry_shift.get())
        decrypted_word = decrypt(word, shift_count)
        label_result.config(text=f"Palabra descifrada: {decrypted_word}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, introduce un número válido para los desplazamientos.")

# Crear la ventana principal
root = tk.Tk()
root.title("Cifrador y Descifrador de Palabras")

# Etiqueta para el título
label_title = tk.Label(root, text="Cifrador y Descifrador de Palabras", font=("Arial", 14))
label_title.pack(pady=10)

# Campo para la palabra a cifrar o descifrar
label_word = tk.Label(root, text="Introduce la palabra:")
label_word.pack()
entry_word = tk.Entry(root, width=30)
entry_word.pack(pady=5)

# Campo para la cantidad de desplazamientos
label_shift = tk.Label(root, text="Introduce la cantidad de desplazamientos:")
label_shift.pack()
entry_shift = tk.Entry(root, width=30)
entry_shift.pack(pady=5)

# Botones para cifrar y descifrar
button_encrypt = tk.Button(root, text="Cifrar", command=on_encrypt, width=20)
button_encrypt.pack(pady=5)

button_decrypt = tk.Button(root, text="Descifrar", command=on_decrypt, width=20)
button_decrypt.pack(pady=5)

# Etiqueta para mostrar el resultado
label_result = tk.Label(root, text="", font=("Arial", 12), fg="blue")
label_result.pack(pady=20)

# Ejecutar la ventana principal
root.mainloop()
