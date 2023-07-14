import os
import requests
from github import Github

# GitHub API token
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Repository information
REPO_OWNER = 'NiceDuckGames'
REPO_NAME = 'ducky-ai-optins'

def parse_opt_in_issues():
    # Initialize GitHub API client
    g = Github(GITHUB_TOKEN)

    # Get the repository
    repo = g.get_repo(f'{REPO_OWNER}/{REPO_NAME}')

    # Get all open opt-in issues
    opt_in_issues = repo.get_issues(state='open', labels=['opt-in'])

    # Generate opt-in data collection list
    opt_in_data = []
    for issue in opt_in_issues:
        project_url = issue.body.strip()
        commit_hash = issue.comments[0].body.strip() if issue.comments else ''
        opt_in_data.append({'project_url': project_url, 'commit_hash': commit_hash})

    return opt_in_data

def update_opt_in_list(opt_in_data):
    # Write opt-in data to a file
    with open('opt_in_list.txt', 'w') as file:
        for item in opt_in_data:
            file.write(f"{item['project_url']},{item['commit_hash']}\n")

def main():
    opt_in_data = parse_opt_in_issues()
    update_opt_in_list(opt_in_data)
    print('Opt-in data collection list has been updated.')

if __name__ == '__main__':
    main()
