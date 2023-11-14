# WinSNPGT-mkRef

## 💡 General Introduction
We have developed a toolkit to call variant loci on the Windows system, **[WinSNPGT](https://github.com/Min-Zer0/WinSNPGT)**. It can obtain the genotypes of the raw sequencing data for the snp loci specified in our datasets, which is very friendly for those with little Linux operating experience. **WinSNPGT-mkRef** is an extended function plug-in of WinSNPGT that provides users with customized reference genome construction.

The installation and use of this toolkit is described below.

## 🔍 Demo data



## 🌟 Installation

1. Download the compressed package **[Make_RefGenome.zip](https://github.com/Min-Zer0/WinSNPGT-mkRef/raw/main/Make_RefGenome.zip)**
2. Unzip the package to **`Make_RefGenome/`**, and move the entire directory to the previously installed directory **`WinSNPGT`**
3. Enter **`Make_RefGenome/`** and double-click **install.bat** to complete the installation

![](https://img-blog.csdnimg.cn/a91f4fe314734f58a72dac7b54a9678e.png)


## 🌟 Usage
- Double-click **`SNPGT-build`** to initiate the program
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
	    of the species into Make_RefGenome/
	
	 2. Enter species name and Strain information
	```
- Enter species name
- Enter the number of SNP
- Enter the type of population (Inbred or Hybrid)
![](https://img-blog.csdnimg.cn/b4fd852232f1439cba5d4e3d5cf320c1.png)
- After running, open **WinSNPGT** again
- [Step 4](https://github.com/Min-Zer0/WinSNPGT/blob/main/README.md) New data options will appear in Species and Dataset


## 👥 Contacts
> - Jie Qiu (qiujie@shnu.edu.cn)  
> - Min Zhu (zer0min@outlook.com)  
> - Jiaxin Chen (jxchen1217@gmail.com)
