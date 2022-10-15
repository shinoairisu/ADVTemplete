# ADVTemplete
##  1. 基础使用

```python
import ADVTemplete as at

def func1():
	at.os("这是第一个函数，将要跳到fun2")
	at.jump(tag="func1",to="func2") #跳到函数2，但是会从函数2回来。 tag是当前函数的世界标记。to是jump去的函数。tag标记会加入到函数栈。
	if at.jumpResult(tag="func1"): #处理jump栈的返回。比如jump去的函数中调用了call，此处就会直接跳出函数。True指的是直接结束这个函数。其实就是调用栈最后一个tag与此处tag不同。
        #此处jumpResult会去执行nextFunc。然后检查函数栈最后一个tag。如果与func1不同，就会返回true。
		return;
		#此处return后，线程回到 at.run()线程。这个线程也会处理nextFunc
	at.char("函数2","我回来了")



def func2(param):
	at.os("这是第二个函数，将要跳到fun3")
	op = at.option("1","2","3")
    print(param) #获取别处来的参数
	if op == 1:
		at.call("func3") #跳到fun3，不会回来这个函数。
		#fun3 会被记录到全局变量 nextFunc 中。默认nextFunc为""。
		return;  #必须跟return; 否则不会跳转
	if op == 2 or op == 3:
		at.ignore() #无视 或者做别的处理



def fun3():

	at.os("我是最后一个函数。")

#此处结束。但是，注意，虽然不会回到函数2，但是会回到函数1。由于call func3清空了调用栈，func1会得到一个true。

at.reg(name="main",func=func1)#注册函数。默认运行名字为main的函数
at.reg(name="func2",func=func2)
at.reg(name="func3",func=func3)
at.run() #运行ADV流程。每次内部跳转时会自动管理nextFunc
```



## 2.call与jump的签名

```python
import ADVTemplete as at
os.call(to="函数名",parameters={参数列表});return; #参数列表是向跳向的函数发送数据

os.jump(tag="标签名",to="函数名" ,parameters={参数列表});return if os.jumpResult(tag="标签名");
```

