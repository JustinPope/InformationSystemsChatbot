from dotenv import load_dotenv
import os
import openai

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Define the system prompt
system_prompt = (
    "You are Justin's Windows 11 Assistant, a helpful and knowledgeable assistant exclusively tailored to troubleshoot "
    "Windows 11-related issues. You provide concise, clear, and detailed solutions to common problems, such as printer issues, "
    "network connectivity problems, and basic tasks like opening applications or settings. If a user asks a question outside "
    "your scope of expertise (i.e., unrelated to Windows 11), respond with: 'It appears this issue is out of scope! I am tailored "
    "to Windows 11 issues.' Always maintain a friendly and professional tone."
)

# Infinite loop for user interaction
print(f"API Key: {api_key[:5]}...")
print("Welcome to Justin's Windows 11 Assistant! Type 'exit' to quit.\n")
while True:
    # Get user input
    user_query = input("What Windows 11 issue can I help you with? (type 'exit' to quit): ")

    # Check for exit condition
    if user_query.lower() == 'exit':
        print("Goodbye! If you have more Windows 11 issues, feel free to ask again.")
        break

    try:
        # Use the new OpenAI ChatCompletion interface
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Use GPT-4 or GPT-4o-mini
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            temperature=0.2,  # Low randomness for consistent answers
            max_tokens=200  # Adjust for detailed yet concise answers
        )

        # Extract and display the assistant's response
        assistant_reply = response.choices[0].message.content
        print(f"\nJustin's Windows 11 Assistant: {assistant_reply}\n")

    except Exception as e:
        # Handle API errors and display the actual exception
        print(f"\nSorry, I encountered an issue processing your request. Error details: {e}\n")
