## 报错信息
```
Can't create handler inside thread Thread[xxx] that has not called Looper.prepare()
```


## 问题原因
因为Handler对象与其调用者在同一线程中，如果在Handler中设置了延时操作，则调用线程也会堵塞。
每个Handler对象都会绑定一个Looper对象，每个Looper对象对应一个消息队列（MessageQueue）。
如果在创建Handler时不指定与其绑定的Looper对象，系统默认会将当前线程的Looper绑定到该Handler上。

在主线程中，可以直接使用new Handler()创建Handler对象，其将自动与主线程的Looper对象绑定；
在非主线程中直接这样创建Handler则会报错，因为Android系统默认情况下非主线程中没有开启Looper，而Handler对象必须绑定Looper对象。


## 解决方法
这种情况下，则有两种方法可以解决此问题：

### 方法1
先在该线程中手动开启Looper（Looper.prepare()-->Looper.loop()），然后将其绑定到Handler对象上；
```java
new Thread() {
　　public void run() {
        Looper.prepare();
        new Handler().post(runnable);//Runnable对象是运行在子线程中的，可以进行联网操作，不能更新UI
        Looper.loop();
　　}
}.start();
```
 

### 方法2
通过Looper.getMainLooper()，获得主线程的Looper，将其绑定到此Handler对象上。
```java
new Thread() {
　　public void run() {
        new Handler(Looper.getMainLooper()).post(runnable);//Runnable对象是运行在主线程中的，不可以进行联网操作，可以更新UI
　　}
}.start();
```

---
- [在子线程中new Handler报错--Can't create handler inside thread that has not called Looper.prepare() - Echo--Android - 博客园](https://www.cnblogs.com/jingmo0319/p/5730963.html)
