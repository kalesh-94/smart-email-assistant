from flask import Flask, request, jsonify, render_template,redirect, url_for
from agents.response_generator import ResponseGenerator
from agents.escalation_agent import EscalationAgent
from agents.email_classifier import EmailClassifier
import os


# init flask app
app = Flask(__name__)


#  Agents
classifier = EmailClassifier()  
generator = ResponseGenerator()
escalator = EscalationAgent()


#  Home 
@app.route('/')
def home():
    return render_template('index.html')


#  Process  Route
@app.route('/process', methods=['POST'])
def process_email():
    email_text = request.form.get('email_text')

    if not email_text:
        return jsonify({'error': 'No email text provided'}), 400

    #  1: Classification
    category, confidence = classifier.classify(email_text)

    if category == "Invalid":
        output = {
            "email_text": email_text,
            "status": "Invalid Email",
            "reason": "The input does not look like a valid email. Please write a meaningful sentence."
        }
        return render_template('result.html', result=output)

    #  2: Decision 
    if confidence >= classifier.confidence_threshold and category != "Other":
        response = generator.generate_response(email_text, category)
        output = {
            "email_text": email_text,
            "predicted_category": category,
            "confidence": confidence,
            "response": response
        }
    else:
        escalation = escalator.escalate(email_text, category, confidence)
        output = {
            "email_text": email_text,
            "predicted_category": category,
            "confidence": confidence,
            **escalation
        }

    return render_template('result.html', result=output)


# ---------- Escalation Log Page ----------
@app.route('/escalation-log')
def show_escalation_log():
    try:
        with open("escalation_log.txt", "r") as file:
            logs = file.readlines()
    except FileNotFoundError:
        logs = []

    # Parse log lines
    parsed_logs = []
    for line in logs:
        try:
            timestamp, rest = line.split('|', 1)
            email_text, rest2 = rest.strip().split('| Category:', 1)
            category, confidence_part = rest2.strip().split('| Confidence:')
            parsed_logs.append({
                "timestamp": timestamp.strip(),
                "email_text": email_text.replace('Escalated Email:', '').strip(),
                "category": category.strip(),
                "confidence": confidence_part.strip()
            })
        except:
            continue

    return render_template('escalation_log.html', logs=parsed_logs, full_log_text="".join(logs))


# ---------- Clear Logs ----------
@app.route('/clear-log')
def clear_log():
    open("escalation_log.txt", "w").close()
    return redirect(url_for('show_escalation_log'))



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
