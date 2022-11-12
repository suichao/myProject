# git创建仓库
# create a new repository on the command line
echo "# myProject" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/suichao/myProject.git
git push -u origin main

# 清除远程仓库
git remote rm origin
git remote add origin https://gitee.com/xxxxxx.git
git push origin master

# 清除大文件
git filter-branch --force --index-filter "git rm -rf --cached --ignore-unmatch demo/mySubword/news.zh.txt" --prune-empty --tag-name-filter cat -- --all
# 清除缓存文件
git rm --cached path_of_a_giant_file
git rm --cached -r path_of_a_giant_dir
