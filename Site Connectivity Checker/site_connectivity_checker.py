# import urllib to use url functions
# Use urllib.request to get the data from the url
import urllib.request as urllib
# Welcome message displays when the program starts and prompts the user to enter a url.
print("This is a site connectivity checker program")
user_url = input("Please input your url: ")
# Write a function that accepts urls.
def main(url):
    # Displays a message for checking the connection which takes a few moments to complete.
    print("Checking Connectivity...")
    response = urllib.urlopen(url)
    print("Connected to", url, "successfully!")
    # Returns a response and the appropriate code if the url is valid or not.
    print("The response code: ", response.getcode())
#Call the url function
main(user_url)