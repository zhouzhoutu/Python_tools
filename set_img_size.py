## 这是一个修改图片文字存储大小的脚本

import os,sys

a=input('你希望将文件转成什么大小？ eg:100x100:')

num = len(sys.argv) ## 统计传入的参数量，注包含了函数本身

for i in range(1,num):
    s_name = sys.argv[i]
    os.system("convert -resize %s %s %s"  %(a,s_name,s_name))
    print(s_name,'打印成功')

