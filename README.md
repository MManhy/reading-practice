# Git 与代码版本管理实践笔记

## 学习资料来源
- 廖雪峰 Git 教程：https://www.liaoxuefeng.com/wiki/896043488029600
- Git 官方文档：https://git-scm.com/doc

## 实践流程
1. 在 Windows 环境安装 Git，配置用户名和邮箱
2. 创建本地文件夹 D:\git-practice
3. 使用 `git init` 初始化仓库
4. 创建代码文件，多次修改，使用 `git add` 和 `git commit` 进行版本记录
5. 在 Gitee 创建公开远程仓库，关联本地并推送

## 提交记录说明
- 第 1 次提交：添加初始代码文件 `ner_extraction.py`
- 第 2 次提交：添加注释说明
- 第 3 次提交：增加完成提示功能
- 第 4 次提交：增加注释说明

## 遇到的问题及解决方法
1. 问题：第一次执行 `git push` 时提示 “failed to push some refs”  
   解决：因为远程仓库有 README 文件而本地没有，使用 `git pull origin main --allow-unrelated-histories` 拉取合并后再推送成功。

2. 问题：执行 `git add` 后不小心提交了多余的文件  
   解决：先用 `git reset HEAD 文件名` 取消暂存，然后创建 `.gitignore` 文件并添加忽略规则。

## Git 学习心得
这次的实践让我理解了版本控制的意义。每一次 commit 就像给代码拍了一张快照，可以随时回到过去的状态。虽然刚开始觉得命令有点抽象，但实际跟着操作一遍后，发现它确实能解决“改了哪里”“改坏了怎么回去”的问题。在后续的课程项目中，我将尝试使用 Git 来管理小组作业，避免代码混乱。
