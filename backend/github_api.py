import requests


def get_repository_data(repo_url):

    parts = repo_url.rstrip("/").split("/")

    if len(parts) < 2:
        raise Exception("Invalid GitHub repository URL")

    owner = parts[-2]
    repo = parts[-1]

    api_url = f"https://api.github.com/repos/{owner}/{repo}"

    response = requests.get(api_url)

    if response.status_code != 200:
        raise Exception("Repository not found")

    data = response.json()

    return {
        "name": data["name"],
        "full_name": data["full_name"],
        "description": data["description"],
        "stars": data["stargazers_count"],
        "forks": data["forks_count"],
        "open_issues": data["open_issues_count"],
        "watchers": data["watchers_count"],
        "language": data["language"],
        "created_at": data["created_at"],
        "updated_at": data["updated_at"],
        "license": data["license"]["name"] if data["license"] else "No license",
        "default_branch": data["default_branch"]
    }
