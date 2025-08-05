import json

# Ruta del notebook 
ruta = "/MachineTranslation_en_to_ml.ipynb"  # cambia esto

# Cargar el notebook como JSON
with open(ruta, "r", encoding="utf-8") as f:
    data = json.load(f)

# Limpia los widgets si están dañados
if "widgets" in data.get("metadata", {}):
    print("Corrigiendo metadata.widgets...")
    del data["metadata"]["widgets"]

# Guardar el notebook limpio
with open(ruta, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=1)

print("Notebook .")