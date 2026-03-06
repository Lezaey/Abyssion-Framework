from django.conf import settings

def check_debug_disable():
    check_id = "SEC001"
    name = "Debug Mode Enabled"
    severity = "CRITICAL"
    description = "Debug should be disabled in production"
    
    debug_mode = getattr(settings, "DEBUG", False)

    if debug_mode:
        status = "FAIL"
        solution = "Disable debug in production"
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