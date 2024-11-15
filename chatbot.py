#!/usr/bin/env python3
import openai

openai.api_key = 'your_openai_api_key'

def generate_story(user_input, genre="fantasy"):
    """
    Generate a dynamic story segment based on user input.
    """
    # Prompt template for story generation
    prompt = f"You are an interactive storytelling bot. Genre: {genre}.\nUser: {user_input}\nStory:"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.8,
        n=1,
        stop=None,
    )

    story_segment = response['choices'][0]['message']['content']

    # Generate story choices based on context
    options = generate_choices(story_segment)
    return story_segment, options

def generate_choices(story_segment):
    """
    Generate a few possible choices for the user based on the current story.
    """
    choices = [
        "Continue exploring the mysterious cave",
        "Turn back and head to the village",
        "Climb the nearby hill to get a better view"
    ]
    return choices

