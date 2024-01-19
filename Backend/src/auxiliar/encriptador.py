from cryptography.fernet import Fernet

# Genera una nueva clave y se guarda para utilizarla posteriormente
def generar_y_guardar_clave():
    clave = Fernet.generate_key()
    with open("clave_secreta.key", "wb") as archivo_clave:
        archivo_clave.write(clave)

# Carga la clave desde el archivo
def cargar_clave():
    return open("src/auxiliar/clave_secreta.key", "rb").read()

# Encripta una contraseña utilizando la clave
def encriptar_contrasenia(contrasena):
    clave = cargar_clave()
    cifrador = Fernet(clave)
    contrasena_encriptada = cifrador.encrypt(contrasena.encode())
    return contrasena_encriptada.decode()

# Desencripta una contraseña utilizando la clave
def desencriptar_contrasenia(contrasena_encriptada):
    clave = cargar_clave()
    cifrador = Fernet(clave)
    contrasena = cifrador.decrypt(contrasena_encriptada).decode()
    return contrasena


if __name__ == '__main__':
    # generar_y_guardar_clave()

    # Carga la clave desde el archivo
    clave = cargar_clave()

    # Encripta una contraseña
    contrasena_original = "mi_contrasena_secreta"

    print(f"Contraseña original: {contrasena_original}")

    contrasena_encriptada = encriptar_contrasenia(contrasena_original)
    print(f"Contraseña encriptada: {contrasena_encriptada}")

    # Desencripta la contraseña
    contrasena_desencriptada = desencriptar_contrasenia(contrasena_encriptada)
    print(f"Contraseña desencriptada: {contrasena_desencriptada}")
