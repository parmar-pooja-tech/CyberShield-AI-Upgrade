# 🛡️ CyberShield – AI-Assisted Phishing & Cyber Threat Analyzer

CyberShield is a web-based cybersecurity tool designed to analyze suspicious messages and identify potential phishing, credential theft, malicious links, and social-engineering indicators.

The project combines **rule-based threat detection** with **Google Gemini AI** to provide threat analysis, risk assessment, and security recommendations.

---

## 🌐 Live Demo

Try the deployed CyberShield Threat Analyzer:

**Live Tool:**  
https://cybershield-threat-analyzer.onrender.com

> Note: The free cloud instance may take some time to wake up after a period of inactivity.

---

## 📌 Project Overview

Phishing and social-engineering attacks often use urgency, fake verification requests, credential-related messages, and suspicious links to trick users.

CyberShield analyzes the text of a suspicious message and provides:

- Threat status
- Risk level
- Risk score
- Threat type
- Detected indicators
- Gemini AI analysis
- Security recommendation

The project is inspired by patterns observed in a real-world phishing campaign reported by Microsoft Security.

---

## 🎯 Objectives

- Detect common phishing indicators.
- Identify social-engineering techniques.
- Detect credential-related requests.
- Identify suspicious URLs and link patterns.
- Calculate a rule-based risk score.
- Use Gemini AI for additional threat reasoning.
- Provide practical security recommendations.
- Demonstrate AI-assisted cybersecurity analysis.

---

## 🧰 Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Security
- Fernet Encryption
- Bcrypt

### Artificial Intelligence
- Google Gemini API

### Deployment & Development
- Git
- GitHub
- Render
- Visual Studio Code
- Python Virtual Environment

---

## 🔐 Security Features

CyberShield checks suspicious messages for several indicators:

### 1. Urgency and Pressure

Examples:

- Urgent
- Act now
- Immediately
- Account suspended
- Final notice

### 2. Login and Verification Requests

Examples:

- Login
- Sign in
- Verify your account
- Confirm your identity
- Account verification

### 3. Credential-Related Requests

Examples:

- Password
- Username
- Credentials
- OTP
- Security code

### 4. Suspicious Links

The application checks for URLs and known suspicious link patterns.

### 5. Social Engineering Indicators

Examples:

- Code of Conduct
- Compliance
- Policy violation
- Workforce Communications
- Internal Regulatory

---

## 🤖 AI-Assisted Analysis

CyberShield uses the **Google Gemini API** to provide additional analysis of suspicious messages.

Gemini evaluates the message for:

- Phishing
- Social engineering
- Credential theft
- Malicious links
- Account takeover attempts

The AI provides a short explanation and safety recommendation.

---

## 📊 Risk Assessment

The rule-based detection system calculates a risk score.

The application categorizes messages into:

| Risk Level | Meaning |
|---|---|
| LOW | Few or no strong threat indicators |
| MEDIUM | Some suspicious indicators detected |
| HIGH | Multiple strong threat indicators detected |

The final result can be displayed as:

- SAFE
- THREAT

---

## 🔄 System Workflow

```text
User enters suspicious message
            ↓
CyberShield Web Interface
            ↓
Secure Message Processing
            ↓
Rule-Based Threat Detection
            ↓
Risk Score & Threat Indicators
            ↓
Gemini AI Analysis
            ↓
Combined Threat Result
            ↓
Risk Level + Threat Type
            ↓
Security Recommendation
🧪 Test Result
Sample Test Message
Urgent! Your account will be suspended.
Please click here to verify your password
and login immediately.
CyberShield Result
STATUS: THREAT
RISK: HIGH
RISK SCORE: 5
Detected Threat Types
Phishing
Credential Theft
Detected Indicators
Urgency or pressure
Login / verification request
Credential-related request
AI Analysis

Gemini identified the use of artificial urgency and fear of account suspension as indicators commonly associated with credential theft.

Recommendation

Do not click suspicious links or share passwords, OTPs, or credentials. Verify the request through an official source.

📚 Real-World Case Study
Microsoft “Code of Conduct” Phishing Campaign

CyberShield was inspired by a real-world phishing campaign documented by Microsoft Security.

Incident observed: 14–16 April 2026

Publicly reported: 4 May 2026

According to Microsoft Security:

More than 35,000 users were targeted.
More than 13,000 organizations were affected.
The campaign was observed across 26 countries.
Microsoft reported that 92% of targets were in the United States.
Attack Chain
Phishing Email
      ↓
CAPTCHA / Intermediate Page
      ↓
Fake Legitimacy & Urgency
      ↓
Fake Microsoft Sign-In
      ↓
Adversary-in-the-Middle (AiTM)
      ↓
Token Theft
Project Connection

CyberShield does not reproduce the real attack and does not perform token theft.

Instead, the project uses the case study as a reference to understand and detect common phishing and social-engineering patterns such as:

Urgency
Impersonation
Fake verification
Credential requests
Social engineering
🖼️ Project Screenshots
Home Page

Threat Analysis

Case Study Reference

📁 Project Structure
CyberShield-Threat-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── templates/
│   ├── index.html
│   ├── chat.html
│   ├── login.html
│   └── register.html
│
└── screenshots/
    ├── home-1.png
    ├── threat-1.png
    ├── threat-2.png
    ├── threat-3.png
    ├── case-study-1.png
    └── case-study-2.png
💻 Run Locally
1. Clone the repository
git clone https://github.com/parmar-pooja-tech/CyberShield-Threat-Analyzer.git
2. Open the project folder
cd CyberShield-Threat-Analyzer
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Windows:

venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
6. Configure the Gemini API key

Create a .env file:

GEMINI_API_KEY=your_api_key_here

Do not upload the .env file to GitHub.

7. Run the application
python app.py
8. Open the application
http://127.0.0.1:5000
☁️ Deployment

The application is deployed using Render.

Live Application

https://cybershield-threat-analyzer.onrender.com

The Gemini API key is stored securely as an environment variable on the deployment platform and is not included in the GitHub repository.

⚠️ Limitations
The tool currently analyzes message text.
It does not directly inspect email headers.
It does not automatically verify URLs against live reputation databases.
AI analysis depends on Gemini API availability and quota.
Rule-based detection may not identify every new phishing technique.
The project is intended for educational and defensive cybersecurity purposes.
🚀 Future Enhancements

Possible future improvements include:

URL reputation checking
Email header analysis
Attachment analysis
Domain reputation checking
Machine-learning-based phishing classification
Browser extension integration
Email security integration
Threat intelligence integration
Improved phishing detection models
🔗 Project Links
🌐 Live Tool

https://cybershield-threat-analyzer.onrender.com

💻 GitHub Repository

https://github.com/parmar-pooja-tech/CyberShield-Threat-Analyzer

📖 References
Microsoft Security

Breaking the code: Multi-stage “Code of Conduct” phishing campaign leads to AiTM token compromise

https://www.microsoft.com/en-us/security/blog/2026/05/04/breaking-the-code-multi-stage-code-of-conduct-phishing-campaign-leads-to-aitm-token-compromise/

Google Gemini

Google Gemini API documentation

Flask

Flask documentation

Render

Render documentation

👩‍💻 Project Information

Project: CyberShield – AI-Assisted Phishing & Cyber Threat Analyzer

Domain: Cybersecurity & Artificial Intelligence

Purpose: Educational and defensive cybersecurity project

Developer: Pooja Parmar