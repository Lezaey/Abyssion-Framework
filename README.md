<p align="center">
  <img src="docs/frame.png" width="650">
</p>

<h1 align="center">AbyssionFramework</h1>

<p align="center">
Lightweight security scanner for Django applications
</p>

---

## Overview

**Abyssion Framework v1.0.0** is a lightweight security scanner designed for **Django applications**.

It helps developers quickly identify **security misconfigurations and risky settings** before deploying applications to production environments.

The framework focuses on **simplicity, speed, and useful security insights** without requiring complex setup.

---

## Features

* Automatic Django project detection
* 10+ built-in security checks
* Clean terminal security report
* JSON export for automation and pipelines
* Lightweight and fast execution

---

## Installation

Clone the repository:

```
git clone https://github.com/Lezaey/Abyssion-Framework.git
```

Navigate into the project:

```
cd Abyssion-Framework
```

Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

Run the scanner inside your **Django project directory**:

```
python abyssionframework/runner.py
```

The framework will automatically detect the Django configuration and run the security checks.

---

## Example Output

```
SEC001 | Debug Mode Enabled | FAIL | CRITICAL
SEC002 | Allowed Hosts | PASS | CRITICAL
SEC003 | Secret Key | FAIL | HIGH
```

---

## JSON Report

A machine-readable report will also be generated:

```
security_report.json
```

This allows integration with:

* CI/CD pipelines
* Security automation
* Monitoring tools

---

## Security Checks

### Core Security

```
SEC001 — Debug Mode Enabled
SEC002 — Allowed Hosts
SEC003 — Secret Key Strength
SEC004 — SSL Redirect
SEC005 — Session Cookie Secure
SEC006 — CSRF Cookie Secure
```

### Security Headers

```
SEC007 — HSTS Header
SEC008 — X-Frame-Options
SEC009 — Content-Type Nosniff
SEC011 — Referrer Policy
```

### Upload Security

```
SEC010 — Dangerous File Upload
WEB001 — SVG Upload Risk
```

---

## License

This project is licensed under the **MIT License**.
