# README.md

````markdown
# 🔐 Secure Coding Review Platform

Secure Coding Review Platform is a full-stack Flask-based cybersecurity application that analyzes uploaded source code files to detect common security vulnerabilities.
The project helps developers identify insecure coding practices and provides remediation recommendations for building secure applications.

An advanced full-stack cybersecurity web application developed using Flask, HTML, CSS, and JavaScript for performing secure coding reviews and vulnerability analysis.

The platform allows users to upload source code files and automatically detects common security vulnerabilities such as:

- eval() usage
- exec() usage
- Hardcoded passwords
- SQL Injection
- Command Injection
- Weak Cryptography
- Cross Site Scripting (XSS)

---

# 🚀 Features

## ✅ User Features

- Upload source code files
- Automatic vulnerability detection
- Security analysis reports
- Severity-based vulnerability classification
- Secure coding recommendations
- Interactive web interface

---

# 🛡️ Vulnerabilities Detected

| Vulnerability | Severity |
|---|---|
| eval() Usage | High |
| exec() Usage | Critical |
| Hardcoded Passwords | High |
| SQL Injection | Critical |
| Command Injection | Critical |
| Weak Cryptography (MD5) | Medium |
| Cross Site Scripting (XSS) | High |

---

# 🏗️ Tech Stack

## Backend
- Python
- Flask

## Frontend
- HTML5
- CSS3
- JavaScript

## Security Concepts
- Static Code Analysis
- Vulnerability Scanning
- Secure Coding Practices

---

# 📂 Project Structure

```bash
secure-coding-review/
│
├── app.py
│
├── templates/
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── upload.html
│   └── results.html
│
├── static/
│   └── uploads/
│
├── test.py
│
└── README.md
````

---

# ⚙️ Installation

## Step 1: Clone Repository

```bash
git clone https://github.com/your-username/secure-coding-review.git
```

---

## Step 2: Navigate to Project

```bash
cd secure-coding-review
```

---

## Step 3: Install Flask

```bash
pip install flask
```

---

## Step 4: Run Application

```bash
python app.py
```

---

# 🌐 Application URL

```text
http://127.0.0.1:5000
```

---

# 📤 Upload Vulnerable Files

Upload vulnerable source code files such as:

* Python files (.py)
* JavaScript files (.js)
* PHP files (.php)

---

# 🧪 Example Vulnerable File

## test.py

```python
password="admin"

eval("print('unsafe')")
```

---

# 📊 Output Example

| Issue              | Severity | Recommendation            |
| ------------------ | -------- | ------------------------- |
| Use of eval()      | High     | Avoid using eval()        |
| Hardcoded Password | High     | Use environment variables |

---

# 🔒 Security Recommendations

* Avoid dynamic code execution
* Use parameterized SQL queries
* Sanitize user input
* Store credentials securely
* Use strong cryptographic algorithms
* Validate uploaded files

---

# 🚀 Future Enhancements

* AI-based vulnerability detection
* PDF report generation
* User authentication system
* Database integration
* Real-time threat analysis
* GitHub repository scanning
* OWASP Top 10 coverage
* Machine learning risk prediction
* 
# 🎯 Learning Objectives

This project helps understand:

* Secure coding principles
* Static code analysis
* Web application security
* Flask development
* Vulnerability assessment
* Cybersecurity best practices
# 📜 License

This project is for educational and learning purposes only.
The Secure Coding Review Platform successfully demonstrates how static code analysis can be used to identify common software security vulnerabilities in source code files. The system provides an interactive environment for uploading files, detecting insecure coding practices, and generating security recommendations to improve application safety.
#Conclusion

This project enhances understanding of secure coding principles, Flask web development, vulnerability assessment, and cybersecurity best practices. It also serves as a foundation for future improvements such as AI-based detection, database integration, real-time threat monitoring, and advanced OWASP vulnerability analysis.
