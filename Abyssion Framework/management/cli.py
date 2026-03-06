import argparse
from engine.loader import load_checks
from engine.executor import run_checks
from report.generator import generate_terminal_report, export_json_report

import checks

def main():
    parser = argparse.ArgumentParser(description="Security Check Framework")

    parser.add_argument(

        "--json",
        help="Export results to JSON",
        action="store_true"
    )

    args = parser.parse_args()

    checks = load_checks(checks.django)
    results = run_checks(checks)
    generate_terminal_report(results)
    if args.json:
        export_json_report(results)