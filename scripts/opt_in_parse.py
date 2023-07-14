import os
import json
import sys

# Directory where the opt-ins file is located
OPTINS_FILE = '../optins.jsonl'

def parse_opt_in_issue(issue_body):
    # Extract relevant data from the issue body
    data = json.loads(issue_body)
    project_url = data['project_url']
    commit_hash = data['commit_hash']

    return {'project_url': project_url, 'commit_hash': commit_hash}

def update_opt_ins_file(opt_in_data):
    # Append opt-in data to the JSONL file
    with open(OPTINS_FILE, 'a') as file:
        json.dump(opt_in_data, file)
        file.write('\n')

def main():
    # Get the issue body from the command line argument
    if len(sys.argv) < 2:
        print('Error: Issue body is missing.')
        sys.exit(1)

    issue_body = sys.argv[1]

    print("Parsing issue body")
    print(issue_body)

    # Parse the opt-in issue and extract relevant data
    opt_in_data = parse_opt_in_issue(issue_body)

    # Create the opt-ins file if it doesn't exist
    if not os.path.exists(OPTINS_FILE):
        open(OPTINS_FILE, 'a').close()

    # Update the opt-ins file
    update_opt_ins_file(opt_in_data)

if __name__ == '__main__':
    main()
