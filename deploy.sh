#!/usr/bin/env sh

# abort on errors
set -e

# build the project
npm run build

# navigate into the build output directory
cd dist

# setting a custom domain
echo 'www.opus-app.com.au' > CNAME

# initialize a new git repository
git init
git add -A
git commit -m 'deploy'

# force push to the gh-pages branch
git push -f git@github.com:paulalaorga/art-history-app.git main:deployment

# return to the previous directory
cd -
