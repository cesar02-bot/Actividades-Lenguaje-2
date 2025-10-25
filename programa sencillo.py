# Lista simulada de entradas de usuario
usuarios = ["Carlos_23", "Ana<script>", "Luis!", "Maria_89", "Pedro123"]

# Lista para almacenar usuarios válidos
usuarios_validos = []

# Ciclo para revisar cada entrada
for usuario in usuarios:
    # Condicional para validar que el nombre solo contenga letras, números y guiones bajos
    if usuario.replace("_", "").isalnum():
        usuarios_validos.append(usuario)
    else:
        print(f"Entrada inválida detectada: {usuario}")

# Resultado final
print("Usuarios válidos para insertar en la base de datos:", usuarios_validos)
