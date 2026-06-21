url = input("Enter URL: ")

if "@" in url:
    print("Suspicious Link Detected")

elif "bit.ly" in url:
    print("Suspicious Shortened Link")

elif not url.startswith("https://"):
    print("Warning: Website is not using HTTPS")

else:
    print("URL looks safe")
