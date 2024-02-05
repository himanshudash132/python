


import os
from openai import OpenAI
client = OpenAI()
# Set your OpenAI API key
OpenAI.api_key = os.environ["OPENAI_API_KEY"] 

def search_word_information(word):
    # Define your prompt or question
    prompt = f"Search information about {word}"

    # Make a request to the OpenAI API with GPT-3.5-turbo engine
    response =  client.completions.create(
         model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=150,  # Adjust as needed
        n=1,  # Number of completions
        stop=None,  # You can add custom stop words if needed
        temperature=0.7,  # Adjust temperature for creativity vs. accuracy
    )

    # Extract and print the generated text
    generated_text = response.choices[0].text
    
    print(generated_text)

# Example usage
search_word_information("Rajeev Kumar databricks Molina healthcare")