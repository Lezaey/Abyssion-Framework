from django.conf import settings

def check_allowed_hosts():
    check_id = "SEC002"
    name = "Allowed Hosts"
    severity = "CRITICAL"
    description = "Allowed hosts should be set in production"

    allowed_hosts = settings.ALLOWED_HOSTS
    debug_mode = settings.DEBUG

    if debug_mode:
        status = "SKIPPED"
        solution = None

    elif not allowed_hosts:
        status = "FAIL"
        solution = "Set ALLOWED_HOSTS to a list of allowed hosts"
    
    elif "*" in allowed_hosts:
        status = "FAIL"
        solution = "Remove '*' and specify explicit hostnames"

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