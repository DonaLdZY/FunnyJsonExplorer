# UML

![1717677821746](image/README/1717677821746.png)

# Document

+ FunnyJsonExplorer: 程序的入口
  + parse_json()解析json文件并用ContainerFactory()创建Container对象
  + show()通过RootContainer()递归绘制json
  
+ IconFactory: 图标的工厂方法
  + get_icon() 生成对应图标族的图标
  
+ ContainerFactory: Container对象的抽象工厂方法
  + create_root_container() 字面意思
  + 具体工厂必须继承自此类并且实现创建中间Container与叶子Container两种方法
  
+ ConfigableFactory: ConfigabelContainer对应的工厂方法
  + create_container()/create_leaf() 创建ConfigabelContainer对象,并初始化不同的is_leaf参数

+ RectangleFactory/TreeFactory: 让ConfigableFactory指定加载rectangle/tree风格
  
+ RootContainer: json目录树的树根
  + add() 往该结点下挂子节点
  + draw() 树根不绘制内容,递归绘制的入口
  
+ Container: json目录树的中间节点或叶子结点
  + add() 往该结点下挂子节点
  + draw() 虚函数,其它Container类必须实现该函数

+ ConfigableContainer: 实现了由config.json读取style配置进行绘制
  + loadConfig()从config文件获得该行对应的制表符表
  + draw()根据制表符表绘制本行内容
