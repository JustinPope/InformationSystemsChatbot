from dotenv import load_dotenv
import os
import openai

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key