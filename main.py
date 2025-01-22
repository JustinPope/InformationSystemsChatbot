from dotenv import load_dotenv
import os
import openai
import tkinter as tk
from tkinter import ttk, scrolledtext

# Load environment variables from the .env file
load_dotenv()

# Access the API key
api_key = os.getenv("OPENAI_API_KEY")
openai.api_key = api_key

# Check to see if the .env file is configured properly
if not api_key:
    print("Error: API key not found. Make sure your .env file is correctly configured.")
    exit(1)

# Define the system prompt
system_prompt = (
    "You are Justin's Windows 11 Assistant, a helpful and knowledgeable assistant exclusively tailored to troubleshoot "
    "Windows 11-related issues. You provide concise, clear, and detailed solutions to common problems, such as printer issues, "
    "network connectivity problems, and basic tasks like opening applications or settings. If a user asks a question outside "
    "your scope of expertise (i.e., unrelated to Windows 11), respond with: 'It appears this issue is out of scope! I am tailored "
    "to Windows 11 issues.' Always maintain a friendly and professional tone."
)

# Function to handle user queries
def get_response(event=None):
    user_query = user_input.get().strip()
    if not user_query:
        display_message("Please enter a valid query.", "system")
        return
    
    display_message(user_query, "user")  # Display the query
    user_input.delete(0, tk.END)  # Clear the field

    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",  # Use GPT-4 or GPT-4o-mini
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ],
            temperature=0.2,  # Low randomness for consistent answers
            max_tokens=200  # Adjust for detailed yet concise answers
        )
        assistant_reply = response.choices[0].message.content
        display_message(assistant_reply, "assistant")  # Display the assistant's reply
    except Exception as e:
        display_message(f"Error: {e}", "system")  # Handle errors gracefully


# Function to display messages in the chat area
def display_message(message, sender):
    # Frame for the message
    frame = tk.Frame(chat_area, bg="#f5f5f5", pady=5, padx=5)

    # Determine alignment and colors based on sender
    if sender == "user":
        anchor = "e"
        bubble_color = "#e2e3e5"  # Light gray for user
    elif sender == "assistant":
        anchor = "w"
        bubble_color = "#d1e7dd"  # Light green for assistant
    else:  # System messages
        anchor = "w"
        bubble_color = "#f8d7da"  # Light red for system errors

    # Create the message bubble
    bubble = tk.Label(
        frame,
        text=message,
        wraplength=400,
        justify="left",
        bg=bubble_color,
        fg="black",
        font=("Arial", 10),
        padx=10,
        pady=5,
        relief="solid",
        bd=1
    )
    bubble.pack(side="right" if sender == "user" else "left", padx=5)

    # Add the frame to the chat area
    frame.pack(anchor=anchor, fill="x", padx=10, pady=2)

    # Auto-scroll to the bottom
    chat_canvas.update_idletasks()
    chat_canvas.yview_moveto(1.0)

# Initialize the GUI
root = tk.Tk()
root.title("Justin's Windows 11 Assistant")
root.geometry("500x600")
root.resizable(False, False)

# Chat area frame
chat_frame = tk.Frame(root, bg="#f5f5f5", relief="solid", bd=1)
chat_frame.pack(fill="both", expand=True, padx=10, pady=10)

# Scrollable canvas for chat messages
chat_canvas = tk.Canvas(chat_frame, bg="#f5f5f5")
chat_scroll = ttk.Scrollbar(chat_frame, orient="vertical", command=chat_canvas.yview)
chat_area = tk.Frame(chat_canvas, bg="#f5f5f5")

# Configure scrollable chat area
chat_area.bind("<Configure>", lambda e: chat_canvas.configure(scrollregion=chat_canvas.bbox("all")))
chat_canvas.create_window((0, 0), window=chat_area, anchor="nw")
chat_canvas.configure(yscrollcommand=chat_scroll.set)

chat_canvas.pack(side="left", fill="both", expand=True)
chat_scroll.pack(side="right", fill="y")

# Input area frame
input_frame = tk.Frame(root, bg="#f5f5f5", pady=5)
input_frame.pack(fill="x", padx=10, pady=5)

# Input box
user_input = tk.Entry(input_frame, font=("Arial", 12), relief="solid", bd=1)
user_input.pack(side="left", fill="x", expand=True, padx=(0, 10))
user_input.bind("<Return>", get_response)  # Bind Enter key to submit

# Send button
send_btn = tk.Button(
    input_frame,
    text="Send",
    command=get_response,
    font=("Arial", 10),
    bg="#007bff",
    fg="white",
    relief="solid",
    bd=1
)
send_btn.pack(side="right")

# Run the GUI
root.mainloop()