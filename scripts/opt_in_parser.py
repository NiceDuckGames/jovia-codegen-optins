import os
import re
import json

# Directory where the opt-ins file is located
OPTINS_FILE = '../optins.jsonl'

def parse_url(url):
    parts = url.split('/')
    new_parts = parts[:5] + ['']

    new_url = '/'.join(new_parts)
    return new_url

def parse_opt_in_issue(issue_body):
    # Extract relevant data from the issue body
    title_match = re.search(r'## Opt-In Request: (.+)', issue_body)
    repo_match = re.search(r'GitHub Repository: (.+)', issue_body)
    commit_match = re.search(r'Commit Hash: (.+)', issue_body)

    if not (title_match and repo_match and commit_match):
        print('Error: Invalid issue body format.')
        exit(1)

    title = title_match.group(1).strip()
    title = title.replace(' ', '_')
    repository_url = repo_match.group(1).strip()
    commit_hash = commit_match.group(1).strip()

    return {
        'title': title, 
        'repository_url': repository_url, 
        'commit_hash': commit_hash, 
        'tree_url': parse_url(repository_url) + f'tree/{commit_hash}', 
        'issue_link': os.getenv('ISSUE_LINK')
    }

def update_opt_ins_file(opt_in_data):
    # Append opt-in data to the JSONL file
    with open(OPTINS_FILE, 'a') as file:
        json.dump(opt_in_data, file)
        file.write('\n')

def main():
    # Get the issue body from the environment variable
    issue_body = os.getenv('ISSUE_BODY')

    if issue_body is None:
        print('Error: Issue body is missing.')
        exit(1)

    # Parse the opt-in issue and extract relevant data
    opt_in_data = parse_opt_in_issue(issue_body)

    print("OPT-IN Request")
    print(opt_in_data)

    # Add opt-in data to the GH ENV for use in the workflow.
    env_file = os.getenv('GITHUB_ENV')

    with open(env_file, "a") as envfile:
        envfile.write(f"PROJECT_NAME={opt_in_data['title']}\n")
        envfile.write(f"PROJECT_LINK={opt_in_data['repository_url']}\n")
        envfile.write(f"COMMIT_HASH={opt_in_data['commit_hash']}\n")
        envfile.write(f"TREE_URL={opt_in_data['tree_url']}\n")

    # Create the opt-ins file if it doesn't exist
    if not os.path.exists(OPTINS_FILE):
        open(OPTINS_FILE, 'a').close()

    # Update the opt-ins file
    update_opt_ins_file(opt_in_data)

if __name__ == '__main__':
    main()
