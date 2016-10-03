from lxml import etree
import time
import urllib.request

class Downloader():

    def __init__(self, url):
        self.url = url
        self.contents = 'a'

    def download(self):

     #   try:
        url = urllib.request.urlopen(self.url)
        self.contents = url.read().decode('utf-8')
      #  response = browser.getcode()
       # print(browser)
      #  if(response == 200):
       #     print('get response success')

      #  self.contents = browser.read()
       # print(self.contents)
   #     except:
     #       raise HTTPError(None, None, None, None, None)


class HackerNewsParser(Downloader):
    def _init_(self):

       # url = 'https://news.ycombinator.com/'
        Downloader.__init__(self)


    def get_itemlist(self):

        Downloader.download(self)
        if self.contents:

            path = "/home/raymond/PycharmProjects/HQ/results/hackernews_{0}.txt".format(time.strftime('%M_%H_%d_%m_%Y'))
            thefile = open(path, 'w')

            thefile.write(self.url + "\n\n" + time.strftime("%d %B, %Y") + "\n\n" + time.strftime("%H:%M") + "\n\n\n")

            tree = etree.HTML(self.contents)
            print(tree)
            xpaths = [#rank
                      "string((//tr[@class='athing']/td[@class = 'title']/span[@class='rank']/text())[{0}])", \
                      #article link
                      "string((//tr[@class='athing']/td[@class = 'title']/a/@href)[{0}])", \
                      #article name
                      "string((//tr[@class='athing']/td[@class = 'title']/a/text())[{0}])", \
                      #article site link
                      "string((//tr[@class='athing']/td[@class = 'title']/span[@class = 'sitebit comhead']/a/@href)[{0}])", \
                      #scores
                      "string((//td[@class='subtext']/span[@class='score']/text())[{0}])", \
                      #how old the article is
                      "string((//td[@class='subtext']/span[@class='age']/a/text())[{0}])", \
                      #comment page link ( same as "string((//td[@class='subtext']/span[@class='age']/a/@href)[{0}])"   )
                      "string((//td[@class='subtext']/a[contains(text(), 'comment')]/@href)[{0}])", \
                      #amount of comments
                      "string((//td[@class='subtext']/a[contains(text(), 'comment')]/text())[{0}])"]

            for rank in range(1,10):

                for path_num in range(len(xpaths)):

                    item = tree.xpath(xpaths[path_num].format(rank))

                    if (path_num == 4) or (path_num == 7):
                        item = "https://news.ycombinator.com/{0}".format(item)
                    thefile.write(item +"\n")

                thefile.write("\n\n")

            thefile.close()








