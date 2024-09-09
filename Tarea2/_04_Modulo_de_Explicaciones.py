# Mauricio Becerra Guzman - 21310105
# Módulo de Explicaciones
class ExplanationModule:
    def explain(self, inference):
        if inference == "Inference: Turn on fan":
            return "The system decided to turn on the fan because the temperature is above 30 degrees."
        return "No explanation available."

# Uso
explanation_module = ExplanationModule()
explanation = explanation_module.explain(result)
print("Explicación:", explanation)

