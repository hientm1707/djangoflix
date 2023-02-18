#!/bin/bash
echo "Cleaning up any git ignored files..."

# copy and paste the line below to get the same results as running this script
git rm --cached 'git ls-files -ic --exclude-from=.gitignore'

echo "Finished clean up."