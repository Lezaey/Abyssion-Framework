from django.conf import settings

def check_svg_upload():
    check_id = "WEB001"
    name = "SVG Upload"
    severity = "MEDIUM"
    description = "SVG uploads can allow embedded scripts and lead to XSS if not sanitized"
    
    debug_mode = settings.DEBUG

    allow_svg = getattr(settings, "ALLOW_SVG_UPLOAD", False)
    allowed_extensions = getattr(settings, "ALLOWED_EXTENSIONS", [])
    
    if debug_mode:
        status = "PASS"
        solution = None
    
    elif allow_svg:
        status = "FAIL"
        solution = "Disable SVG uploads or sanitize SVG files before storing"
    
    elif "svg" in allowed_extensions:
        status = "FAIL"
        solution = "Remove 'svg' from ALLOWED_UPLOAD_EXTENSIONS or sanitize SVG files"    

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