import config

TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'

BOT_NAME = "amazon_scraper"

SPIDER_MODULES = ["amazon_scraper.spiders"]
NEWSPIDER_MODULE = "amazon_scraper.spiders"

ADDONS = {}
LOG_STDOUT=False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "amazon_scraper (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False
COOKIES_ENABLED = False
REDIRECT_ENABLED = False
METAREFRESH_ENABLED = False

# Concurrency and throttling settings
CONCURRENT_REQUESTS = config.CONCURRENT_REQUESTS
CONCURRENT_REQUESTS_PER_DOMAIN = config.CONCURRENT_REQUESTS
DOWNLOAD_DELAY = config.DELAY_BETWEEN_REQUESTS
RANDOMIZE_DOWNLOAD_DELAY = True

DOWNLOAD_TIMEOUT = config.DOWNLOAD_TIMEOUT
DOWNLOAD_WARNSIZE = 0
DNSCACHE_ENABLED = True
DNSCACHE_SIZE = 10000

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": 'en-GB,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "amazon_scraper.middlewares.AmazonScraperSpiderMiddleware": 543,
#}

# ScrapeOps Configuration from config
SCRAPEOPS_API_KEY = config.SCRAPEOPS_API_KEY
SCRAPEOPS_PROXY_ENABLED = True
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = False  # Disabled to use our custom rotation
SCRAPEOPS_FAKE_BROWSER_HEADER_ENABLED = True

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'amazon_scraper.middlewares.DynamicUserAgentMiddleware': 400,
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
    'amazon_scraper.middlewares.AmazonScraperDownloaderMiddleware': 543,
    'scrapeops_scrapy.middleware.retry.RetryMiddleware': 550, 
    'scrapy.downloadermiddlewares.retry.RetryMiddleware': None,
    'scrapy.downloadermiddlewares.offsite.OffsiteMiddleware': None,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
  'scrapeops_scrapy.extension.ScrapeOpsMonitor': 500, 
}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "amazon_scraper.pipelines.ValidationPipeline": 100,           # Validate first
    "amazon_scraper.pipelines.DuplicatesPipeline": 200,           # Memory duplicate backup
    "amazon_scraper.pipelines.DatabaseDuplicatesPipeline": 250,   # Filter DB duplicates  
    "amazon_scraper.pipelines.AmazonScraperPipeline": 300,        # Your existing processing
    "amazon_scraper.pipelines.MongoDBPipeline": 400,              # Store in MongoDB
    "amazon_scraper.pipelines.JsonWriterPipeline": 500,           # Output to JSON
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = config.DELAY_BETWEEN_REQUESTS
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = config.AUTOTHROTTLE_MAX_DELAY
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = config.AUTOTHROTTLE_TARGET_CONCURRENCY
# Enable showing throttling stats for every response received:
AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
HTTPCACHE_ENABLED = config.ENABLE_CACHE
HTTPCACHE_EXPIRATION_SECS = config.CACHE_EXPIRATION_HOURS * 3600
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"

# Logging configuration from config
LOG_LEVEL = config.LOG_LEVEL
LOG_FILE = config.LOG_FILE

# Configure feed exports
FEEDS = {
    f'{config.OUTPUT_FILENAME_PREFIX}.csv': {
        'format': 'csv',
        'overwrite': True,
    },
    f'{config.OUTPUT_FILENAME_PREFIX}.json': {
        'format': 'json',
        'overwrite': True,
    },
}

# ScrapeOps Monitoring
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'
SCRAPEOPS_FAKE_BROWSER_HEADER_ENDPOINT = 'https://headers.scrapeops.io/v1/browser-headers'
SCRAPEOPS_MONITORING_ENABLED = True
SCRAPEOPS_MONITORING_ENDPOINT = 'https://api.scrapeops.io/app/scrapy/stats'

# Retry configuration from config
RETRY_TIMES = config.RETRY_TIMES
RETRY_HTTP_CODES = config.RETRY_HTTP_CODES

# Configure telnet console
TELNETCONSOLE_ENABLED = False

FEED_EXPORT_BATCH_ITEM_COUNT = 1000
STATS_DUMP = False
COMPRESSION_ENABLED = True
DOWNLOAD_FAIL_ON_DATALOSS = False