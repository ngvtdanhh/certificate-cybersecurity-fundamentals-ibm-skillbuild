import re

def analyze(header: str):
    alerts = []
    if re.search(r"spf=fail", header, re.I): alerts.append("SPF failed")
    if re.search(r"dkim=fail", header, re.I): alerts.append("DKIM failed")
    if re.search(r"from=.*@(?!yourdomain\.com)", header, re.I): alerts.append("Suspicious From domain")
    return alerts or ["No obvious spoofing detected"]

# Example
# print(analyze(open("header.txt").read()))
