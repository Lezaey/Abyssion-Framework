from django.conf import settings

def check_sec_ssl_redirect():
    check_id = "SEC004"
    name = "SSL Redirect"
    severity = "HIGH"
    description = "SSL redirect should be enabled in production"
    
    debug_mode = settings.DEBUG
    ssl_redirect = getattr(settings, "SECURE_SSL_REDIRECT", False)
    
    if debug_mode:
        status = "SKIPPED"
        solution = None
    
    elif not ssl_redirect:
        status = "FAIL"
        solution = "Set SECURE_SSL_REDIRECT to True"
    
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
