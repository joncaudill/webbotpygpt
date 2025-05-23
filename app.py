from openai import OpenAI
import os

secret = os.getenv("OPENAI_TEST_KEY")
if secret is None:
    raise ValueError("Please set the OPENAI_TEST_KEY environment variable.")
client = OpenAI(api_key=secret)

messages = []

while True:
    # capture user input
    user_input = input('Enter your prompt (enter q to quit):')

    if user_input.lower() == 'q':
        print("Exiting the program.")
        exit()

    # prompt preparation
    messages.append({"role": "user", "content": user_input})

    # send api call
    response = client.chat.completions.create(messages=messages, model="gpt-4.1")

    # share the response
    print(response.choices[0].message.content)

    #expand the conversation 
    messages.append({
        'role': response.choices[0].message.role,
        'content': response.choices[0].message.content
    })

    print(messages)