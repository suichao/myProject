ps -aux| grep test # 根据字符模糊匹配进程
lsof -i:8090 # 查询端口进程
nohup python test.py >> log.txt 2>&1 & # 后台运行python并输出日志
head log.txt -n 10 | grep text
tail log.txt -n 10
ln -l path softline # 创建软链接
chomk -R 777 dir # 修改权限