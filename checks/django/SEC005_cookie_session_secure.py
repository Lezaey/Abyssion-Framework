from django.conf import settings

def check_cookie_session_secure():
    check_id = "SEC005"
    name = "Cookie Session Secure"
    severity = "HIGH"
    description = "Session cookies should only be sent over HTTPS"
    
    debug_mode = settings.DEBUG
    cookie_session_secure = getattr(settings, "SESSION_COOKIE_SECURE", False)
    
    if debug_mode:
        status = "SKIPPED"
        solution = None
    
    elif not cookie_session_secure:
        status = "FAIL"
        solution = "Set SESSION_COOKIE_SECURE to True"
    
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
