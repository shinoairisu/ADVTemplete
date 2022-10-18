# ADVTemplete
这个方案应当可以适用于所有编程语言之中。

## 1. 基础使用

```python
from ADVTemplete import advtemp as at
at.srcfolder("./game")
at.sourcefolder("./img")
at.load("xx.json") #读取存档
at.save("xx.json") #存储存档
at.run()#启动游戏
```

## 2. yaml

```yaml
#in main.yml
main: #以main标签开始
	- os: #os 画外音,也可以写作 旁白
		content: 测试测试  #可以写作 内容
	- speak:
		name: 毛毛
		content: 吃了吗
	- jump: #跳出去，会回来
		to: 标签名
		params: 
        	变量1: 15
        	变量2: 20
    - call: #跳出去，不回来了
    	to: 标签名
		params: 
        	变量1: 15
        	变量2: 20
    - history:
    	show: all
    - save:
    	name: xx.json
    - load:
    	name: xx.json
```



