import openai

# Put your 
   import os
   from openai import OpenAI
   client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
def chat():
    print("AI Chatbot - Type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        print("Bot:", response.choices[0].message.content)

if __name__ == "__main__":
    chat()
