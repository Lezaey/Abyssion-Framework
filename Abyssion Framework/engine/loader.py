import pkgutil
import importlib

def load_checks(package):
    checks = []

    for _, module_name, _ in pkgutil.iter_modules(package.__path__):

        module = importlib.import_module(f"{package.__name__}.{module_name}")

        for attribute in dir(module):
            if attribute.startswith("check_"):

                check_function = getattr(module, attribute)

                if callable(check_function):
                    checks.append(check_function)

    return checks