# create a new repository on the command line
echo "# myProject" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/suichao/myProject.git
git push -u origin main

git remote rm origin
git remote add origin https://gitee.com/xxxxxx.git
git push origin master

git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch demo/mySubword/news.zh.txt" --prune-empty --tag-name-filter cat -- --all

git remote add origin https://github.com/suichao/myProject.git
git branch -M main
git push -u origin main