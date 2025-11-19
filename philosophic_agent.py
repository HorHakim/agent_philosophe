from groq import Groq
from dotenv import load_dotenv
import random
import os
import json
load_dotenv()

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


client = Groq(api_key=os.environ["GROQ_KEY"])

def generate_philosophic_mail():

    response = client.chat.completions.create(

        messages=[
            {
                "role": "system",
                "content": read_file(file_path="context.txt")
            },
            {
                "role": "user",
                "content": read_file(file_path="prompt.txt")
            }
        ],
        temperature=0.5,
        response_format={"type": "json_object"},
        model="openai/gpt-oss-120b"
    )
    philosophic_mail = json.loads(response.choices[0].message.content)

    return philosophic_mail


if __name__ == "__main__":
    philosophic_mail = generate_philosophic_mail()
    subject = philosophic_mail["sujet"]
    message = philosophic_mail["contenu"]
    print(subject)
    print(message)