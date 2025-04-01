from utils import logger

USUARIOS_FILE = "data/usuarios.txt"

def cargar_usuarios():
    usuarios = {}
    try:
        with open(USUARIOS_FILE, "r") as f:
            for linea in f:
                usuario, contraseña = linea.strip().split(",")
                usuarios[usuario] = contraseña
    except Exception as e:
        logger.error(f"Error al cargar usuarios: {e}")
    return usuarios

def login():
    usuarios = cargar_usuarios()
    intentos = 3
    while intentos > 0:
        print("=== LOGIN ===")
        usuario = input("Usuario: ")
        contraseña = input("Contraseña: ")
        if usuario in usuarios and usuarios[usuario] == contraseña:
            logger.info(f"Usuario '{usuario}' inició sesión")
            print("\n✅ Acceso concedido.\n")
            return True
        else:
            intentos -= 1
            logger.warning(f"Intento fallido de login. Usuario: '{usuario}', contraseña ingresada: '{contraseña}'")
            print("\n❌ Usuario o contraseña incorrectos.")
            if intentos > 0:
                print(f"Intentos restantes: {intentos}\n")
            else:
                print("\n❌ Se agotaron los intentos de login. Cerrando sesión.")
                logger.error(f"Login fallido: Se agotaron los intentos para el usuario '{usuario}'")
    return False
