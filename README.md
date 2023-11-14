# WinSNPGT-mkRef

## 💡 总体介绍
- 我们开发了一个在Windows系统上调用变种位点的工具包 **[WinSNPGT](https://github.com/Min-Zer0/WinSNPGT)**，对于那些Linux操作经验很少的人来说非常友好。它可以获得我们数据集中指定的 SNP 位点的原始测序数据的基因型。 WinSNPGT-mkRef为WinSNPGT的扩展功能插件，提供用户自定义构建参考基因组。
- 以下是该工具包的安装和使用说明。


## 🔍 测试数据
- 


## 🌟 安装

- 下载 **[Make_RefGenome.zip](https://github.com/Min-Zer0/WinSNPGT-mkRef/raw/main/Make_RefGenome.zip)** 压缩包
-  解压到 **`Make_RefGenome/`**, 并移入 **`WinSNPGT`** 安装目录下
-  进入 **`Make_RefGenome/`**，双击 **install.bat**, 即可完成安装
![](https://img-blog.csdnimg.cn/a91f4fe314734f58a72dac7b54a9678e.png)


## 🌟 使用方法
- 双击 **`SNPGT-build`** 启动软件
	```black
	#########################################################################
	#     _____ _   ______  ____________            __          _ __    __  #
	#    / ___// | / / __ \/ ____/_  __/           / /_  __  __(_) /___/ /  #
	#    \__ \/  |/ / /_/ / / __  / /    ______   / __ \/ / / / / / __  /   #
	#   ___/ / /|  / ____/ /_/ / / /    /_____/  / /_/ / /_/ / / / /_/ /    #
	#  /____/_/ |_/_/    \____/ /_/             /_.___/\__,_/_/_/\__,_/     #
	#                                                                       #
	#########################################################################
		Program: SNPGT-build (Tools for make RefGenome)
	
	Usage:
	 1. Put the whole genome reference sequence and SNP site information(bim file)
	    of the species into 00.Make_Reference_Genome/
	
	 2. Enter species name and Strain information
	```
- 输入物种名
- SNP位点数量
- 群体纯杂合类型
![](https://img-blog.csdnimg.cn/b4fd852232f1439cba5d4e3d5cf320c1.png)
- 运行结束后，再次打开 **WinSNPGT**
- [教程步骤 4](https://blog.csdn.net/NBRWzm/article/details/134232418) 选择物种与数据集（Species and Dataset）中会出现新数据选项


## 👥 联系我们
> - 邱杰 Jie Qiu (qiujie@shnu.edu.cn)  
> - 朱旻 Min Zhu (zer0min@outlook.com)  
> - 陈嘉欣 Jiaxin Chen (jxchen1217@gmail.com)
