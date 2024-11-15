#!/usr/bin/env python3
from flask import Flask, render_template, request, jsonify
from chatbot import generate_story

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form.get('user_input')
    story_segment, options = generate_story(user_input)
    return jsonify(story=story_segment, options=options)

if __name__ == "__main__":
    app.run(debug=True)

