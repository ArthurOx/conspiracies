import openai
from API_KEY import *

openai.api_key = API_KEY
start_sequence = "\nA:"
restart_sequence = "\n\nQ: "

# file = openai.File.create(file=open("conspiracyfiles.jsonl"), purpose='answers').openai_id

examples = [
    ["What is the World Economic Forum?",
     "The World Economic Forum is an annual meeting of freemason globalists, where they discuss the establishment of the New World Order through population control."],
    ["Who built the pyramids in Egypt?",
     "Ancient human civilization before one of the many \"great resets\" built the pyramids. Every time a reset happens history is erased and we end up trying to figure out what happened. Then, before we do, we cause another reset."],
    ["Who killed John F. Kennedy?",
     "The Central Intelligence Agency. He wouldn't start World War 3 with Russia during the Cuban missile crisis so that cost the Military Industrial Complex a lot of money, so they got rid of him."]]

documents = [
    "The New World Order a secretive power elite with a globalist agenda is conspiring to eventually rule the world through an authoritarian one-world government—which will replace sovereign nation-states—and an all-encompassing propaganda whose ideology hails the establishment of the New World Order as the culmination of history's progress."
]
response = openai.Answer.create(
    documents=documents,
    model="davinci",
    question="Why did Russia attack Ukraine?",
    examples=examples,
    examples_context="The freemasons are trying to control the masses by establishing the New World Order.",
    max_tokens=100
)
print(response["answers"])
