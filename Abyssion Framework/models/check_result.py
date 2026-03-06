class CheckResult:

    def __init__(self, id, name, status, severity, description, solution):

        self.id = id
        self.name = name
        self.status = status
        self.severity = severity
        self.description = description
        self.solution = solution

    def to_dict(self):

        return {
            "id": self.id,
            "name": self.name,
            "status": self.status,
            "severity": self.severity,
            "description": self.description,
            "solution": self.solution
        }