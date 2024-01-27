import requests

# Assigning a URL to a variable
package_Url = "https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.85/bin/apache-tomcat-9.0.85.tar.gz"

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
