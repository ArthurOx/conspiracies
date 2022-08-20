A bot that answers your questions with conspiracy theories. The code runs the Flask server for the website, which communicates with OpenAI API to get completions from a trained module.


Files:
* main.py - calls the OpenAI APIs.
* app.py - opens main.py functions on a Flask server.
* conspiracyfiles.jsonl - training data for the fine-tuned algorithm.
