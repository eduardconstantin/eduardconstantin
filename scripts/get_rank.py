import requests
from bs4 import BeautifulSoup
import re

name = "Eduard-Constantin Ibinceanu"
url = "https://raw.githubusercontent.com/gayanvoice/top-github-users/main/markdown/public_contributions/romania.md"
response = requests.get(url)
data = response.text

soup = BeautifulSoup(data, "html.parser")

table = soup.find_all("table")[3]

rows = table.find_all("tr")

name = "Eduard-Constantin Ibinceanu"
for i, row in enumerate(rows):
    if len(row.find_all("td")) > 1:
        if name in row.find_all("td")[1].text:
            rank = i
            break

print(f"The rank of {name} is {rank}")

with open("README.md", "r") as f:
    readme = f.read()

start_comment = "<!-- RANK:START -->"
end_comment = "<!-- RANK:END -->"
new_text = f"{start_comment}\n- 🏆 I am ranked {rank} among the top [GitHub users in Romania based on public contributions.](https://github.com/gayanvoice/top-github-users/blob/main/markdown/public_contributions/romania.md)\n{end_comment}"
readme = re.sub(f"{start_comment}.*{end_comment}", new_text, readme, flags=re.DOTALL)

with open("README.md", "w") as f:
    f.write(readme)