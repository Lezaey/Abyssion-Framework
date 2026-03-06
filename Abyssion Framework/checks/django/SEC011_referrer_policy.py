from django.conf import settings

def check_referrer_policy():
    check_id = "SEC011"
    name = "Referrer Policy"
    severity = "MEDIUM"
    description = "Referrer Policy should be enabled in production"
    
    debug_mode = settings.DEBUG

    referrer_policy = getattr(settings, "SECURE_REFERRER_POLICY", None)
    
    valid_policies = [
        "no-referrer",
        "origin",
        "origin-when-cross-origin",
        "same-origin",
        "strict-origin",
        "strict-origin-when-cross-origin"
    ]

    if debug_mode:
        status = "SKIPPED"
        solution = None
    
    elif not referrer_policy:
        status = "FAIL"
        solution = "Set SECURE_REFERRER_POLICY to 'strict-origin-when-cross-origin'"      

    elif referrer_policy not in valid_policies:
        status = "FAIL"
        solution = "Use a secure policy like 'strict-origin-when-cross-origin'"
    
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