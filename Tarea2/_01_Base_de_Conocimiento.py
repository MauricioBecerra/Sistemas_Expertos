# Mauricio Becerra Guzman - 21310105
# Base de Conocimiento
class KnowledgeBase:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        """Agrega una nueva regla"""
        self.rules.append(rule)

    def get_rules(self):
        """Obtiene todas las reglas"""
        return self.rules

# Uso
knowledge_base = KnowledgeBase()
knowledge_base.add_rule("If humidity < 40% then activate humidifier")
print("Reglas en la Base de Conocimiento:", knowledge_base.get_rules())
