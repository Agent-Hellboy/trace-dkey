import requests
from trace_dkey import trace

# GitHub API example
def github_api_example():
    # Get information about a GitHub repository
    repo = "Agent-Hellboy/trace-dkey"
    url = f"https://api.github.com/repos/{repo}"
    response = requests.get(url)
    data = response.json()

    # Find the path to the 'stargazers_count' key
    paths = trace(data, 'stargazers_count')
    print("Paths to 'stargazers_count':")
    for path in paths:
        print(" -> ".join(path))
        print(f"Value: {data['stargazers_count']}")

    # Find the path to the 'login' key (owner's login)
    paths = trace(data, 'login')
    print("\nPaths to 'login':")
    for path in paths:
        print(" -> ".join(path))
        print(f"Value: {data['owner']['login']}")

if __name__ == "__main__":
    github_api_example()