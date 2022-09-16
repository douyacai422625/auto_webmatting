import os
import sys
from functions import click_upload,uploadImage,changebackground,downloadImage,closepage,click_first_upload_btn,open_website

folder = r'C:\matting\appearance\222\cut_img'

browser = open_website()

names = os.listdir(folder)  # 列举出该目录下所有的文件名
for i,name in enumerate(names):
    path = os.path.join(folder, name)  # 拼接出图片完整路径
    print('对图像: ',path,' 进行处理')
    if i == 0:
        upload_label = click_first_upload_btn(browser,name)
    else:
        upload_label = click_upload(browser,name)

    if upload_label == -1:
        print('佐糖登录过程或者点击上传图片过程中出现问题')
        sys.exit(0)  # 退出当前程序，但不重启shell

    uploadImage(path)
    # 更换背景
    changebackground(browser,name)
    # 下载按钮
    downloadImage(browser,name)
    #下载完毕后需要关闭弹出的对话框
    closepage(browser,name)


print('恭喜！全部完成')