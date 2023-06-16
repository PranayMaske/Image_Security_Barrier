import re

num = 'ASD456A4'

if re.match(r'^[A-Z]{3}\d{3}[A-Z]\d$', num):
    print("String matches the pattern")
else:
    print("String does not match the pattern")