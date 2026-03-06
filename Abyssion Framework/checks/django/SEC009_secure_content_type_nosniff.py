from django.conf import settings

def check_secure_content_type_nosniff():
    check_id = "SEC009"
    name = "Secure Content Type Nosniff"
    severity = "HIGH"
    description = "Secure Content Type Nosniff should be enabled in production"
    
    debug_mode = settings.DEBUG
    secure_content_type_nosniff = getattr(settings, "SECURE_CONTENT_TYPE_NOSNIFF", False)
    
    if debug_mode:
        status = "SKIPPED"
        solution = None
    
    elif not secure_content_type_nosniff:
        status = "FAIL"
        solution = "Set SECURE_CONTENT_TYPE_NOSNIFF to True"
    
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