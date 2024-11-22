#!/bin/bash

# Check if a commit message is provided
if [-z "$1"]; then
  echo "Error: Commit message is required."
  echo "Usage: ./push-to-github.sh \"Your commit message\""
  exit 1
fi

echo "Adds all untracked and updated files"
git add .

echo "Add files and do local commit"
git commit -am "$1"

echo "Pushing to Github repository..."
git push origin main
