import string

# Secuencia de caracteres que vas a usar
sequence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Crear el mapeo de la secuencia (circular)
mapping = {sequence[i]: sequence[(i + 1) % len(sequence)] for i in range(len(sequence))}
reverse_mapping = {sequence[i]: sequence[(i - 1) % len(sequence)] for i in range(len(sequence))}

# Función para cifrar la palabra
def encrypt(word, shift_count):
    encrypted_word = list(word)  # Convertir la palabra en una lista de caracteres para manipularla
    shift_count = shift_count % len(sequence)  # Reducir el desplazamiento con módulo
    for _ in range(shift_count):
        encrypted_word = [mapping[char] if char in mapping else char for char in encrypted_word]
    return "".join(encrypted_word)

# Función para descifrar la palabra
def decrypt(word, shift_count):
    decrypted_word = list(word)  # Convertir la palabra en una lista de caracteres para manipularla
    shift_count = shift_count % len(sequence)  # Reducir el desplazamiento con módulo
    for _ in range(shift_count):
        decrypted_word = [reverse_mapping[char] if char in reverse_mapping else char for char in decrypted_word]
    return "".join(decrypted_word)

# Función principal que ofrece las opciones al usuario
def main():
    print("Bienvenido al cifrador y descifrador de palabras.")
    
    # Obtener la palabra y el tipo de acción (cifrado o descifrado)
    action = input("¿Quieres cifrar o descifrar una palabra? (cifrar/descifrar): ").strip().lower()
    if action not in ["cifrar", "descifrar"]:
        print("Opción no válida, elige 'cifrar' o 'descifrar'.")
        return
    
    word = input("Introduce la palabra: ")
    shift_count = int(input("Introduce la cantidad de desplazamientos: "))
    
    if action == "cifrar":
        encrypted_word = encrypt(word, shift_count)
        print(f"Palabra cifrada: {encrypted_word}")
    elif action == "descifrar":
        decrypted_word = decrypt(word, shift_count)
        print(f"Palabra original (después de descifrar): {decrypted_word}")

# Ejecutar la función principal
if __name__ == "__main__":
    main()

#cifrada: uxB mrxBnB mnknw nBCjA uxlxB
#decifrado: los dioses deben estar locos

#nqu fkqugu fgdgp guvct nqequ