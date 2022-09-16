import time
from selenium.webdriver.common.by import By
import win32con
import win32gui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
import sys

#打开网页函数
def open_website():
    s = Service(r'C:\Users\li\PycharmProjects\web_matting\chromedriver.exe')
    # 初始化浏览器为chrome浏览器
    browser = webdriver.Chrome(service=s)
    browser.get(r'https://picwish.cn/upload/')
    time.sleep(2)
    # 账户登录
    return_label = sign_in(browser)
    if return_label == -1:
        sys.exit()  # 退出当前程序，但不重启shell
    return browser


def sign_in(browser):
    attemp_num = 0
    while True:
        try:
            sign_in = browser.find_element(By.CSS_SELECTOR, '#header__login')
            sign_in.click()
            return 1
        except:
            print('正在点击网页的登录按钮，请耐心等待')
            attemp_num += 1
            if attemp_num == 60:
                print('十分抱歉您的耐心等待，可能因网络问题，点击登录按钮失败')
                return -1
        else:
            return 1
        finally:
            time.sleep(1)
            return 1

def click_first_upload_btn(browser,name):
    attemp_num = 0
    while True:
        try:
            upload = browser.find_element(By.CSS_SELECTOR, '#app > div:nth-child(5) > section > div > a.upload-btn')
            upload.click()
            return 1
        except:
            print('请先使用电话、微信、QQ等登录佐糖')
            attemp_num += 1
            if attemp_num == 60:
                print('十分感谢您的耐心等待，您在1分钟内未检测到登录佐糖软件，程序将终止的运行')
                return -1
        else:
            return 1
        finally:
            time.sleep(1)

def click_upload(browser,name):
    attemp_num = 0
    while True:
        try:
            # 定位到 重新上传 按钮
            upload = browser.find_element(By.CSS_SELECTOR, '#matting-workshop > div.matting-header.h-55px.flex.justify-between.align-center.bg-white.border-0.border-b.border-solid.border-gray-eee > div.matting-header__right.flex.align-center > div.m-button.text-theme.border-theme.hover\:bg-theme.hover\:text-white.uploadbutton')
            upload.click()
            return 1
        except:
            print('点击重新上传按钮')
            attemp_num += 1
            if attemp_num == 60:
                print('十分感谢您的耐心等待，在1分钟内点击重新上传按钮失败，程序将终止运行')
                print('上传失败的图像名称是: ',name)
                return -1
        else:
            return 1
        finally:
            time.sleep(1)


def uploadImage(filepath):
    dialog = win32gui.FindWindow('#32770', u'打开')  # 对话框
    ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)  # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    button = win32gui.FindWindowEx(dialog, 0, 'Button', None)  # 打开按钮
    if Edit is not None and button is not None:
        time.sleep(0.5)
        win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, filepath)  # 往输入框输入绝对地址
        # print('上传：', filepath)
        time.sleep(0.5)
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点 打开 按钮
        time.sleep(5)

def changebackground(browser,name):
    attemp_num = 0
    while True:
        try:
            # 定位更换背景的按钮
            upload = browser.find_element(By.CSS_SELECTOR,
                                          '#matting-workshop > div.matting-main > div.matting-controls > div.controls__left.flex.align-center > div.changbg')
            upload.click()
            time.sleep(1)

            # 定位白色背景的按钮
            upload = browser.find_element(By.CSS_SELECTOR,
                                          '#matting-workshop > div.matting-main > div.matting-advanced.flex > div.matting-advanced-toolbar.flex-shrink-0 > div.mat__panels > div:nth-child(1) > div > div.bg-replacement__body.flex-1 > div.flex.flex-wrap.justify-between > div.m-item.border')
            upload.click()
            time.sleep(1)

            return 1
        except:
            print(name,' 更换背景颜色')
            attemp_num += 1
            if attemp_num == 60:
                print('十分感谢您的耐心等待，在1分钟内更换背景失败，程序将终止运行')
                print('更换背景颜色失败的图像名称是 : ', name)
                return -1
        else:
            return 1
        finally:
            time.sleep(1)


def downloadImage(browser,name):
    attemp_num = 0
    while True:
        try:
            download = browser.find_element(By.CSS_SELECTOR, '#matting-workshop > div.matting-header.h-55px.flex.justify-between.align-center.bg-white.border-0.border-b.border-solid.border-gray-eee > div.matting-header__right.flex.align-center > div.m-button.text-theme.border-theme.hover\:bg-theme.hover\:text-white.downloadbutton')
            download.click()
            time.sleep(5)

            return 1
        except:
            print('下载',name)
            attemp_num += 1
            if attemp_num == 60:
                print('十分感谢您的耐心等待，在1分钟内下载文件失败，程序将终止运行')
                print('下载失败的图像名称是 : ', name)
                return -1

        else:
            return 1
        finally:
            time.sleep(1)

def closepage(browser,name):
    attemp_num = 0
    while True:
        try:
            # 定位更换背景的按钮
            upload = browser.find_element(By.CSS_SELECTOR,
                                          '#app > div.modal-app > div > div.close')
            upload.click()
            time.sleep(1)
            return 1
        except:
            print('关闭按钮完成验证识别')
            attemp_num += 1
            if attemp_num == 60:
                print('十分感谢您的耐心等待，在1分钟内关闭对话框失败，程序将终止运行')
                print('关闭对话框失败的图像名称是 : ',name)
                return -1

        else:
            return 1
        finally:
            time.sleep(1)