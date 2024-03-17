# email_validation.py

import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$'
    return re.match(pattern, email) is not None

def filter_valid_emails(N, emails):
    valid_emails = [email for email in emails if is_valid_email(email)]
    return sorted(valid_emails)

# Пример использования функции
if __name__ == "__main__":
    N = int(input().strip())
    emails = [input().strip() for _ in range(N)]
    
    valid_emails = filter_valid_emails(N, emails)
    print(valid_emails)
