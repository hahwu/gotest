from git import Repo

fo = open("test","w")

fo.write("hello world")

fo.close()

repo = Repo("/home/swoole/gotest")

repo.index.commit("修改test文件")