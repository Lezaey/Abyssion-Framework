def run_checks(checks):

    results = []

    for check in checks:
        try:
            result = check()
            results.append(result)

        except Exception as error:

            results.append({
                "id": "ENGINE_ERROR",
                "name": check.__name__,
                "status": "ERROR",
                "severity": "CRITICAL",
                "description": str(error),
                "solution": "Fix the check implementation"
            })
    
    return results