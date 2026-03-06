![Security Report](docs/frame.png)

# AbyssionFramework

AbyssionFramework v1.0.0 is a lightweight security scanner for Django applications.

It helps developers detect common security misconfigurations before deploying to production.

---

## Features

- Automatic Django project detection
- 10+ security checks
- Terminal security report
- JSON export for automation
- Lightweight and easy to run

---

## Installation

Clone the repository:

git clone https://github.com/Lezaey/Abyssion-Framework.git

Install dependencies:

pip install -r requirements.txt

---

## Usage

Run the scanner inside your Django project directory:

python abyssionframework/runner.py

---

## Example Output

SEC001 | Debug Mode Enabled | FAIL | CRITICAL
SEC002 | Allowed Hosts | PASS | CRITICAL
SEC003 | Secret Key | FAIL | HIGH

---

## JSON Report

A JSON security report will be generated:

security_report.json

---

## Security Checks

SEC001 — Debug Mode Enabled  
SEC002 — Allowed Hosts  
SEC003 — Secret Key Strength  
SEC004 — SSL Redirect  
SEC005 — Session Cookie Secure  
SEC006 — CSRF Cookie Secure  
SEC007 — HSTS Header  
SEC008 — X-Frame-Options  
SEC009 — Content-Type Nosniff  
SEC010 — Dangerous File Upload  
SEC011 — Referrer Policy  

WEB001 — SVG Upload Risk

---

## License


MIT


