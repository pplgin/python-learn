from lxml import html
import requests
import pprint

import pymysql.cursors
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root',
                       db='blog',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

def search(url):
  page = requests.get(url)
  tree = html.fromstring(page.text)

  mvEles = tree.xpath('//div[@class="item"]')

  movies = [];

  try:
    for ele in mvEles:
      movie = {}
      img = ele.xpath('./div[@class="pic"]//@src')
      link = ele.xpath('./div[@class="info"]//a/@href')
      names = ele.xpath('./div[@class="info"]//a//span/text()')
      desc = ele.xpath('.//p/text()')
      keywords = ele.xpath('.//span[@class="inq"]/text()')
      with conn.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `movies` (`link`, `name`, `desc`,`keywords`, `img`) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (''.join(link) ,''.join(names), ''.join(desc).strip(), ''.join(keywords), ''.join(img)))
      conn.commit()
  finally:
    conn.close();

  # print('nams', names)
  # for x in names:
  #   print(x)

if __name__ == '__main__':
  search('https://movie.douban.com/top250')