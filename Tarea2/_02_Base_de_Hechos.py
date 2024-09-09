# Mauricio Becerra Guzman - 21310105
# Base de Hechos
class FactsBase:
    def __init__(self):
        self.facts = []

    def add_fact(self, fact):
        """Agrega un nuevo hecho"""
        self.facts.append(fact)

    def get_facts(self):
        """Obtiene todos los hechos"""
        return self.facts

# Uso
facts_base = FactsBase()
facts_base.add_fact("Temperature is 32 degrees")
print("Hechos en la Base de Hechos:", facts_base.get_facts())
