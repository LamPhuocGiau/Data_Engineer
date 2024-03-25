from split_user_and_domain import main, printMsg

def split_emails():
    emails = ("Lamphuocgia@gmail.com", "lamgialinh@gmail.com", "vonhuquynh@yahoo.com", "lamphuocgiau@hotmail.com")
    for email in emails:
        user_email, domain_email = main(email)
        printMsg(user_email, domain_email)

if __name__ == "__main__":
    split_emails()
    