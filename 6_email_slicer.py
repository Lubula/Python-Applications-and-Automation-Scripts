def email_slicer():
    """
    This function collects an email address from the user, splits it into username, domain, and extension,
    and prints out each part.
    """
    print("Welcome to Email Slicer")
    print("")

    # Collect the email address from the user
    email_input = input("Input your email address: ")
    
    # Split the email into username and domain parts
    (username,domain) = email_input.split("@")
    
    # Split the domain into domain name and extension parts
    (domain_name, extension) = domain.split(".")

    # Print out the username, domain name, and extension
    print("Username: ", username)
    print("Domain: ", domain_name)
    print("Extension: ", extension)

# Call the function to run the code
email_slicer()
