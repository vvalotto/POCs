from gestor_vinculo import GestorVinculo
import configurador_vinculo

invocador = configurador_vinculo.invocador
gestor = GestorVinculo(invocador)
gestor.obtener_holter()