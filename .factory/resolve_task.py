"""Validate a factory trigger before its issue number reaches an agent prompt."""
import json
import os
import re
import sys


def issue_number(value):
    if type(value) is not int or value < 1:
        raise ValueError('Issue number must be a positive integer')
    return value


def resolve_task(event, event_name, repository):
    if event.get('repository', {}).get('full_name') != repository:
        raise ValueError('Unexpected repository')
    if event.get('action') != 'labeled':
        raise ValueError('Expected a label event')
    label = event.get('label', {}).get('name')
    if event_name == 'issues' and label == 'factory':
        return issue_number(event.get('issue', {}).get('number'))
    if event_name == 'pull_request' and label == 'factory-go':
        pr = event.get('pull_request', {})
        if pr.get('state') != 'open':
            raise ValueError('Pull request is not open')
        if pr.get('head', {}).get('repo', {}).get('full_name') != repository:
            raise ValueError('Fork pull requests cannot run the factory')
        if pr.get('base', {}).get('ref') != event['repository'].get('default_branch'):
            raise ValueError('Expected the default base branch')
        match = re.fullmatch(r'factory/([1-9][0-9]*)', pr.get('head', {}).get('ref', ''))
        if not match:
            raise ValueError('Expected branch factory/<positive issue number>')
        return int(match.group(1))
    raise ValueError('Unsupported factory trigger')


if __name__ == '__main__':
    try:
        with open(os.environ['GITHUB_EVENT_PATH'], encoding='utf-8') as source:
            event = json.load(source)
        number = resolve_task(event, os.environ['GITHUB_EVENT_NAME'], os.environ['GITHUB_REPOSITORY'])
        with open(os.environ['GITHUB_OUTPUT'], 'a', encoding='utf-8') as output:
            output.write(f'number={number}\n')
    except (ValueError, KeyError, OSError) as error:
        print(f'Factory trigger rejected: {error}', file=sys.stderr)
        sys.exit(1)
