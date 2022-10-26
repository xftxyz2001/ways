## 问题描述
Implicit super constructor Object() is undefined for default constructor. Must define an explicit constructor.


## 解决方法
把java的类库加载进去
- 在工程上右键选择属性
- Java Build Path的Libraries
- Add Library选择JRE System Library
- 点击Next
- 选择Execution environment并选择版本或workspace default jre
- 点击Finish。
