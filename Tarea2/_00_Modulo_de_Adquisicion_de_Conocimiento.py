# Mauricio Becerra Guzman - 21310105
# Módulo de Adquisición de Conocimiento
class KnowledgeAcquisition:
    def __init__(self, knowledge_base, facts_base):
        self.knowledge_base = knowledge_base
        self.facts_base = facts_base

    def acquire_from_expert(self, rule):
        """Adquiere reglas de un experto"""
        self.knowledge_base.add_rule(rule)
        print(f"Regla adquirida: {rule}")

    def acquire_from_sensor(self, sensor_data):
        """Adquiere hechos de sensores"""
        fact = f"Temperature is {sensor_data['temperature']} degrees"
        self.facts_base.add_fact(fact)
        print(f"Hecho adquirido del sensor: {fact}")

# Uso
knowledge_base = KnowledgeBase()
facts_base = FactsBase()
acquisition_module = KnowledgeAcquisition(knowledge_base, facts_base)
acquisition_module.acquire_from_expert("If temperature > 30 then turn on fan")
acquisition_module.acquire_from_sensor({"temperature": 32})
