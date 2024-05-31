from enum import Enum

class HelpMessages(Enum):
    USER_HELP = (
        "\nComandos disponibles para usuarios:\n"
        "/nombre <nuevo_nombre> - Cambiar tu nombre\n"
        "/ingresar <nombre_grupo> - Ingresar a un grupo de chat\n"
        "/color <color> - Cambiar el color de tus mensajes\n"
        "/admin <contraseña> - Convertirse en administrador\n"
        "/grupos - Listar grupos disponibles\n"
        "/help - Mostrar esta ayuda\n"
    )

    ADMIN_HELP = (
        "\nComandos disponibles para admin:\n"
        "/nombre <nuevo_nombre> - Cambiar tu nombre\n"
        "/ingresar <nombre_grupo> - Ingresar a un grupo de chat\n"
        "/ver_mensajes <nombre_usuario> | <user_id> - Ver mensajes de un usuario\n"
        "/ver_comandos <nombre_usuario> | <user_id> - Ver comandos de un usuario\n"
        "/color <color> - Cambiar el color de tus mensajes\n"
        "/admin <contraseña> - Convertirse en administrador\n"
        "/crear_grupo <nombre_grupo> - Crear un nuevo grupo\n"
        "/grupos - Listar grupos disponibles\n"
        "/help - Mostrar esta ayuda\n"
    )

    SUPER_ADMIN_HELP = (
        "\nComandos disponibles para super admin:\n"
        "/nombre <nuevo_nombre> - Cambiar tu nombre\n"
        "/ingresar <nombre_grupo> - Ingresar a un grupo de chat\n"
        "/ver_mensajes <nombre_usuario> | <user_id> - Ver mensajes de un usuario\n"
        "/ver_comandos <nombre_usuario> | <user_id> - Ver comandos de un usuario\n"
        "/color <color> - Cambiar el color de tus mensajes\n"
        "/admin <contraseña> - Convertirse en administrador\n"
        "/crear_grupo <nombre_grupo> - Crear un nuevo grupo\n"
        "/grupos - Listar grupos disponibles\n"
        "/shutdown - Cerrar el servidor\n"
        "/help - Mostrar esta ayuda\n"
    )
