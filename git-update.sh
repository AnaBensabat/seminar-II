find * -size +99M -type f | cat >> .gitignore
git add -A
git commit -m "update"
git push
