#1 imprime la url
url = input("URL: ").strip()
print(url)

#2 imprime el nombre de usuario
url = input("URL: ").strip()
username = url.replace("https://twitter.com/", "")
print(f"Username: {username}")

#3 
import re

url = input("URL: ").strip()
matches = re.search(r"^https?://(www\.)?twitter\.com/(.+)$", url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(2))

#4
import re

url = input("URL: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))