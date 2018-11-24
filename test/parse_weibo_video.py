import os
from html.parser import HTMLParser

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

path = 'https://weibo.com/tv/v/H42E0hvp1?fid=1034:4309634744303951'


class WeiboHtmlParse(HTMLParser):

    def error(self, message):
        pass

    def __init__(self, *, convert_charrefs=True):
        super().__init__(convert_charrefs=convert_charrefs)
        self.video_data = []

    def handle_starttag(self, tag, attrs):

        if tag == 'video':
            for attr in attrs:
                url = attr[1]
                p = os.path.splitext(url)
                suffix = p[1]
                if suffix.find('mp4'):
                    self.video_data.append('https:' + url)


with webdriver.Chrome(ChromeDriverManager().install()) as browser:
    browser.get(path)

    # 添加条件等待
    WebDriverWait(browser, 20, 0.5).until(
        expected_conditions.presence_of_all_elements_located((By.TAG_NAME, 'video')))
    data = browser.page_source

    parser = WeiboHtmlParse()
    parser.feed(data)
    # 写文件
    with open('/Users/mac/Downloads/result.txt', 'a') as k:
        for s in parser.video_data:
            k.write(s + '\n------------------\n')
