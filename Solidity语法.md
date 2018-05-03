### set方法
![set方法.gif](https://upload-images.jianshu.io/upload_images/1053458-4102fba85aebee9c.gif?imageMogr2/auto-orient/strip)

### 0012 字符串

字符串可以通过""或者''来表示字符串的值

```
pragma solidity 0.4.23;

contract StringLiterals{
    string _name;
    constructor() public{
        _name = 'name';
    }
    
    function setName(string name) public{
        _name = name;
    }
    
    function name() 
        public constant
        returns(string)
    {
        return _name;
    }
}
```

![string.gif](https://upload-images.jianshu.io/upload_images/1053458-c294047ed8c29296.gif?imageMogr2/auto-orient/strip)

**备注：**`string`字符串不能通过`length`方法获取其长度

### 0013 固定大小字节数组(Fixed-size byte arrays)
&emsp;&emsp;固定大小字节数组可以通过`bytes1`,`bytes2`,`bytes3`,...,`bytes32`来进行声明。`byte`的别名就是`byte1`
* `bytes1`只能存储`一个`字节，也就是二进制`8位`的内容。
* `bytes2`只能存储`两个`字节，也就是二进制`16位`的内容。
* `bytes3`只能存储`三个`字节，也就是二进制`24位`的内容。
* ....
* `bytes32`只能存储`三十二个`字节，也就是二进制`32*8 ＝ 256位`的内容。

```
pragma solidity 0.4.23;

contract arrays{
    byte public a = 0x6c;
    bytes1 public b = 0x6c;
    bytes2 public c = 0x6c69;
    bytes3 public d = 0x6c6979;
    bytes4 public e = 0x6c69797;
    
    //....
    
}
```

![array1.gif](https://upload-images.jianshu.io/upload_images/1053458-8c198ddc8b7ff159.gif?imageMogr2/auto-orient/strip)



**比较运算符**



```
pragma solidity 0.4.23;

// <=, <, == , != , >= ,>
contract comapre{
    byte a = 0x6c; //12 + 6 * 16 = 108
    byte b = 0x66; //6 + 6 * 16 = 102 
    byte c = 0x6c;
  
    bool public d = a >= b;
    bool public e = a == c;
    bool public f = a < b;
    
}

```

![compare.gif](https://upload-images.jianshu.io/upload_images/1053458-b86b125427283200.gif?imageMogr2/auto-orient/strip)

**位操作符:** `&`,`|`,`^(异或)`,`～(取反)`,`<<(左移)`,`>>(右移)`

```

pragma solidity 0.4.23;

contract comapre{
    byte a = 0x6c; //12 + 6 * 16 = 108
    byte b = 0x66; //6 + 6 * 16 = 102 
    byte c = 0x6c;
  
    //&,|,^(异或),～(取反),<<(左移),>>(右移)
    byte public d = a & b;
    byte public e = a | c;
    byte public f = a ^ b;
    byte public g = ~a;
    byte public h = a << 1;
    byte public i = a >> 1;
    
}
```
![位运算.gif](https://upload-images.jianshu.io/upload_images/1053458-db91066db7604531.gif?imageMogr2/auto-orient/strip)

**索引访问:**如果`x`是一个`bytesI`,那么可以通过`x[k](0<k<I)`获取对应索引的字节，PS:x[k]是只读，不可写。

```


```



**length**

```
pragma solidity 0.4.23;

contract comapre{
    bytes9 a = 0x6c6975828122; 
    
    uint public leng = a.length;
}

```

**对于不可变的理解**
* 长度不可变，里边的内容不可修改

`bytesI(1<=I<=32)`可以声明固定字节大小的字节数组变量，一旦声明，内部的字节和字节数组长度不可修改，
当然可以通过索引读取对应索引的字节，或者通过`length`读取字节数组的字节数。

### 14 动态大小字节数组(Dynamically－size byte arrays)

#### 一、Dynamically－size byte array
* `string`是一个动态尺寸的`UTF-8`编码字符串，它其实是一个特殊的可辨字节数组，`string`是引用类型，而非值类型
* `bytes`动态字节数组，引用类型

#### 二、常规字符串string转换为bytes

`string`字符串中没有提供`length`方法获取字符串长度，也没有提供方法修改某个索引的字节码，
不过我们可以将`string`转换为`bytes`,再调用`length`方法获取字节长度，当然可以修改某个索引的字节码。

```

pragma solidity 0.4.23;

contract stobyte{
    string a = "china is very beautiful";
    
    bytes public res = bytes(a);
    uint public length = res.length;
    
    function setAFirstChar() public{
        bytes(a)[0] = "C";
    }
    
    function getA() public constant returns(string){
        return a;
    }
}
```

![字符串转数组.gif](https://upload-images.jianshu.io/upload_images/1053458-88f9f6e76c32a598.gif?imageMogr2/auto-orient/strip)

#### 三、汉字字符串或特殊字符的字符串转换为bytes

```

pragma solidity 0.4.23;

contract stobyte{
    string a = "中国是很美丽的";
    // string a = "a!+&520";
    bytes public res = bytes(a);
    uint public length = res.length;
    
    function setAFirstChar() public{
        bytes(a)[0] = "C";
    }
    
    function getA() public constant returns(string){
        return a;
    }
    
    
}

```

![特殊字符.gif](https://upload-images.jianshu.io/upload_images/1053458-2f080f9a6e0c7972.gif?imageMogr2/auto-orient/strip)

#### 四、bytes可变数组的创建

```

pragma solidity 0.4.23;

contract createBytes{
   bytes  b = new bytes(1);//创建
   
   function bLength()
        public constant
        returns(uint)
   {
       return b.length;
   }
   
   function addToB(byte s,uint index) 
        public
        returns(bytes)
   {
       b[index] = s;
   }
   
   function getB()
        public constant
        returns(bytes)
   {
       return b;
   }
    
    //设置数组长度
    function setBLength(uint length) public
    {
        b.length = length;
    }

    //清空数组
    function clearBytes()
        public
    {

		//b.length = 0;
        delete b;
    }

}  

```

![创建bytes字节数组.gif](https://upload-images.jianshu.io/upload_images/1053458-432e13e929961e7e.gif?imageMogr2/auto-orient/strip)


#### 五、bytes可变数组length和push两个函数的使用案例
```

pragma solidity 0.4.23;

contract createBytes{
   bytes  b = new bytes(1);
   
   function bLength()
        public constant
        returns(uint)
   {
       return b.length;
   }
   
   function getB()
        public constant
        returns(bytes)
   {
       return b;
   }
    
 

   //往字节数组中添加字节
   function pushAbyte(byte s)
        public
   {
       b.push(s);
   }


}  
```


![push的使用.gif](https://upload-images.jianshu.io/upload_images/1053458-c9168dd1fda52bbb.gif?imageMogr2/auto-orient/strip)


