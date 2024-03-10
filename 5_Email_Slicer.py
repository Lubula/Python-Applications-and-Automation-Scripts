def email_slicer():
    """
    This function collects an email address from the user, splits it into username, domain, and extension,
    and prints out each part.
    """
    print("Welcome to Email Slicer")
    print("")

    # Collect the email address from the user
    email_input = input("Input your email address: ")

    # Check if "@" and "." are present in the email address
    if "@" not in email_input or "." not in email_input:
        print("Invalid email address. Please enter a valid email.")
        return

    # Split the email into username and domain parts
    username, domain = email_input.split("@")

    # Split the domain into domain name and extension parts
    domain_parts = domain.split(".")
    if len(domain_parts) != 2:  # Ensure domain has exactly one dot
        print("Invalid domain in email address. Please enter a valid email.")
        return

    domain_name, extension = domain_parts

    # Print out the username, domain name, and extension
    print(f"Username: {username}")
    print(f"Domain: {domain_name}")
    print(f"Extension: {extension}")

# Call the function to run the code
email_slicer()

def test_email_slicer():
    # Test valid email address
    assert email_slicer("john@example.com") == ("john", "example", "com")

    # Test invalid email address without "@" symbol
    assert email_slicer("johnexample.com") is None

    # Test invalid email address without "." symbol
    assert email_slicer("john@examplecom") is None

    # Test invalid email address with multiple dots in domain
    assert email_slicer("john@example.co.uk") is None

    print("All tests passed!")

if __name__ == "__main__":
    test_email_slicer()
