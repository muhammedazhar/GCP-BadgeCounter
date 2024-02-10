import requests
from bs4 import BeautifulSoup

# 1. Fetch webpage
url = "https://www.cloudskillsboost.google/public_profiles/6f083d23-4a2d-4d67-977b-7c3c7cea165c"
response = requests.get(url)
html_content = response.content

# 2. Parse HTML
soup = BeautifulSoup(html_content, "html.parser")

# 3. Extract badge information
badge_elements = soup.find_all("div", class_="profile-badge")

# 4. Count badges
badge_count = len(badge_elements)

# 5. Output result
print("Total number of skill badges:", badge_count)