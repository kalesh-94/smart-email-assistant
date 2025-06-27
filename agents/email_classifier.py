import google.generativeai as genai
import json
import re
from dotenv import load_dotenv
import os


# Load .env variables
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

class EmailClassifier:
    def __init__(self):
        print("Loaded model.pkl and vectorizer.pkl successfully .")
        self.confidence_threshold = 0.6
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    def is_valid_email_text(self, text):
        if not text or len(text.strip()) < 10:
            return False
        words = text.split()
        meaningful = [w for w in words if w.isalpha()]
        return len(meaningful) >= 3

    def classify(self, email_text):
        if not self.is_valid_email_text(email_text):
            return "Invalid", 0.0

        prompt = f"""
You are an email classification AI.

Classify the following email strictly into one of these categories:
- HR
- IT
- Other

Return your response strictly in JSON only. Do NOT add extra text.

Example Format:
{{
  "category": "HR",
  "confidence": 0.89
}}
If confidence ≥ 0.6 **and** category ≠ "Other" → Response Generator Agent.
Else → Escalation Agent.
Return generated response or escalation status

Email:
\"\"\"{email_text}\"\"\"

ONLY output the JSON. Nothing else.
"""

        try:
            response = self.model.generate_content(prompt)
            output = response.text.strip()

            
            json_match = re.search(r'\{.*\}', output, re.DOTALL)
            if json_match:
                json_data = json.loads(json_match.group())
                category = json_data.get("category", "Other")
                confidence = float(json_data.get("confidence", 0.0))
                if category not in ["HR", "IT", "Other"]:
                    category = "Other"
                return category.strip(), round(confidence, 2)
            else:
                print(f" JSON parsing failed. Raw output:\n{output}")
                return "Other", 0.0

        except Exception as e:
            print(f"  Error: {e}")
            return "Other", 0.0
