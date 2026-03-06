from django.conf import settings

def check_secret_key():

    check_id = "SEC003"
    name = "Secret Key"
    severity = "HIGH"
    description = "Secret key should be set in production and should be a strong random value"

    secret_key = settings.SECRET_KEY
    debug_mode = settings.DEBUG

    if debug_mode:
        status = "SKIPPED"
        solution = None

    elif not secret_key:
        status = "FAIL"
        solution = "Set SECRET_KEY to a strong random value"

    elif "django-insecure" in secret_key:
        status = "FAIL"
        solution = "Replace the default Django insecure secret key"

    elif len(secret_key) < 50:
        status = "FAIL"
        solution = "Use a longer and stronger SECRET_KEY"

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