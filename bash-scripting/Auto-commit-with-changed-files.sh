#!/bin/bash

cd ~/notes
git init
git add .

# Check if there are any previous commits
if git rev-parse --verify HEAD >/dev/null 2>&1; then
  # Get a list of changed files
  changed_files=$(git diff --name-only --cached)

  # If there are no changes, set a default commit message
  if [ -z "$changed_files" ]; then
    commit_message="No changes"
  else
    commit_message="Changed files: $changed_files"
  fi
else
  commit_message="Initial commit"
fi

if git commit -m "$commit_message"; then
  echo "Commit created with message: $commit_message"
else
  echo "Commit not created"
fi

# Check if remote origin exists
if git remote | grep -q "origin"; then
  echo "Remote origin already exists"
else
  # Extract the GitHub username and repository name from the remote URL
  remote_url=$(git config --get remote.origin.url)
  github_username=$(echo $remote_url | cut -d':' -f2 | cut -d'/' -f1)
  github_repo=$(echo $remote_url | cut -d'/' -f2 | cut -d'.' -f1)
  
  git remote add origin git@github.com:$github_username/$github_repo.git
fi

if git branch --list | grep -q "master"; then
  git push -u origin master
elif git branch --list | grep -q "main"; then
  git push -u origin main
else
  echo "Neither master nor main branch exists"
fi
