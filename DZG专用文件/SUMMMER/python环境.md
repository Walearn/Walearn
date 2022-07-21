## 下载python的解释器

1:[python官网](https://www.python.org/)

优点 : 最正规 并且可以下载各种python版本

缺点: 全英文 多python版本加大了 新手的理解难度 而且一般情况下 网速感人 还有可能打不开 哈哈哈

![image-20220720024657108](D:\3.DOC\2.GITBOOK\COLLAGE_BOOK\Walearn\DZG专用文件\IMAGE\image-20220720024657108.png)

![image-20220720024803659](D:\3.DOC\2.GITBOOK\COLLAGE_BOOK\Walearn\DZG专用文件\IMAGE\image-20220720024803659.png)

2:[腾讯软件中心](https://pc.qq.com/search.html#!keyword=python)

优点 : 本土化网站 简单易用 会用搜索就行

缺点: 版本单一 我现在就只有3.8.5的版本 

记得一定要点普通下载 

![image-20220720024535541](D:\3.DOC\2.GITBOOK\COLLAGE_BOOK\Walearn\DZG专用文件\IMAGE\image-20220720024535541.png)

## python的ide(集成开发环境)

1: pycharm (个人推荐)

​		就只有一件事情要做 就是 创建一个python环境给 pycharm 使用 就这样 

2: vscode

插件里面下载python就好了 

3: 等等 

## 修改pip源

因为pip 默认会去官网下载 导致网速感人 而且还会有超时的风险 所以我们会采用国内镜像 加快下载速度

```
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple 
```

```
阿里云 http://mirrors.aliyun.com/pypi/simple/
中国科技大学 https://pypi.mirrors.ustc.edu.cn/simple/
豆瓣(douban) http://pypi.douban.com/simple/
清华大学 https://pypi.tuna.tsinghua.edu.cn/simple/
中国科学技术大学 http://pypi.mirrors.ustc.edu.cn/simple/
```



## 修改lib的安装位置

```
python -m site 
可以查看到python的环境变量
```

![image-20220720025357134](D:\3.DOC\2.GITBOOK\COLLAGE_BOOK\Walearn\DZG专用文件\IMAGE\image-20220720025357134.png)

打开python安装目录中Lib文件夹下的site.py 修改其中的这两项 

这里两个文件夹如果 不存在 需要你自己创建



```
USER_SITE = "%python安装路径%Libsite-packages"     #用户自定义的依赖安装包的路径

USER_BASE = "%python安装路径%Scripts"    #用户自定义的启用Python脚本的路径
```

