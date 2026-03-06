from django.conf import settings

def check_secure_hsts_seconds():
    check_id = "SEC007"
    name = "Secure HSTS Seconds"
    severity = "HIGH"
    description = "Secure HSTS seconds should be enabled in production"
    
    hsts_seconds = getattr(settings, "SECURE_HSTS_SECONDS", 0)

    if hsts_seconds <= 0:
        status = "FAIL"
        solution = "Set SECURE_HSTS_SECONDS to a positive value"

    elif hsts_seconds < 31536000:
        status = "FAIL"
        solution = "Set SECURE_HSTS_SECONDS to 31536000"
    
    else:
        status = "PASS"
        solution = None
    
    return {
        "id": check_id,
        "name": name,
        "status": status,
        "severity": severity,
        "description": description,
        "solution": solution
    }
