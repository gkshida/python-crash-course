# Striping white spaces
favorite_languages = ' python '
favorite_languages = favorite_languages.rstrip()
print(favorite_languages)
favorite_languages = favorite_languages.lstrip()
print(favorite_languages)
favorite_languages = ' python '
favorite_languages = favorite_languages.strip()
print(favorite_languages)

# Removing prefix
url = "https://www.google.com"
simple_url = url.removeprefix("https://")
print(simple_url)