from django.conf import settings


def check_dangerous_file_upload():
    check_id = "SEC010"
    name = "Dangerous File Upload"
    severity = "HIGH"
    description = "Dangerous file upload extensions should not be allowed in production"

    allowed_extensions = getattr(settings, "ALLOWED_UPLOAD_EXTENSIONS", [])

    # normalizar extensões
    allowed_extensions = [
        ext.lower().replace(".", "").strip()
        for ext in allowed_extensions
    ]

    dangerous_extensions = {
        "php", "php3", "php4", "php5", "phtml",
        "js",
        "html", "htm",
        "svg", "xml",
        "exe",
        "sh",
        "bat",
        "cmd",
        "cgi",
        "pl",
        "py"
    }

    if not allowed_extensions:
        status = "FAIL"
        solution = """
        Add this to your Django settings:

        ALLOWED_UPLOAD_EXTENSIONS = [
            "jpg",
            "jpeg",
            "png",
            "pdf"
        ]
        """

    else:
        detected = sorted(set(allowed_extensions) & dangerous_extensions)

        if detected:
            status = "FAIL"
            solution = (
                "Remove dangerous extensions from ALLOWED_UPLOAD_EXTENSIONS: "
                + ", ".join(detected)
            )
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