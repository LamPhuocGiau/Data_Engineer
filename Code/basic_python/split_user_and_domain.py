def input_email():
    email = input("please input email: ")
    return email

def main(email):
    user_email = email[:email.index("@")]
    domain_email = email[email.index("@") + 1:]
    return user_email, domain_email

def printMsg(user_email, domain_email):
    print(f"User of email is : {user_email}")
    print(f"Domain of email is: {domain_email}")

if __name__ == "__main__":
    email = input_email()
    user_email, domain_email = main(email)
    printMsg(user_email, domain_email)