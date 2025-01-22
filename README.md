# InformationSystemsChatbot Readme
## Version 1.0
#### Date: January 22, 2025

#### Author: Justin Pope

## Table of Contents
- Introduction
- Features
- System Requirements
- Installation
- Getting Started
- Usage
- Troubleshooting
- Contributing
- License

## Introduction
Welcome to my InformationSystemsChatbot! This chatbot is designed to troubleshoot Windows 11 issues using OpenAI's GPT models. It offers a GUI resembling a modern chat widget and dynamic message bubbles.

The chatbot focuses exclusively on Windows 11-related problems, providing professional, concise, and tailored responses to common issues like network connectivity, printer troubleshooting, and accessing system tools.

This README will guide you through installation, setup, and usage.

## Features
- Intuitive and interactive chat interface
- Dynamic user and assistant message bubbles
- Focused on Windows 11 troubleshooting

## System Requirements
Before running the chatbot, ensure your system meets the following requirements:
- Python 3.7 or higher
- OpenAI API key
- Pip for Python package management
- A suitable IDE (recommended: VS Code or PyCharm)

## Installation
1. Clone the repository from GitHub:
```
   git clone https://github.com/yourusername/InformationSystemsChatbot.git
```

2. Change to the project directory:
```
cd InformationSystemsChatbot
```

3. Install the required dependencies using pip:
```
pip install openai python-dotenv
```

4. Create a .env file in the project directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_openai_api_key_here
```

You're now ready to use the chatbot!

## Getting Started
1. Run the chatbot script:
```
python main.py
```
2. A GUI window will open:
- Type your Windows 11 query in the input field.
- Press Enter or click "Send" to interact with the assistant.
3. The chatbot will provide responses tailored to your query.

## Usage
The chatbot specializes in resolving Windows 11-related issues. Here are some example queries:

- "How do I reset my network settings?"
- "Why is my printer not working?"
- "How do I open the Device Manager?"

If your query is outside the chatbot's scope, it will politely let you know.

## Troubleshooting
If you encounter any issues, follow these steps:
- Ensure all dependencies are installed (pip install openai python-dotenv).
- Verify that the .env file contains a valid OpenAI API key.
- Make sure you are using Python 3.7 or higher.
- If the GUI freezes, check your Python installation and confirm dependencies are properly configured.
- For errors or bugs, open an issue on the GitHub repository.

## License
This project is released under the MIT License. Feel free to use, modify, and distribute it under the terms of the license.