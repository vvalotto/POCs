from comando import *
from paquete_datos import *

destinatario = Destinatario("Dongle")
invocador = Invocador()

invocador.registrar_comando("leer_estado", LectorStatusHolter(destinatario, ComandoLecturaStatusEnvio()))
invocador.registrar_comando("leer_configuracion", LectorConfiguracionHolter(destinatario, ComandoLecturaConfiguracionEnvio()))


