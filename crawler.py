from lxml import html
import requests

def search(url):
  page = requests.get(url)
  tree = html.fromstring(page.text)

  names = tree.xpath('//div[@class="hd"]/a/span[@class="title"][1]/text()')

  print('nams', names)
  for x in names:
    print(x)

if __name__ == '__main__':
  search('https://movie.douban.com/top250')