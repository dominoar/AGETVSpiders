BOT_NAME = 'agetv'

SPIDER_MODULES = ['agetv.spiders']
NEWSPIDER_MODULE = 'agetv.spiders'

# 管道
ITEM_PIPELINES = {
    'agetv.pipelines.AgetvPipeline': 200
}

ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
    ':authority': ' www.agemys.cc',
    ':method': 'GET',
    ':path': '/rank',
    ':scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'referer': 'https://www.agemys.cc/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': ' "Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

# 是否启用日志
LOG_ENABLED = True

# 日志使用的编码
LOG_ENCODING = 'utf-8'

# 日志文件(文件名)
LOG_FILE = None

# 日志格式
LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'

# 日志时间格式
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'

# 日志级别 CRITICAL, ERROR, WARNING, INFO, DEBUG
LOG_LEVEL = 'ERROR'

# 如果等于True，所有的标准输出（包括错误）都会重定向到日志，例如：print('hello')
LOG_STDOUT = False

# 如果等于True，日志仅仅包含根路径，False显示日志输出组件
LOG_SHORT_NAMES = False

# 高并发请求时最大延迟时间
AUTOTHROTTLE_MAX_DELAY = 60

# 访问同一个网站的间隔时间
DOWNLOAD_DELAY = 0

# scrapy下载器最大并发数
CONCURRENT_REQUESTS = 100
CONCURRENT_REQUESTS_PER_DOMAIN = 100
CONCURRENT_REQUESTS_PER_IP = 100

# 禁用cookie
COOKIES_ENABLED = False
