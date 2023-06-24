import argparse
import constants
import openai
from os import system

openai.api_key = constants.openai_api_key

arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('-s', '--style', help='Optional style in which ChatGPT should give its responses')
arg_parser.add_argument('-v', '--speak', action='store_true')
args = arg_parser.parse_args()

do_speak = args.speak

style = "You are an intelligent assistant"
if (args.style):
    style = "You are an intelligent assistant in the style of %s" % args.style

messages = [
 {"role": "system", "content" : style}
]

while True:
    content = input("User: ")
    if content == "dump":
        for message in messages:
            print(message)
    else:
        messages.append({"role": "user", "content": content})
        
        completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
        )

        chat_response = completion.choices[0].message.content
        print(f'ChatGPT: {chat_response}')
        messages.append({"role": "assistant", "content": chat_response})
        if do_speak:
            system("say -r 300 \"%s\"" % chat_response)