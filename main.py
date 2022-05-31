import openai
from config import *
from API_KEY import API_KEY
openai.api_key = API_KEY


def zero_shot(prompt: str):
    assumption_text = "Always give an answer based on a popular conspiracy theory with an assumption that the theory is an actual fact."
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
        question=prompt,
        examples=examples,
        examples_context=examples_context,
        max_tokens=MAX_TOKENS,
        temperature=0.7,
        n=1,
        return_prompt=True
    )
    return response


if __name__ == "__main__":
    for i in range(1):
        question = "Why did the eagles not just fly Frodo to Mordor?"
        print("Zero shot")
        zero_shot_answer = zero_shot(question)['choices'][0]['text']
        print(zero_shot_answer)
        print("Few shot")
        few_shot_answer = few_shot(question)
        print(few_shot_answer["answers"])