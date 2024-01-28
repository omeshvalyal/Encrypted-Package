# save this script as 'print_url.py' or any other name you prefer
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python trigger2.py <url>")
        sys.exit(1)

    url_parameter = sys.argv[1]
    print(f"{url_parameter}")

