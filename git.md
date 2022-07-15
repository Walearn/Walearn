安装git 这些东西都不是问题啊 
其实我还是推荐 你去使用我们ubuntu系统来学习计算机 这才是 

[参考教程_雪峰](https://www.liaoxuefeng.com/wiki/896043488029600)

[参考教程_知乎_](https://zhuanlan.zhihu.com/p/30044692)



## 基本信息配制
    git config --global user.name "K_M_911"
    git config --global user.email 2547715095@qq.com
### 关闭服务器代理
    git config --global --unset http.proxy
    git config --global --unset https.proxy
### 生成密匙

    ssh-keygen -t rsa -C 2547715095@qq.com
    这里其实可以设置ssh的生成位置
### 关闭ssl认证

    git config --global http.sslverify false

copy.py 不可以使用哦 
import copy 会出问题 

### 添加远程仓库

```
git remote add friend https://github.com/Walearn/Walearn.git
```

### 上传

```
git add .
git commit -m "test"
git push 
```

### 下载

```
git clone https or ssh 
这里可以是
git clone https://github.com/Walearn/Walearn.git
```

## 更新 

```
git pull
```



## 指令表

|指令表|用途|
|--|--|
|commit||

在学习算法之前:
    我们先谈谈为什么我们要学习算法
    我们学习的都是最基本的算法 比如站队列 这些数据结构都是可以被我们使用的 比如创建一个队列 等待下载 但是 这里其实没有那么多的问题 我们直接创建进程 然后去等待 其实根本就没有那么复杂 但是 但是 我觉得写这样的代码是很低效率的'
    其实是没有问题的 因为本身你可能就一点写不了多少代码实际的情况就是这样 