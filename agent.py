from utils import load_data, format_plans

data = load_data()

def detect_intent(text):
    text = text.lower()

    if any(word in text for word in ["hi", "hello", "hey"]):
        return "greeting"

    elif any(word in text for word in ["buy", "subscribe", "interested", "want"]):
        return "high_intent"

    elif any(word in text for word in ["price", "plan", "cost"]):
        return "pricing"

 


def handle_query(user_input):
    intent = detect_intent(user_input)

    if intent == "greeting":
        return "Hi! I can help you with pricing, features, or getting started."

    elif intent == "pricing":
        return format_plans(data)

    elif intent == "general":
        return "You can ask about plans, features, or pricing."

    return None


def collect_lead():
    print("Agent: I'd love to help you get started!")

    name = input("Name: ")
    email = input("Email: ")
    platform = input("Platform (YouTube/Instagram/etc): ")

    return name, email, platform


def mock_lead_capture(name, email, platform):
    print(f"\n[Lead Captured] {name} | {email} | {platform}")