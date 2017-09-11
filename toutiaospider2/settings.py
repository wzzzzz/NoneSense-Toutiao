# -*- coding: utf-8 -*-

# Scrapy settings for toutiaospider2 project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'toutiaospider2'

SPIDER_MODULES = ['toutiaospider2.spiders']
NEWSPIDER_MODULE = 'toutiaospider2.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'toutiaospider2 (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'application/json, text/javascript',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'en-US,en;q=0.8,zh-CN;q=0.6,zh;q=0.4,zh-TW;q=0.2',
    'Connection': 'keep-alive',
    'Content-Type':'application/x-www-form-urlencoded',
    'Cookie': 'UM_distinctid=15e5218dc87aad-0b5d9c4e1b865a-31637e01-13c680-15e5218dc8898c; '
              'uuid="w:782e1c2baa364b5a9182ab1db82cd42b"; sso_login_status=1; '
              'login_flag=4ae747980cc1ea2aeed5bbc160a1dcc6; sessionid=de77a32f2bfbe22041254c98763ab48a; '
              'uid_tt=90a4d8a43bcde6c1bad72e7dac306e7d; sid_tt=de77a32f2bfbe22041254c98763ab48a; '
              'sid_guard="de77a32f2bfbe22041254c98763ab48a|1504960845|2591999|Mon\054 09-Oct-2017 12:40:44 GMT"; '
              'csrftoken=366f1576bdbca99792e29482078adffc; WEATHER_CITY=%E5%8C%97%E4%BA%AC; '
              '_ga=GA1.2.811560088.1504960981; _gid=GA1.2.2001402057.1504960981; '
              '__tasessionId=mif033br41504959167322; CNZZDATA1259612802=253699115-1504612769-%7C1504958369; '
              '__utma=24953151.811560088.1504960981.1504961568.1504961568.1; __utmb=24953151.3.10.1504961568; '
              '__utmc=24953151; __utmz=24953151.1504961568.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); '
              'tt_webid=6462276125040985613',
    'Host': 'www.toutiao.com',
    'Referer': 'http://www.toutiao.com',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/60.0.3112.113 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'toutiaospider2.middlewares.Toutiaospider2SpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'toutiaospider2.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'toutiaospider2.pipelines.pipelines.Toutiaospider2Pipeline': None,
    'toutiaospider2.pipelines.pipelines.CommentJsonPipeline': 300
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
