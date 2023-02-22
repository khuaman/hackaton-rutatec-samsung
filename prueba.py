from os import path
from notifypy import Notify
import time

icono = "icono.png"
direcion = path.abspath(path.dirname(__file__))

NotigicacionBase = Notify(
    default_notification_title="Umaru",
    default_notification_icon=path.join(direcion, icono),
)


def EnviarNotificacion(mensaje, audio):
    NotigicacionBase = Notify()
    NotigicacionBase.title = "Discapacitados maps"
    NotigicacionBase.message = mensaje
    if audio is not None:
        NotigicacionBase.audio = path.join(direcion, audio)
    NotigicacionBase.send()


Mensajes = [
    {"mensaje": "Hola", "audio": None, "espera": 4},
    {"mensaje": "Bienvenido a discapacitados maps", "audio": "audio/bienvenida.wav", "espera": 4},
    {
        "mensaje": "¿Deseas inicar sesión?",
        "audio": "audio/iniciar_sesion.wav",
        "espera": 4,
    },
    {"mensaje": "¿Deseas registrarte?", "audio": "audio/registro.wav", "espera": 4},
    {"mensaje": "Tienes una notificacion, alguien necesita ayuda", "audio": "alguien_nayuda.wav", "espera": 4},
    {"mensaje": "Necesito ayuda", "audio": "audio/necesito_ayuda.wav", "espera": 5},
    {
        "mensaje": "Felicidades, ingreso satisfactoriamente",
        "audio": "audio/ingreso.wav",
        "espera": 10,
    },
    {"mensaje": "Adiós", "audio": "audio/adiós.wav", "espera": 4},
]

# time.sleep(espera)
for Mensaje in Mensajes:
    print(f"Repoducion: {Mensaje=}")
    EnviarNotificacion(Mensaje["mensaje"], Mensaje["audio"])
    time.sleep(Mensaje["espera"])