A bot that answers your questions with conspiracy theories. Project for course 67690 "Machine Learning as a Tool for Interactive Products".

The code runs the Flask server for the website, which communicates with OpenAI API to get completions from a trained module. 

See `few_shot_answers` for answer examples.


Files:
* main.py - calls the OpenAI APIs.
* app.py - opens main.py functions on a Flask server.
* conspiracyfiles.jsonl - training data for the fine-tuned algorithm.
