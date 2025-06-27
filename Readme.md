
# 💌 Smart Email Assistant

A web-based tool designed to classify company emails into categories (**HR**, **IT**, or **Other**) and generate professional responses using **Google Gemini AI**.  

This project automates the process of identifying the type of email and replying with relevant, polite, and context-aware responses.

---

## 🚀 Features

- ✅ Classifies emails into `HR`, `IT`, or `Other` using a trained ML model.
- ✅ Provides a **confidence score** for each classification.
- ✅ Generates polite, professional replies using **Gemini Pro**.
- ✅ Automatically **escalates low-confidence or ambiguous emails** to a log file for manual review.
- ✅ Simple, clean user interface built with **HTML + CSS**.
- ✅ Fully modular, agent-based architecture.

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Scikit-learn (Machine Learning Model)
- Google Generative AI (`google-generativeai`)
- HTML5 / CSS3

---

## ⚙️ Getting Started

### 🔧 Prerequisites

- Python `3.7` or higher  
- A **Google API Key** for Gemini (get it from → [https://console.cloud.google.com/apis/credentials?project=gen-lang-client-0024551153&pli=1&inv=1&invt=Ab1N_A](https://makersuite.google.com/app))

---

### 📥 Installation Steps

1️⃣ Clone the repository or download the ZIP.  
```
cd smart-email-assistant
```

2️⃣ (Optional) Create a virtual environment:  
```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

3️⃣ Install all dependencies:  
```bash
pip install -r requirements.txt
```

4️⃣ Set your Gemini API Key:  

Open the file:  
```plaintext
agents/response_generator.py
```

Find this line and add your key:  
```python
genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

5️⃣ Ensure that the ML model and vectorizer exist in the models folder:  
- `models/model.pkl` → Trained classification model  
- `models/vectorizer.pkl` → TF-IDF vectorizer  

---

### ▶️ Running the App

Start the Flask app:  
```bash
python app.py
```

Then open your browser and go to:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 💻 App Usage

- Input an email message in the text box.
- Click **Submit**.
- The app will return:
  - ✅ **Predicted Category:** HR, IT, or Other
  - ✅ **Confidence Score**
  - ✅ **Generated AI Response**

### 🔔 **Escalation:**  
- If the confidence is **below 0.6** or the category is **Other**, the email is logged in `escalation_log.txt` for manual review.

---

## ✉️ Example

### ➕ **Input:**  
```plaintext
Hi HR, I have updated my bank details. Can you please let me know the steps to update my salary account?
```

### ➖ **Output:**  
```plaintext
Predicted Category: HR
Confidence: 0.94
Generated Response: Dear Employee, thank you for updating your bank details. Kindly contact the HR department or follow the internal portal instructions to update your salary account. Let us know if you need further assistance.
```

---

## 📂 Folder Structure

```
smart-email-assistant/
├── agents/
│   ├── email_classifier.py         # ML Classification Agent
│   ├── response_generator.py        # Gemini Response Generator
│   └── escalation_agent.py          # Escalation Handler
├── models/
│   ├── model.pkl                    # Trained ML model
│   └── vectorizer.pkl               # TF-IDF Vectorizer
├── templates/
│   ├── index.html                   # Input UI
│   └── result.html                  # Output UI
├── escalation_log.txt               # Log file for escalated emails
├── app.py                           # Flask app orchestrator
├── requirements.txt                 # Dependencies
└── README.md                        # Documentation
```

---

## 🌍 Deployment (Optional Bonus)

This project can be deployed to:

- AWS EC2 / Lambda  
- Render.com / Railway  
- Docker Container  

---

## 🔥 Author

**Kalesh Patil**  
AI/ML Engineer | Applicant at **Newel Technologies Pvt. Ltd.**  
💡 Passionate about AI, ML, Generative AI, and Intelligent Agent Systems.

---

## 📜 License

This project is for educational and demonstration purposes.

---
 
