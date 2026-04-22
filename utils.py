import json

def load_data():
    with open("knowledge_base.json") as f:
        return json.load(f)

def format_plans(data):
    response = ""
    for plan in data["plans"]:
        response += f"{plan['name']} Plan ({plan['price']}):\n"
        for ftr in plan["features"]:
            response += f" - {ftr}\n"
    return response