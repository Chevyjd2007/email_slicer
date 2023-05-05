email = input("What is your email? ")

def email_slicer(email):
    (user, domain) = email.split("@")
    (domain, TLD) = domain.split(".")

    print("Your user is: " + user)
    print("Your domain is: " + domain)
    print("Your top-level domain is: " + TLD)

    email = input("Would you like to split your email again? (email/quit) ")
    if email == quit:
        quit
    else:
        email_slicer(email)


email_slicer(email)
