class DeviceManager:
    def __init__(self):
        self.device_list = []  # Lista que almacena dispositivos

    def agregar_dispositivo(self, nombre_dispositivo, tipo_dispositivo):
        dispositivo = {
            "nombre": nombre_dispositivo,
            "tipo": tipo_dispositivo,
            "estado": "apagado"
        }
        self.device_list.append(dispositivo)
        return f"Dispositivo '{nombre_dispositivo}' agregado."

    def listar_dispositivos(self):
        return self.device_list if self.device_list else "No hay dispositivos registrados."

    def buscar_dispositivo(self, nombre_dispositivo):
        for dispositivo in self.device_list:
            if dispositivo["nombre"] == nombre_dispositivo:
                return dispositivo
        return "Dispositivo no encontrado."

    def eliminar_dispositivo(self, nombre_dispositivo):
        for dispositivo in self.device_list:
            if dispositivo["nombre"] == nombre_dispositivo:
                self.device_list.remove(dispositivo)
                return f"Dispositivo '{nombre_dispositivo}' eliminado."
        return "Dispositivo no encontrado."