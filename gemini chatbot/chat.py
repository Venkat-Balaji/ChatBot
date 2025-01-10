

# Import necessary libraries
import google.generativeai as genai
import os

# Set your Gemini API key
my_api_key_gemini = 'YOUR API KEY'  # Replace with your actual API key

# Configure the generative AI API
genai.configure(api_key=my_api_key_gemini)

# Function to generate a response from Gemini
def ask_gemini(question):
    try:
        # Use the generative model to generate content
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(question)

        # Check if there's valid text in the response
        if response.text:
            return response.text
        else:
            return "Sorry, but I think Gemini didn't want to answer that!"
    except Exception as e:
        # Handle any exceptions (like invalid API key, network issues, etc.)
        return f"An error occurred: {str(e)}"

# Interactive input/output loop in Colab
print("Welcome to the Gemini Chatbot! Type 'quit' to exit.")
while True:
    prompt = input("You: ")
    if prompt.lower() == 'quit':
        print("Goodbye!")
        break

    # Get the response from Gemini and print it
    reply = ask_gemini(prompt)
    print(f"AI: {reply}")

