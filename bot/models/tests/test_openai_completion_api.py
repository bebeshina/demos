import io
import json

from openai import OpenAI
import nltk


nltk.download('punkt')
OPENAI_API_KEY = "KEY"

client = OpenAI(api_key=OPENAI_API_KEY)


def completion_test(text):
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "Vous êtes un assistant automobile. Soyez bref."},
        {"role": "assistant", "content": "%s" % text}
      ]
    )
    print(completion.choices[0].message)


def generate_qa_pairs():
    text = io.open("knowledge.txt", "r", encoding="utf-8").read()
    sentences = nltk.sent_tokenize(text)
    f = open("generation_test.txt", "w+", encoding="utf-8")
    for sentence in sentences[:50]:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Vous êtes un utilisateur automobile. Posez des questions. Vous faites des fautes de frappe."},
                {"role": "assistant",
                 "content": "%s" % sentence}
            ]
        )
        print("%s :::::::::: %s\n" % (sentence, completion.choices[0].message.content))




