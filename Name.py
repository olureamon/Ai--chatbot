import requests

username = input("Enter the username to check: ")

sites = {
    "GitHub": f"https://github.com/{username}",
    "Twitter/X": f"https://twitter.com/{username}", 
    "Instagram": f"https://www.instagram.com/{username}/",
    "Reddit": f"https://www.reddit.com/user/{username}/",
    "TikTok": f"https://www.tiktok.com/@{username}"
}

print(f"\nChecking username: {username}\n")

for site_name, url in sites.items():
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{site_name}: TAKEN ❌")
        elif response.status_code == 404:
            print(f"{site_name}: AVAILABLE ✅")
        else:
            print(f"{site_name}: Not sure – got status {response.status_code}")
    except:
        print(f"{site_name}: Couldn't check")

print("\nNote: Sometimes sites block checks. If it says TAKEN, it’s usually correct.")
