from selenium import webdriver
from selenium.webdriver.common.by import By
import time, re

# 基础参数
PATH = "/Users/zhouzhou/code/edgedriver/msedgedriver" #webdriver位置，需要变更为你的本地目录
nga_old = "https://nga.178.com/thread.php?fid=666&page=1" #示例NGA招募区
nga_zm = "https://nga.178.com/thread.php?fid=306&page=1" #示例NGA怀旧服招募区


def run_webdriver(url):
    """
    此函数用于生成 selenium 网页，并访问NGA论坛获取所有标题及链接。
    返回基于Markdown格式的页面信息
    """

    options = webdriver.EdgeOptions()
    options.add_experimental_option("detach", True)  # 不自动关闭浏览器
    driver = webdriver.Edge(PATH, options=options)
    driver.get(url)
    time.sleep(5)  # NGA首页跳转需要等待，不然会卡在403页面

    titles = driver.find_elements(By.XPATH, "//tbody[*]/tr/td[2]/a")
    mkd = []
    for i in titles:
        link = i.get_attribute("href")
        new_i = i.text.replace("[", "<").replace("]", ">")
        newlk = "[{}]({})".format(new_i, link)
        mkd.append(newlk)
    time.sleep(5)
    driver.quit()
    return mkd


def filter(url):
    “”“
    通过关键词过滤标题内容
    ”“”
    all_titles = run_webdriver(url)
    sl = ["台服", "亚服"]

    for s in sl:
        for l in all_titles:
            if l.find(s) == -1:
                continue
            else:
                print(l)


def get_only_link(url):
    """
    使用正则表达式，仅匹配链接
    """
    pattern = re.compile(r"\w*://\w*.\d*.\w*\/\w*\.\w*\?\w*=\d*")
    for i in run_webdriver(url):
        b = pattern.search(i).group(0)
        print(b)


if __name__ == "__main__":
    # slist = run_webdriver(nga)
    filter(nga_old)
    filter(nga_zm)
    #get_only_link(nga_old)
