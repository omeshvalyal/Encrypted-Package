import requests

# Assigning a URL to a variable
package_Url = "https://www.oracle.com/middleware/technologies/weblogic-server-installers-downloads.html#license-lightbox"

print("Package URL:", package_Url)

# Making a GET request
response = requests.get(package_Url)

# Checking the response
if response.status_code == 200:
    print("Request successful")
    print("Response content:")
    print(response.text)
else:
    print("Request failed. Status code:", response.status_code)
