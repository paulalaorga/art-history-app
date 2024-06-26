#!/usr/bin/env sh

# abort on errors
set -e

# build the project
npm run build

# navigate into the build output directory
cd dist

# setting a custom domain
echo 'https://paulalaorga.github.io/art-history-app/' > CNAME

# initialize a new git repository
git init
git add -A
git commit -m 'deploy'

# force push to the gh-pages branch
git push -f git@github.com:paulalaorga/art-history-app.git main:gh-pages

# return to the previous directory
cd -
