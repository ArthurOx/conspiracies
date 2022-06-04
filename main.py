import openai
from config import *
from API_KEY import API_KEY

openai.api_key = API_KEY
from pathlib import Path
from flask import Flask

assumption_text = "I am a bot that believes in conspiracy theories. Everything in the world can be explained by a " \
                  "conspiracy theory. The conspiracy theories are true and I never doubt them." \
                  "The Freemasons, a secretive power elite with a globalist agenda are conspiring to eventually rule the world " \
                  "through an authoritarian one-world government."


def zero_shot(prompt: str):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"{assumption_text}\nQ: {prompt}\nA:",
        max_tokens=MAX_TOKENS,
        temperature=0.7
    )
    return response


def few_shot(prompt: str):
    txt = Path("theories").read_text()
    documents.append(txt)
    response = openai.Answer.create(
        documents=documents,
        model="davinci",
        question=prompt,
        examples=examples,
        examples_context=examples_context,
        max_tokens=MAX_TOKENS,
        temperature=0.7,
        n=1,
        return_prompt=True,
        logit_bias={"47483": -100},
        stop=["\n"]
    )
    return response


def get_assumption_with_examples():
    new_assumption = assumption_text + "\n\n"
    for example in examples:
        new_assumption += f"Q: {example[0]}\n"
        new_assumption += f"A: {example[1]}\n\n"
    return new_assumption


def few_shot_completion(prompt: str):
    assumption = get_assumption_with_examples()
    response = openai.Completion.create(
        engine="davinci:ft-hebrew-university-2022-06-04-15-27-18",
        prompt=assumption + f"Q: {prompt}\nA:",
        max_tokens=MAX_TOKENS,
        temperature=0.5,
        logit_bias={"47483": -100},
        stop=["\n", "A:"]
    )
    return response


if __name__ == "__main__":

    # resp = openai.FineTune.create(
    #     training_file="file-07K1a1wMj1y2nUkj0cVxGYX6",
    #     model = "davinci"
    #
    # )
    # resp = openai.FineTune.list()
    # print(resp)
    # ft-jnZj5wpz00OwjoXBXpULHZbE
    for i in range(0):
        question = "Is evolution real?"
        # print("Zero shot")
        # zero_shot_answer = zero_shot(question)['choices'][0]['text']
        # print(zero_shot_answer)

        print("Few shot with Completions API")
        few_shot_answer = few_shot_completion(question)['choices'][0]['text']
        print(few_shot_answer)

        # print("Few shot with Answers API")
        # few_shot_answer = few_shot(question)
        # ans = few_shot_answer["answers"][0]
        # print(ans)
