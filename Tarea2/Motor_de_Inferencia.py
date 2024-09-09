# Mauricio Becerra Guzman - 21310105
# Motor de Inferencia
class InferenceEngine:
    def infer(self, rules, facts):
        """Realiza inferencia basada en reglas y hechos"""
        for rule in rules:
            if "temperature > 30" in rule and any("32 degrees" in fact for fact in facts):
                return "Inference: Turn on fan"
        return "No inference made"

# Uso
inference_engine = InferenceEngine()
result = inference_engine.infer(knowledge_base.get_rules(), facts_base.get_facts())
print("Resultado de la Inferencia:", result)

