import requests
import xmltodict
import chevron
import os
from dotenv import load_dotenv
import json

load_dotenv()

# Prepare data
data = {
    "posts": [],
    "repositories": []
}

# Get my feeds
print("Collecting blogs data...")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
}
resp = requests.get("https://medium.com/feed/@chonla", headers=headers)
feed = xmltodict.parse(resp.text)

for feed_item in feed["rss"]["channel"]["item"]:
    data["posts"].append({
        "title": feed_item["title"],
        "link": feed_item["link"]
    })

# Get my repositories
print("Collecting repositories data...")
GITHUB_TOKEN = os.environ["GH_TOKEN"]
headers = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}
query = """
{
    user(login: "chonla") {
        pinnedItems(first: 6, types: REPOSITORY) {
            nodes {
                ... on Repository {
                        name
                        description
                        url
                        createdAt
                        updatedAt
                    }
            }
        }
    }
}
"""
resp = requests.post("https://api.github.com/graphql", json={"query":query}, headers=headers) #users/chonla/repos?sort=updated&direction=desc", headers=headers)

repos = list(map(
            lambda repo: {
                "name": repo["name"],
                "url": repo["url"],
                "description": repo["description"] if repo["description"] else ""
            },
            resp.json()["data"]["user"]["pinnedItems"]["nodes"]
        ))
for repo in repos:
    data["repositories"].append(repo)

with open("README.mustache", "r") as f:
    readme_content = chevron.render(f, data)
    with open("README.md", "w") as w:
        w.write(readme_content)