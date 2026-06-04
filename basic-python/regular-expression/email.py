import re

email_pattern = r"\b[A-Za-z\s]+\b[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,3}\b"

email = "Contact as prasannavenkatesh652@gmail.com"

email1 = re.findall(email_pattern, email)

if(email):
    print("Email is found", email1)

else:
    print("Not found")