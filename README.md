commit-id  // 版本标志的MD5编码  

git init //初始化文件夹

git branch -M main
git branch -d bak  //删除分支

git remote add origin git@github.com:MrLiuWinter/vscodetest.git

git fetch + git merge ==> git pull

查看  
git config user.name  
git config user.email

配置  
git config --global user.name "name"  
git config --global user.email "email"  

提交代码  
远程：dev分支  
本地：bak分支  

git add .  // 提交所有更新到本地当前工作区 bak 
git commit -m "comments" //备注

更新远程库节点  
git checkout dev  //检出到主分支  
git fetch  
git rebase -i  //同步本地的dev分支，提交所有commit内容（Pick或F继承）  
git cherry-pick bak  // 同步bak与dev，处理冲突  
编译检查一遍  
git push

 
git stash  //暂存修改  
git reset --hard  //强制重置  
git reset --soft  //软重置  