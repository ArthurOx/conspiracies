import openai
from config import *
from API_KEY import API_KEY
openai.api_key = API_KEY


def zero_shot(prompt: str):
    assumption_text = "Always give an answer based on a popular conspiracy theory. Suppose the conspiracy theory is a fact."
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{assumption_text}\nQ: {prompt}\nA:",
        max_tokens=MAX_TOKENS,
        temperature=0.7
    )
    return response


def few_shot(prompt: str):
    response = openai.Answer.create(
        documents=documents,
        model="davinci",
        question="Can you prove that the earth is flat?",
        examples=examples,
        examples_context=examples_context,
        max_tokens=MAX_TOKENS
    )
    return response


if __name__ == "__main__":
    question = input("Ask anything. ")
    print(zero_shot(question))
