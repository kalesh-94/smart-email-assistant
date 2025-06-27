
from datetime import datetime


class EscalationAgent:
    def __init__(self, log_file="escalation_log.txt"):
        self.log_file = log_file

    def escalate(self, email_text, category, confidence):
        if not email_text:
            raise ValueError("Email text cannot be empty.")

        log_message = (
            f"{datetime.now()} | Escalated Email: {email_text} "
            f"| Category: {category} | Confidence: {confidence}\n"
        )

        try:
            with open(self.log_file, "a") as file:
                file.write(log_message)
        except Exception as e:
            print(f"Failed to write to log: {e}")

        return {
            "status": "escalated",
            "reason": "Low confidence or category 'Other'",
            "logged_to": self.log_file
        }
