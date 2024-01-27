# Assigning a URL to a variable
package_url = "https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.85/bin/apache-tomcat-9.0.85.tar.gz"

# Print the package URL
print("Package URL:", package_url)
# save this script as 'print_url.py' or any other name you prefer
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python print_url.py <url>")
        sys.exit(1)

    url_parameter = sys.argv[1]
    print(f"The provided URL is: {url_parameter}")
