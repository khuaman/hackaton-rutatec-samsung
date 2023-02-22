from notifypy import Notify
from os import path

notification = Notify()
notification.title = "App"
notification.message = "Alguien nececita ayuda"
icono = "icono.png"
audio = "alguiennecesitaayuda.wav"
direcion = path.abspath(path.dirname(__file__))
notification.icon = path.join(direcion, icono)
notification.audio = path.join(direcion, audio)
notification.send()