import requests
from bs4 import BeautifulSoup
import re

name = "Eduard-Constantin Ibinceanu"
urls = {
    "public_contributions": "https://raw.githubusercontent.com/gayanvoice/top-github-users/main/markdown/public_contributions/romania.md",
    "followers": "https://raw.githubusercontent.com/gayanvoice/top-github-users/main/markdown/followers/romania.md",
    "total_contributions": "https://raw.githubusercontent.com/gayanvoice/top-github-users/main/markdown/total_contributions/romania.md",
}
ranks = {}

for category, url in urls.items():
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    table = soup.find_all("table")[3]
    rows = table.find_all("tr")

    for i, row in enumerate(rows):
        if len(row.find_all("td")) > 1:
            if name in row.find_all("td")[1].text:
                ranks[category] = i
                break

print(f"The ranks of {name} are {ranks}")

with open("README.md", "r") as f:
    readme = f.read()

start_comment = "<!-- RANK:START -->"
end_comment = "<!-- RANK:END -->"
new_text = f'{start_comment}\n<div align="center">\n'
for category, rank in ranks.items():
    new_text += f'  <a href="https://github.com/gayanvoice/top-github-users/blob/main/markdown/{category}/romania.md" target="_blank">\n'
    new_text += f'    <img src=https://img.shields.io/badge/{rank}-blue?style=for-the-badge&label={category.replace("_", "%20")} />\n'
    new_text += f'  </a>\n'
new_text += f'</div>\n{end_comment}'

readme = re.sub(f"{start_comment}.*{end_comment}", new_text, readme, flags=re.DOTALL)

with open("README.md", "w") as f:
    f.write(readme)