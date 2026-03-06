import os
import sys
import django
import importlib
from pathlib import Path

from engine.loader import load_checks
from engine.executor import run_checks
from report.generator import generate_terminal_report, export_json_report

import checks


def autodetect_django_settings():
    base_path = Path(os.getcwd())

    for path in base_path.rglob("settings.py"):
        project_name = path.parent.name
        settings_module = f"{project_name}.settings"
        return settings_module

    return None


def setup_django():
    settings_module = autodetect_django_settings()

    if not settings_module:
        print("Django project not detected. Running only web checks.")
        return False

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", settings_module)

    try:
        django.setup()
        print(f"Django project detected: {settings_module}")
        return True
    except Exception as e:
        print(f"Failed to initialize Django: {e}")
        return False


def main():

    sys.path.insert(0, os.getcwd())

    django_ready = setup_django()

    all_checks = []

    if django_ready:
        django_checks = load_checks(checks.django)
        all_checks.extend(django_checks)

    web_checks = load_checks(checks.web)
    all_checks.extend(web_checks)

    results = run_checks(all_checks)

    generate_terminal_report(results)
    export_json_report(results)


if __name__ == "__main__":
    main()