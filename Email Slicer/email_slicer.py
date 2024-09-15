print("Welcome to the email slicer!")
# Define a function that will split the gmail into a username, domain, and extension.
def main(email_input):
    # Created 2 variables and initialize them to the email input that was split at the "@" symbol using the split function.
    (username, domain) = email_input.split("@")
    # Now we do the same for the domain that will split at the "." with the split function. This will split the domain and the extension.
    (domain, extension) = domain.split(".")
    # Print the Username, Domain, and the Extension using the Triple Quote (Multi-Line) docstrings.
    print(f"""Username: {username}
Domain: {domain}
Extension: {extension}""")
# Call the main() function, use the input function to pass the user input (email address) as a variable for the function.
main(input("Provide your email address: "))