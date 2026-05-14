
import re

class StaticAnalyzer:

    def analyze_code(self, code):
        vulnerabilities = []

        patterns = [
            ('eval\\(', 'Use of eval()', 'High', 'Avoid eval() usage.'),
            ('exec\\(', 'Use of exec()', 'Critical', 'Avoid dynamic execution.'),
            ('password=', 'Hardcoded Password', 'High', 'Use environment variables.')
        ]

        for pattern, issue, severity, recommendation in patterns:
            if re.search(pattern, code):
                vulnerabilities.append({
                    'issue': issue,
                    'severity': severity,
                    'recommendation': recommendation
                })

        return vulnerabilities
