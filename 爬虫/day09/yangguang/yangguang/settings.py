# Scrapy settings for yangguang project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'yangguang'  # 项目名

SPIDER_MODULES = ['yangguang.spiders']  # 爬虫的位置
NEWSPIDER_MODULE = 'yangguang.spiders'  # 如果新建爬虫，爬虫所在的位置
MONGO_HOST = "127.0.0.1"

# LOG_LEVEL = "WARNING"  # 日志等级
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 浏览器身份表示、用户代理
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # 是否遵守robots协议

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32  # 设置最大并发请求

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3  # 下载延迟，每次请求之前睡3秒
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16  # 单个域名最大并发请求数
# CONCURRENT_REQUESTS_PER_IP = 16  # 单个ip最大并发请求数

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False  # 是否开启cookie，默认是开启的

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False  # 是否开启telnet终端

# Override the default request headers:  # 默认请求头
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'yangguang.middlewares.YangguangSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'yangguang.middlewares.YangguangDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines  # item 管道
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'yangguang.pipelines.YangguangPipeline': 300,
}

# 自动限速，默认关闭
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# http缓存，默认关闭
# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
