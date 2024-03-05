#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository.

Usage: ./100-github_commits.py <repository name> <repository owner>
"""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])

    req = requests.get(url)
    commits = req.json()
    try:
        for k in range(10):
            print("{}: {}".format(
                commits[k].get("sha"),
                commits[k].get("commit").get("author").get("name")))
    except IndexError:
        pass
