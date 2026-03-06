from django.conf import settings

def check_x_frame_options():
    check_id = "SEC008"
    name = "X-Frame-Options"
    severity = "HIGH"
    description = "X-Frame-Options should be enabled in production"
    
    debug_mode = settings.DEBUG
    x_frame_options = getattr(settings, "X_FRAME_OPTIONS", None)
    
    allowed_values = ["DENY", "SAMEORIGIN"]

    if debug_mode:
        status = "SKIPPED"
        solution = None
    
    elif x_frame_options not in allowed_values:
        status = "FAIL"
        solution = f"Set X_FRAME_OPTIONS to {allowed_values} to protect against clickjacking"
    
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