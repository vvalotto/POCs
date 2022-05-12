from comando import *
from holter_comands import *

conexion_USB = EnlaceUSB()
conexion_Dongle = EnlaceDongle()
# holter_por_usb = Destinatario(conexion_USB)
holter_por_usb = Destinatario(conexion_Dongle)
invocador = Invocador()

# Leer Status Holter
comando = ComandoLecturaStatusEnvio()
invocador.registrar_comando("leer_estado", LectorStatusHolter(holter_por_usb, 
                                            comando,
                                            RespuestaHolterStatus()))

# Configurar Holter
invocador.registrar_comando("leer_configuracion",   LectorConfiguracionHolter(holter_por_usb, 
                                                    ComandoLecturaConfiguracionEnvio(), 
                                                    RespuestaHolterConfiguracion()))

# Parar Holter
invocador.registrar_comando("parar_modo_holter",    SetIdleMode(holter_por_usb, 
                                                    ComandoEscrituraModoIdleEnvio(),
                                                    RespuestaHolterEscritiuraOK()))

# Poner Modo Monitoreo
invocador.registrar_comando("poner_modo_monitoreo", PonerModoMonitoreo(holter_por_usb, 
                                                    ComandoEscrituraModoMonitoreoEnvio(),
                                                    RespuestaHolterEscritiuraOK()))

# Obtener ECG Monitoreo
invocador.registrar_comando("obtener_ecg_monitoreo",GetECGMonitor(holter_por_usb, 
                                                    ComandEmpty(),
                                                    RespuestaHolterEGCMonitoreo()))

# # desenlazar_holter
# invocador.registrar_comando("desenlazar_holter",    HolterDisconnect (holter_por_usb, 
#                                                     ComandEmpty(),
#                                                     RespuestaHolterEscritiuraOK()))