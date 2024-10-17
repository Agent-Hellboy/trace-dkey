import requests
from trace_dkey import trace

# JSONPlaceholder API example
def jsonplaceholder_api_example():
    # Get a sample post
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = requests.get(url)
    post_data = response.json()

    # Find the path to the 'title' key
    paths = trace(post_data, 'title')
    print("Paths to 'title':")
    for path in paths:
        print(" -> ".join(path))
        print(f"Value: {post_data['title']}")

    # Get comments for the post
    url = "https://jsonplaceholder.typicode.com/posts/1/comments"
    response = requests.get(url)
    comments_data = response.json()

    # Find the path to the 'email' key in the first comment
    paths = trace(comments_data[0], 'email')
    print("\nPaths to 'email' in the first comment:")
    for path in paths:
        print(" -> ".join(path))
        print(f"Value: {comments_data[0]['email']}")

if __name__ == "__main__":
    jsonplaceholder_api_example()