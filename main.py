from agent import handle_query, detect_intent, collect_lead, mock_lead_capture

print("AI Assistant Ready (type 'exit' to quit)\n")

lead_triggered = False

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Agent: Goodbye!")
        break

    intent = detect_intent(user_input)

    if intent == "high_intent" and not lead_triggered:
        name, email, platform = collect_lead()
        mock_lead_capture(name, email, platform)

        print("Agent: Thanks! Our team will reach out soon.")
        lead_triggered = True
        break

    response = handle_query(user_input)
    print("Agent:", response)