from openai import OpenAI
import gradio as gr
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

def respond(history, new_message):
    # add user input to the conversation
    messages.append({"role": "user", "content": new_message})

    # api call
    response = client.chat.completions.create(messages=messages, model="gpt-4.1")

    # obtain the response
    assistant_message = response.choices[0].message.content
    messages.append({
        'role': response.choices[0].message.role,
        'content': assistant_message
    })

    return history + [[new_message, assistant_message]]

with gr.Blocks() as my_bot:
    chatbot = gr.Chatbot()
    user_input= gr.Text()

    user_input.submit(respond, [chatbot, user_input], chatbot)
    user_input.submit(lambda: "", None, user_input)  # Clear the input box after submission

my_bot.launch()