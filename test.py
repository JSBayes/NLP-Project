from requests import get
from bs4 import BeautifulSoup, SoupStrainer
from os import path
import os
import json
from typing import Dict, List
import requests
from env import github_token


def get_links():
    pages = []
    url = 'https://github.com/search?q=stars%3A%3E1&type=Repositories'
    headers = {'User-Agent': 'Technomancer'}
    response = get(url, headers=headers)
    soup = BeautifulSoup(response.text,"html.parser")
    repocards = soup.select("div", class_="repo-list-item")
    urls = []
    for card in repocards:
        if card.select_one("a.v-align-middle") != None:
            try:
                a = card.select_one("a.v-align-middle")
                url = a["href"]
                urls.append(url)
            except:
                continue
        else:
            continue
    urls = list(set(urls))
    return urls

urls = get_links()
urls





repos = urls
headers = {
    "Authorization": f"token {github_token}",
    "User-Agent": "Symeonw",
}

if (
    headers["Authorization"] == "token "
    or headers["User-Agent"] == "N/A"
):
    raise Exception(
        "You need to follow the instructions marked TODO in this script before trying to use it"
    )


def github_api_request(url: str) -> requests.Response:
    return requests.get(url, headers=headers)


def get_repo_language(repo: str) -> str:
    url = f"https://api.github.com/repos{repo}"
    return github_api_request(url).json().get("language", None)


def get_repo_contents(repo: str) -> List[Dict[str, str]]:
    url = f"https://api.github.com/repos{repo}/contents/"
    return github_api_request(url).json()


def get_readme_download_url(files: List[Dict[str, str]]) -> str:
    """
    Takes in a response from the github api that lists
    the files in a repo and returns the url that can be
    used to download the repo's README file.
    """
    print('[get_readme_download_url] files', files)
    for file in files:
        print('[get_readme_download_url] file', file)
        if file["name"].lower().startswith("readme"):
            return file["download_url"]


def process_repo(repo: str) -> Dict[str, str]:
    """
    Takes a repo name like "gocodeup/codeup-setup-script" and returns
    a dictionary with the language of the repo and the readme contents.
    """
    contents = get_repo_contents(repo)
    return {
        "repo": repo,
        "language": get_repo_language(repo),
        "readme_contents": requests.get(get_readme_download_url(contents)).text,
    }


def scrape_github_data():
    """
    Loop through all of the repos and process them. Saves the data in
    `data.json`.
    """
    data = [process_repo(repo) for repo in repos]
    json.dump(data, open("data.json", "w"))


if __name__ == "__main__":
    scrape_github_data()

