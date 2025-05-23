from openai import OpenAI
import os

secret = os.getenv("OPENAI_TEST_KEY")
if secret is None:
    raise ValueError("Please set the OPENAI_TEST_KEY environment variable.")
client = OpenAI(api_key=secret)

messages = []
# prompt to start the conversation as a quiz giver
prompt ={
    "role": "system",
    "content": """You are a quiz giver. You will ask me multiple choice questions with 5 possible answers (a,b,c,d,e) and I will answer them.
               If I answer correctly, you will give me a new question. 
               If I answer incorrectly, you will give me the correct answer and then ask me a new question."""
}
messages.append(prompt)

while True:

    # send api call
    response = client.chat.completions.create(messages=messages, model="gpt-4.1")

    # share the response
    print(response.choices[0].message.content)

    #expand the conversation 
    messages.append({
        'role': response.choices[0].message.role,
        'content': response.choices[0].message.content
    })

    # capture user input
    user_input = input('Enter your answer (enter q to quit):')

    if user_input.lower() == 'q':
        print("Exiting the program.")
        exit()

    # prompt preparation
    messages.append({"role": "user", "content": user_input})

    print(messages)