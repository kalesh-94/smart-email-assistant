import google.generativeai as genai
from dotenv import load_dotenv
import os


# Load .env variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")



class ResponseGenerator:
    def __init__(self):
        
        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def generate_response(self, email_text, category):
        if not email_text or not category:
            raise ValueError("Both email_text and category are required.")

        prompt = (
            f"You are an AI Email Assistant.\n"
            f"Email Category: {category}\n"
            f"Email Content: {email_text}\n"
            f"Write a polite, professional reply for this email."
        )

        try:
            response = self.model.generate_content(prompt)
            return response.text.strip()
        except Exception as e:
            return f"Error generating response: {e}"
