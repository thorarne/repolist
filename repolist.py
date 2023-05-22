#!bin/python
from sys import argv
from os import getenv
from github import Github
from github.GithubException import *

token = getenv('GH_TOKEN') or None

username = argv[1] if len(argv) > 1 else None

if not username:
  print(f'usage: {argv[0]} username')
  exit()

if not token:
  print('Need a valid token set')


g = Github(token)

try:
  user = g.get_user(username)
except UnknownObjectException:
  print(f'invalid github username: {username}')
  exit()

# get a list of repos - skipping forked ones
repos = [ r for r in user.get_repos() if not r.fork ]

# summary
print(f'Showing {len(repos)} of {user.public_repos} repositories in @{username} ({user.type})')

for repo in repos:
  description = repo.description or 'description'
  topics = '/'.join(repo.topics) or 'topics'
  language = repo.language or 'language'
  try:
    license = repo.get_license().license.name
  except:
    license = 'license'

  print(f'{repo.name:15} {language:10} {license:10} {topics:20}')
  print(f'{description} - {repo.html_url}')
  print('')
