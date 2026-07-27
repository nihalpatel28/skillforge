# 🎯 SkillForge - Phishing Awareness Demonstration

> **Educational Cybersecurity Project using Flask & AWS EC2**

---

# 📖 Overview

SkillForge is an educational cybersecurity project that demonstrates how phishing websites can imitate legitimate login pages to collect user-submitted credentials in a controlled laboratory environment.

The purpose of this project is to help students, cybersecurity enthusiasts, and researchers understand how phishing attacks operate and how users can protect themselves against such attacks.

> **Disclaimer:** This project is created solely for educational, research, and cybersecurity awareness purposes. It must only be used in authorized lab environments and never against real users or systems.

---

# 🚀 Features

- Phishing login page simulation
- Flask web application
- HTML/CSS frontend
- User credential capture demonstration
- Local credential storage for educational analysis
- AWS EC2 deployment
- Git version control
- GitHub repository

---

# 🛠 Technologies Used

- Python 3
- Flask
- HTML5
- CSS3
- JavaScript
- AWS EC2
- Amazon Linux 2023
- Git
- GitHub

---

# 📦 Deployment on AWS EC2

## Step 1: Launch EC2 Instance

Launch an **Amazon Linux 2023** EC2 instance.

Allow the following inbound rules:

| Type | Port |
|------|------|
| SSH | 22 |
| HTTP | 80 |
| HTTPS | 443 |
| Custom TCP | 5000 |

---

## Step 2: Connect to EC2

```bash
ssh -i your-key.pem ec2-user@YOUR_PUBLIC_IP
```

---

## Step 3: Update the Server

```bash
sudo dnf update -y
```

---

## Step 4: Install Git

```bash
sudo dnf install git -y
```

Verify installation

```bash
git --version
```

---

## Step 5: Clone Repository

```bash
git clone https://github.com/nihalpatel28/skillforge.git
```

Move into project directory

```bash
cd skillforge
```

---

## Step 6: Install Python & Pip

```bash
sudo dnf install python3 python3-pip -y
```

Verify

```bash
python3 --version
pip3 --version
```

---

## Step 7: Create Virtual Environment

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

---

## Step 8: Install Flask

```bash
pip install flask
```

Or install dependencies

```bash
pip install -r requirements.txt
```

---

## Step 9: Run Application

```bash
python3 app.py
```

Application runs on

```
http://YOUR_PUBLIC_IP:5000
```

---

# 📂 Project Structure

```
skillforge/
│
├── app.py
├── templates/
├── static/
├── users.txt
├── requirements.txt
├── README.md
└── venv/
```

---

# 🎯 Project Usage

This project demonstrates how phishing attacks can imitate legitimate login pages in a controlled environment.

### Demonstration Workflow

1. The victim opens the phishing webpage.
2. A login page similar to a legitimate website is displayed.
3. The victim enters email and password.
4. Flask receives the submitted information.
5. The application stores the submitted information locally.
6. The attacker (demonstration only) can view the collected information.
7. The demonstration highlights why users should always verify URLs and website authenticity before entering credentials.

---

# 🔍 Demonstration Output

The project stores submitted credentials inside

```
users.txt
```

Example

```
Email : demo@example.com

Password : Password123

Time : 28-07-2026 09:45 PM

IP Address : 192.168.1.25
```

---

# 📷 Demonstration Images

## Login Page

```
(Add Screenshot Here)
```

Example

```
images/login-page.png
```

---

## Captured Credentials

```
(Add Screenshot Here)
```

Example

```
images/captured-credentials.png
```

---

# ⚠ Security Awareness

This project demonstrates why phishing attacks are successful.

Users should always:

- Verify website URLs.
- Look for HTTPS certificates.
- Avoid entering credentials on unknown websites.
- Enable Multi-Factor Authentication (MFA).
- Be cautious of suspicious emails and links.

---

# 📚 Educational Purpose

This project helps learners understand:

- Social Engineering
- Credential Harvesting
- Phishing Websites
- Flask Development
- AWS EC2 Deployment
- Web Application Deployment
- Cybersecurity Awareness

---

# ⚖ Disclaimer

This repository is intended **only for educational purposes, cybersecurity research, and awareness training**.

The author does **not** encourage, promote, or support unauthorized phishing, credential theft, or any illegal activity.

Use this project only in controlled laboratory environments or with explicit authorization.

---

# 👨‍💻 Author

**Nihal Patel**

GitHub: https://github.com/nihalpatel28
