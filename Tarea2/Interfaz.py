# Mauricio Becerra Guzman - 21310105
# Interfaz para interacción con el usuario
class Interface:
    def interact(self):
        """Simula una interacción con el usuario"""
        user_input = input("Enter a command (e.g., 'check status'): ")
        if user_input == "check status":
            return "System status is normal."
        return "Unknown command."

# Uso
interface = Interface()
print(interface.interact())
