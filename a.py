import json

nb = "/MachineTranslation_en_to_ml.ipynb"  

# load nb as JSON
with open(ruta, "r", encoding="utf-8") as f:
    data = json.load(f)

# Clean the widgets if they are damaged
if "widgets" in data.get("metadata", {}):
    print("Correcting metadata.widgets")
    del data["metadata"]["widgets"]

# Save the clean nb
with open(nb, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=1)

print("Notebook cleaned.")
