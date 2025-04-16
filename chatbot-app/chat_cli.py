import requests

def chat():
    print("Welcome to the ChatBot! Type 'exit' or 'quit' to leave.")
    while True:
        question = input("You: ")
        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        try:
            # Add a timeout to the request
            response = requests.post("http://127.0.0.1:5000/ask", json={"question": question}, timeout=5)

            # Check if the response is OK
            if not response.ok:
                print("❌ Error:", response.status_code, response.text)
                continue

            # Parse the response JSON
            try:
                answer = response.json().get("answer")
                if answer:
                    print("Bot:", answer)
                else:
                    print("⚠️ No answer found in the response.")
            except ValueError as e:
                print("⚠️ Failed to parse JSON:", e)
                print("Raw response:", response.text)

        except requests.exceptions.RequestException as e:
            print("❌ Failed to connect to the server:", e)

if __name__ == "__main__":
    chat()
