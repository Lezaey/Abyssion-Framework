from django.conf import settings

def check_csrf_cookie_secure():
    check_id = "SEC006"
    name = "CSRF Cookie Secure"
    severity = "HIGH"
    description = "CSRF cookie should only be sent over HTTPS"
    
    debug_mode = settings.DEBUG
    csrf_cookie_secure = getattr(settings, "CSRF_COOKIE_SECURE", False)
    
    if debug_mode:
        status = "SKIPPED"
        solution = None
    
    elif not csrf_cookie_secure:
        status = "FAIL"
        solution = "Set CSRF_COOKIE_SECURE to True"
    
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