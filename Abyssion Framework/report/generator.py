import json
from datetime import datetime


def generate_terminal_report(results):

    scan_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    total = len(results)

    pass_count = sum(1 for r in results if r["status"] == "PASS")
    fail_count = sum(1 for r in results if r["status"] == "FAIL")
    skipped_count = sum(1 for r in results if r["status"] == "SKIPPED")
    error_count = sum(1 for r in results if r["status"] == "ERROR")

    print("\n")
    print("┌──────────────────────────────────────────────┐")
    print("│           Abyssion Framework Scanner         │")
    print("└──────────────────────────────────────────────┘")

    print(f"\nScan Time: {scan_time}")

    print("\nSummary")

    print("\n______________________________________________")

    print(f"Total Checks : {total}")
    print(f"Passed       : {pass_count}")
    print(f"Failed       : {fail_count}")
    print(f"Skipped      : {skipped_count}")
    print(f"Errors       : {error_count}")

    print("\nDetailed Results")
    print("______________________________________________")

    for result in results:

        print(f"\n[{result['id']}] {result['name']}")
        print(f"Status   : {result['status']}")
        print(f"Severity : {result['severity']}")

        if result["status"] == "FAIL":

            if result.get("description"):
                print(f"Issue    : {result['description']}")

            if result.get("solution"):
                print(f"Fix      : {result['solution']}")


def export_json_report(results):

    report = {
        "tool": "Abyssion Security Scanner",
        "scan_time": datetime.now().isoformat(),
        "total_checks": len(results),
        "results": results
    }

    with open("security_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("\nJSON report saved to security_report.json")