from comando import *
from paquete_datos import *
from enlace import *

conexion_USB = EnlaceUSB()
holter_por_usb = Destinatario(conexion_USB)
invocador = Invocador()

invocador.registrar_comando("leer_estado", LectorStatusHolter(holter_por_usb,
                                                              ComandoHolterStatus(),
                                                              RespuestaHolterStatus()))
invocador.registrar_comando("leer_configuracion", LectorConfiguracionHolter(holter_por_usb,
                                                                            ComandoHolterConfiguracion(),
                                                                            RespuestaHolterConfiguracion()))


