# 爬取有赞的相关新闻以及新闻来源
# encoding:utf-8


from bs4 import BeautifulSoup
import urllib.request
import requests
import json
import lxml
from lxml import etree
import re
import time
sess = requests.session()


#获取有赞百度资讯内容
def baidu_youzan():
    i = 0
    while i < 360:
        url = 'https://www.baidu.com/s?ie=utf-8&cl=2&medium=0&rtt=1&bsst=1&rsv_dl=news_b_pn&tn=news&word=%E5%BE%AE%E7%9B%9F&rsv_sug3=6&rsv_sug4=398&rsv_sug1=3&rsv_sug2=0&inputT=5472&x_bfe_rqs=03E80&tngroupname=organic_news&pn=' + str(i)
        headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding':'gzip, deflate, br',
            'Accept-Language':'zh-CN,zh;q=0.9',
            'Cache-Control':'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'www.baidu.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'Cache-Control': 'private',
            'Connection': 'Keep-Alive',
            'Content-Encoding': 'gzip',
            'Content-Type': 'text/html;charset=utf-8',
        }
        html = sess.get(url ,headers = headers).text
        # print(html)
        tree = etree.HTML(html)
        point = tree.xpath('//div[@class="result"]')
        for each_point in point:
            list = each_point.xpath('.//h3[@class="c-title"]//text()') + each_point.xpath('.//p[@class="c-author"]//text()')
            print(list)
        i = i+10

baidu_youzan()


#获取有赞搜狗微信公众号内容
def sougou_weixin():
    headers = {
        'cache - control': 'max - age = 0',
        'content - encoding': 'gzip',
        'content - type': 'text / html',
        'accept': 'text / html, application / xhtml + xml, application / xml:q = 0.9, image / webp, image / apng, * / *;q = 0.8',
        'accept - encoding': 'gzip, deflate, br',
        'accept - language': 'zh - CN, zh',
        'cookie':'IPLOC=CN3301; SUID=0EEAE07A2213940A000000005D391629; SUV=1564022264658538; ABTEST=0|1564022315|v1; SNUID=9C7872EB92971CEAC01711F492A3EF07; weixinIndexVisited=1; CXID=BDBC68F201922A70DF4B42C810BFE336; ad=Ukllllllll2Nnzv6lllllV1iI3ylllllWmR$Rkllll9lllllpqxlw@@@@@@@@@@@; usid=0EEAE07A5E37990A000000005D3A50E5; JSESSIONID=aaaG7giKTZFNOg81ObzRw; pgv_pvi=5046660096; pgv_si=s4794969088; sw_uuid=6110806164; sct=18; ld=nlllllllll2NnSBUlllllV1fBiylllllWmR$RkllllYlllllpklll5@@@@@@@@@@; LSTMV=334%2C261; LCLKINT=1807'
    }
    base_url = 'https://weixin.sogou.com/weixin?query=%E6%9C%89%E8%B5%9E%E5%BE%AE%E5%95%86%E5%9F%8E&type=2&page=1&ie=utf8&p=42341200&dp=1'
    html = sess.get(base_url,headers = headers).text
    print(html)
    tree = etree.HTML(html)
    point = tree.xpath('//h3')
    for each_point in point:
        print(each_point.xpath)

sougou_weixin()


#获取有赞搜狗新闻内容

 def sougou_news():
     headers = {
         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
         'Accept-Language': 'zh-CN,zh;q=0.9',
         'Connection': 'keep-alive',
         'Cache-Control': 'max-age=0',
         'Host': 'news.sogou.com',
         'Upgrade-Insecure-Requests': '1',
         "Cookie": "IPLOC=CN3301; SUID=0EEAE07A2213940A000000005D391629; SUV=1564022264658538; SNUID=9C7872EB92971CEAC01711F492A3EF07; CXID=BDBC68F201922A70DF4B42C810BFE336; ad=Ukllllllll2Nnzv6lllllV1iI3ylllllWmR$Rkllll9lllllpqxlw@@@@@@@@@@@; usid=0EEAE07A5E37990A000000005D3A50E5; pgv_pvi=5046660096; pgv_si=s4794969088; newsCity=%u676D%u5DDE; sw_uuid=6110806164; sct=18; ld=nlllllllll2NnSBUlllllV1fBiylllllWmR$RkllllYlllllpklll5@@@@@@@@@@; LSTMV=334%2C261; LCLKINT=1807",
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
         'Content-Type': 'text/html; charset=GBK',
     }
      base_url = 'https://news.sogou.com/news?mode=1&manual=&query=%D3%D0%D4%DE%CE%A2%C9%CC%B3%C7&time=0&sut=6010&lkt=1%2C1564034073579%2C1564034073579&sst0=1564034073684&sort=0&page=1&w=01029901&dr=1'
     i = 1
     while i < 7:
         url = 'https://news.sogou.com/news?query=%D3%D0%D4%DE%CE%A2%C9%CC%B3%C7&page='+str(i)+'&p=40230447&dp=1'
         #抓包
         index_html = sess.get("https://news.sogou.com/", headers=headers)
         print(sess.cookies)
         html = sess.get(url, headers=headers).text
         print(html)
         #砍树
         tree = etree.HTML(html)
         #正则方法
         #author = re.search('<p class="news-from">(.*?)</p>', html, re.S)
         #author = re.findall('<p class="news-from">(.*?)</p>', html, re.S)
         #author = tree.xpath("//p[@class='news-from']")
         #content = re.search('--resulttitle:(.*?)-->', html, re.S)
         #content = re.findall('--resulttitle:(.*?)-->', html, re.S)
         #摘叶
         point = tree.xpath("//div[@class='vrwrap']")
         list_tmp = []
         dict_tmp = {}
         for each_point in point:
             print("".join(each_point.xpath(".//h3[@class='vrTitle']//text()")).strip())
             title = "".join(each_point.xpath(".//h3[@class='vrTitle']//text()")).strip()
             source = "".join(each_point.xpath(".//p[@class='news-from']/text()"))
             #放篮里
             list_tmp.append({"title":title,"source":source})
             print("---------------------------------------------------")
         list_json = json.dumps(list_tmp)
         print(list_tmp)
         print(list_json)
         i = i+1
        
 sougou_news()
