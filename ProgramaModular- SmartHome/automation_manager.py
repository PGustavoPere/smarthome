class AutomationManager:
    def __init__(self):
        self.automation_config = {}  # Diccionario que almacena la automatización
    

    def configurar_automatizacion(self, condicion, accion):
        self.automation_config = {"condicion": condicion, "accion": accion}
        return f"Automatización configurada: Cuando {condicion}, ejecutar {accion}."

    def obtener_automatizacion(self):
        return self.automation_config if self.automation_config else "Todavia no se ha configurado."