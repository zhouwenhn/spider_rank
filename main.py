from scrapy import cmdline
# 简书
cmdline.execute('scrapy crawl jianshu_spider -o rank.csv'.split())
