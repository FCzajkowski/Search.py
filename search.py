import webbrowser
import sys

# Base URL for Google search
base_url = 'https://www.google.com/search?q='

# List of valid websites to filter the search results
valid_websites = [
    'reddit.com',
    'stackoverflow.com',
    'w3schools.com',
    'kodland.com',
    'leetcode.com',
    'github.com',
    'Udemy.com',
    'CodeAcademy.org'
    #'youtube.com'
]
RED = '\033[91m'
GREEN = '\033[92m'
WHITE = '\033[0m'


def gen_list_of_websites():
    # Generate the site filter string for the query
    filter_str = "("
    for index, website in enumerate(valid_websites):
        filter_str += 'site:' + website
        if index < len(valid_websites) - 1:
            filter_str += ' OR '
    filter_str += ")"
    return filter_str

def create_query():
    # Create the search query from command-line arguments
    query = sys.argv[1:]
    return ' '.join(query)

def create_url(query):
    # Create the full URL for the Google search
    filter_str = gen_list_of_websites()
    search_query = f"{query} {filter_str}"
    full_url = base_url + search_query
    return full_url

def main():
    if len(sys.argv[1:]) == 0:
        print(f"{RED}Please enter a valid query{WHITE}")
    else:
        print(f"{GREEN} opening{WHITE}")
        query = create_query()
        search_url = create_url(query)
        webbrowser.open(search_url)

if __name__ == "__main__":
    main()
