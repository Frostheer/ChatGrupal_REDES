# ChatGrupal_REDES
Proyecto construido para el ramo Redes de computadores [ICC711]

# Aplicación de Chat Grupal por Consola

Este proyecto es una aplicación de chat grupal basada en consola implementada en Python. Soporta múltiples usuarios, grupos y roles (usuario, administrador, super administrador) con varios comandos para interactuar dentro del chat.

## Características

- **Roles de Usuario**: Usuarios regulares, Administradores y Super Administradores.
- **Grupos**: Los usuarios pueden unirse a grupos predefinidos y comunicarse dentro de esos grupos.
- **Comandos**: Los usuarios pueden cambiar su nombre, unirse a grupos, cambiar los colores de los mensajes y más.
- **Comandos de Administrador**: Los administradores pueden ver mensajes y comandos de otros usuarios, y crear nuevos grupos.
- **Comandos de Super Administrador**: Los super administradores pueden cerrar el servidor y realizar todas las acciones de los administradores.

## Empezando

### Requisitos

- Python 3.x

### Instalación

1. Clona el repositorio:
    ```bash
    git clone https://github.com/Frostheer/ChatGrupal_REDES.git
    cd chat-grupal-consola
    ```


### Uso

#### Ejecutando el Servidor

Para iniciar el servidor, utiliza el siguiente comando:

```bash
python ServerManager.py -spa tu_super_contraseña -p tu_puerto -h tu_host
```

-spa o --super_admin_password: Contraseña del super administrador (por defecto: contraseñaSuperAdmin1234)
-p o --port: Puerto del servidor (por defecto: 9999)
-h o --host: Host del servidor (por defecto: 127.0.0.1)


#### Estructura del proyecto 

chat-grupal-consola/
│
├── Client/
│   └── ClientManager.py
├── Server/
│   ├── ServerManager.py
│   └── User.py
├── utils/
│   ├── ColorEnum.py
│   └── HelpMessages.py
├── LICENSE
└── README.md
