4. 取消文件暂存记录
git rm --cached [file]
5. 将文件同步到本地仓库
git commit [file] -m [message]　　　　-----file为同步文件名，写的话，只同步指定的文件，不写的话，同步所有文件，message为提交所填写的信息
说明: -m表示添加一些同步信息，表达同步内容
e.g. 将暂存区所有记录同步到仓库区
git commit -m 'add files'
6. 查看commit 日志记录
git log
git log --pretty=oneline
7. 比较工作区文件和仓库文件差异
git diff [file]
8. 放弃工作区文件修改
git checkout -- [file]　　　　　　　　　　-------“--”l两端都有空格，如果不用“--”则表示从仓库中恢复以前数据（即恢复到不修改，不删除前的内容）
9. 从仓库区恢复文件
git checkout [file]
10 .移动或者删除文件
git mv [file] [path]
git rm [files]
注意: 这两个操作会修改工作区内容，同时将操作记录提交到暂存区。
