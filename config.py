# config.py - Amazon Scraper Configuration

import os
from datetime import datetime

# ==================== API KEYS & AUTHENTICATION ====================
# ScrapeOps Configuration - Get your free API key from https://scrapeops.io/
SCRAPEOPS_API_KEY = os.getenv('SCRAPEOPS_API_KEY', 'api_key_here')

# ==================== SCRAPING TARGETS ====================
# Keywords to scrape (can be overridden via command line)
KEYWORDS = [
    'wireless headphones',
    'laptop',
    'smartphone',
    'gaming chair',
    'bluetooth speaker',
    'coffee machine',
    'running shoes',
    'tablet',
    'smart watch',
    'air fryer',
    'gaming mouse',
    'mechanical keyboard',
    'webcam',
    'monitor',
    'graphics card'
]

# Amazon domains configuration
AMAZON_DOMAINS = {
    'us': 'amazon.com',
    'uk': 'amazon.co.uk',
    'de': 'amazon.de',
    'fr': 'amazon.fr',
    'es': 'amazon.es',
    'it': 'amazon.it',
    'ca': 'amazon.ca',
    'jp': 'amazon.co.jp',
    'au': 'amazon.com.au',
    'in': 'amazon.in',
    'mx': 'amazon.com.mx',
    'br': 'amazon.com.br'
}

# Default domain to scrape
DEFAULT_DOMAIN = 'us'

# ==================== PERFORMANCE & RATE LIMITING ====================
# Scraping performance settings
MAX_PAGES_PER_KEYWORD = 1  # Number of pages to scrape per keyword
MAX_PRODUCTS_PER_PAGE = 20  # Approximate products per page
DELAY_BETWEEN_REQUESTS = 0.1  # Seconds between requests (recommended: 2-5)
RANDOMIZE_DELAY = True  # Add randomness to delays
CONCURRENT_REQUESTS = 50  # Number of concurrent requests (recommended: 1-2)
CONCURRENT_REQUESTS_PER_DOMAIN = 25  # Concurrent requests per domain

# AutoThrottle settings (dynamic delay adjustment)
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 0.1
AUTOTHROTTLE_MAX_DELAY = 1.0
AUTOTHROTTLE_TARGET_CONCURRENCY = 20.0
AUTOTHROTTLE_DEBUG = True

# ==================== USER AGENT CONFIGURATION ====================
# User Agent Strategy: 'dynamic', 'scrapeops', 'fake_useragent', or 'static'
USER_AGENT_STRATEGY = 'scrapeops'  # Recommended: 'scrapeops' or 'fake_useragent'

# Fallback user agents (used when dynamic sources fail)
FALLBACK_USER_AGENTS = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Safari/605.1.15',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
]

# User agent refresh settings
USER_AGENT_REFRESH_INTERVAL = 3600  # Refresh user agents every hour (seconds)
USER_AGENT_CACHE_SIZE = 50  # Number of user agents to cache

# ScrapeOps User Agent API settings
SCRAPEOPS_USER_AGENT_ENDPOINT = 'https://headers.scrapeops.io/v1/user-agents'
SCRAPEOPS_USER_AGENT_PARAMS = {
    'api_key': SCRAPEOPS_API_KEY,
    'num_results': 50,
    'country': 'US'  # US, UK, DE, etc.
}

# ==================== PROXY CONFIGURATION ====================
# Proxy settings
USE_SCRAPEOPS_PROXY = True  # Use ScrapeOps proxy service
USE_CUSTOM_PROXIES = False  # Use custom proxy list below

# Custom proxy list (if USE_CUSTOM_PROXIES is True)
CUSTOM_PROXY_LIST = [
    # Add your proxy servers here
    # 'http://username:password@proxy1:port',
    # 'http://username:password@proxy2:port',
]

# Proxy rotation settings
PROXY_ROTATION_ENABLED = True
PROXY_RETRY_TIMES = 3

# ==================== RETRY & ERROR HANDLING ====================
# Retry configuration
RETRY_TIMES = 2
RETRY_HTTP_CODES = [500, 502, 503, 504, 522, 524, 408, 429, 403]
RETRY_PRIORITY_ADJUST = -1

# Download timeout settings
DOWNLOAD_TIMEOUT = 30  # seconds
DOWNLOAD_WARNSIZE = 33554432  # 32MB

# ==================== CACHING CONFIGURATION ====================
# Cache settings
ENABLE_CACHE = True
CACHE_EXPIRATION_HOURS = 24
CACHE_DIR = 'httpcache'
CACHE_IGNORE_HTTP_CODES = [503, 504, 505, 500, 403, 404, 408]

# ==================== OUTPUT CONFIGURATION ====================
# Output settings
OUTPUT_FORMATS = ['csv', 'json']  # Available: csv, json, xml, jl
OUTPUT_FILENAME_PREFIX = 'amazon_products'
OUTPUT_TIMESTAMP_FORMAT = '%Y%m%d_%H%M%S'

# CSV output settings
CSV_DELIMITER = ','
CSV_QUOTING = 'MINIMAL'  # MINIMAL, ALL, NONNUMERIC, NONE

# JSON output settings
JSON_ENSURE_ASCII = False
JSON_INDENT = 2

# ==================== LOGGING CONFIGURATION ====================
# Logging settings
LOG_LEVEL = 'INFO'  # DEBUG, INFO, WARNING, ERROR, CRITICAL
LOG_FILE = f'logs/amazon_scraper_{datetime.now().strftime("%Y%m%d")}.log'
LOG_FORMAT = '%(levelname)s: %(message)s'
LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'

# Create logs directory if it doesn't exist
os.makedirs('logs', exist_ok=True)

# Enable/disable specific log categories
LOG_SCRAPY_INFO = True
LOG_USER_AGENT_ROTATION = False  # Set to True for debugging
LOG_PROXY_ROTATION = False  # Set to True for debugging
LOG_BLOCKED_REQUESTS = True

# ==================== DATA VALIDATION ====================
# Data validation rules
MIN_PRICE = 0.01
MAX_PRICE = 100000
MIN_STAR_RATING = 0
MAX_STAR_RATING = 5
MIN_NUM_RATINGS = 0
MAX_TITLE_LENGTH = 500

# Product filtering
FILTER_SPONSORED_PRODUCTS = True
FILTER_DUPLICATE_ASINS = True
FILTER_INVALID_PRICES = True

# ==================== FIELDS CONFIGURATION ====================
# Fields to scrape (all available fields)
FIELDS_TO_SCRAPE = [
    'ASIN',
    'Title',
    'StarRating',
    'Price',
    'NumberOfRatings',
    'BestSellerRank',
    'SalesSubRank',
    'SalesSubSubRank',
    'FastestDelivery',
    'SellerOffersCount',
    'DispatchesFrom',
    'SoldBy',
    'IsPrime',
    'CustomerServiceProvider',
    'Brand',
    'AvailableQuantity',
    'ListingDate',
    'IsBuyBoxWinner',
    'FulfilledBy',
    'ShippingCost',
    'DeliveryEstimateFastest',
    'DeliveryEstimateSlowest',
    'DeliveryDaysFastest',
    'DeliveryDaysSlowest',
    'ProductURL',
    'ScrapedAt',
    'Keyword',
    'Domain',
    'PageNumber',
    'SellerName',
    'DeliveryDays',
    'FastestDeliveryDate',
    'SlowestDeliveryDate',
    'Prime'
]

# Required fields (scraping will fail if these are missing)
REQUIRED_FIELDS = ['ASIN', 'Title', 'ProductURL']

# ==================== BROWSER HEADERS ====================
# Additional headers to mimic real browsers
DEFAULT_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Cache-Control': 'max-age=0'
}

# ==================== ADVANCED SETTINGS ====================
REACTOR_THREADPOOL_MAXSIZE = 50
DNSCACHE_ENABLED = True
DNSCACHE_SIZE = 10000
COOKIES_ENABLED = False
REDIRECT_ENABLED = False
# Memory usage settings
MEMUSAGE_ENABLED = True
MEMUSAGE_LIMIT_MB = 4096  # 2GB limit
MEMUSAGE_WARNING_MB = 3072  # Warning at 1.5GB

# Feed export settings
FEED_EXPORT_ENCODING = 'utf-8'
FEED_EXPORT_FIELDS = FIELDS_TO_SCRAPE

# Statistics collection
STATS_CLASS = 'scrapy.statscollectors.MemoryStatsCollector'

# ==================== DEVELOPMENT SETTINGS ====================
# Development and debugging
DEBUG_MODE = False
DEVELOPMENT_MODE = os.getenv('DEVELOPMENT_MODE', 'False').lower() == 'true'

# Test settings for development
if DEVELOPMENT_MODE:
    MAX_PAGES_PER_KEYWORD = 1
    KEYWORDS = ['wireless headphones']  # Limited keywords for testing
    DELAY_BETWEEN_REQUESTS = 5  # More conservative in dev mode
    LOG_LEVEL = 'DEBUG'

# ==================== MONITORING & ALERTS ====================
# ScrapeOps monitoring
SCRAPEOPS_MONITORING_ENABLED = True
SCRAPEOPS_MONITORING_ENDPOINT = 'https://api.scrapeops.io/app/scrapy/stats'

# Performance thresholds for alerts
SUCCESS_RATE_THRESHOLD = 0.8  # 80% success rate minimum
CAPTCHA_RATE_THRESHOLD = 0.1  # 10% CAPTCHA rate maximum
ERROR_RATE_THRESHOLD = 0.2  # 20% error rate maximum

# ==================== HELPER FUNCTIONS ====================
def get_output_filename(format_type='csv', timestamp=None):
    """Generate output filename with timestamp"""
    if timestamp is None:
        timestamp = datetime.now().strftime(OUTPUT_TIMESTAMP_FORMAT)
    return f"{OUTPUT_FILENAME_PREFIX}_{timestamp}.{format_type}"

def get_log_filename():
    """Generate log filename"""
    return LOG_FILE

def validate_config():
    """Validate configuration settings"""
    errors = []
    
    if SCRAPEOPS_API_KEY == 'YOUR_SCRAPEOPS_API_KEY_HERE':
        errors.append("Please set your ScrapeOps API key")
    
    if DELAY_BETWEEN_REQUESTS < 1:
        errors.append("DELAY_BETWEEN_REQUESTS should be at least 1 second")
    
    if CONCURRENT_REQUESTS > 5:
        errors.append("CONCURRENT_REQUESTS should not exceed 5 to avoid getting blocked")
    
    return errors

# Validate configuration on import
_config_errors = validate_config()
if _config_errors:
    print("Configuration warnings:")
    for error in _config_errors:
        print(f"  - {error}")


# ==================== MONGODB CONFIGURATION ====================
# MongoDB connection settings
MONGODB_ENABLED = True
MONGODB_URI = os.getenv('MONGODB_URI', 'mongodb://localhost:27017/')
MONGODB_DATABASE = os.getenv('MONGODB_DATABASE', 'amazon_scraper')

# Collection names
MONGODB_COLLECTIONS = {
    'products': 'products',
    'keywords': 'keywords',
    'scraping_stats': 'scraping_stats'
}

# MongoDB performance settings
MONGODB_BATCH_SIZE = 500  # Batch insert size
MONGODB_CONNECTION_TIMEOUT = 5000  # milliseconds
MONGODB_SOCKET_TIMEOUT = 30000  # milliseconds
MONGODB_MAX_POOL_SIZE = 50

# ==================== DUPLICATE PREVENTION ====================
# Duplicate checking settings
PREVENT_DUPLICATE_PRODUCTS = False  # Don't scrape same ASIN twice
PREVENT_DUPLICATE_KEYWORDS = False  # Don't scrape same keyword twice
DUPLICATE_CHECK_TIMEFRAME_DAYS = 30  # Only check duplicates within X days

# Product duplicate settings
PRODUCT_DUPLICATE_FIELDS = ['ASIN', 'Domain']  # Fields to check for duplicates
PRODUCT_UPDATE_EXISTING = True  # Update existing products with new data

# Keyword duplicate settings
KEYWORD_DUPLICATE_FIELDS = ['keyword', 'domain', 'category']

# ==================== KEYWORD GENERATION ====================
# Keyword generation settings
KEYWORD_GENERATION_ENABLED = True
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY_HERE')
OPENAI_MODEL = 'gpt-3.5-turbo'  # or 'gpt-4'
OPENAI_MAX_TOKENS = 1000
OPENAI_TEMPERATURE = 0.7

# Categories for keyword generation
PRODUCT_CATEGORIES = [
    'Electronics',
    'Home & Kitchen',
    'Sports & Outdoors'
    # 'Health & Personal Care',
    # 'Clothing & Accessories',
    # 'Books',
    # 'Toys & Games',
    # 'Automotive',
    # 'Beauty',
    # 'Office Products'
]

# Keyword generation parameters
KEYWORDS_PER_CATEGORY = 10  # How many keywords to generate per category
GENERATION_PROMPTS_COUNT = 1  # How many times to generate keywords (for variety)
MAX_KEYWORDS_PER_RUN = 50  # Maximum keywords to process in one scraping run

# ==================== KEYWORD GENERATION CONFIGURATION ====================
# OpenAI keyword generation prompt template
KEYWORD_GENERATION_PROMPT = """Generate a list of {count} high-potential, SEO-optimized keywords for trending Amazon products in the {category} category for the year 2025, specifically for the {market_context}.

Focus on:
- Emerging {category_lower} trends (e.g. {trends})
- Keywords that reflect current user intent and purchase behavior
- A mix of long-tail and short-tail keywords
- Amazon-specific product search terms
- Products that are likely to be popular in 2025

The output should be a flat list of {count} unique keywords, sorted by trend relevance, without any extra commentary."""

# Category-specific trending focus areas
CATEGORY_TRENDS = {
    'Electronics': 'smart home, wearables, AI gadgets, portable devices, gaming accessories, wireless charging, VR/AR devices, streaming devices',
    'Home & Kitchen': 'smart kitchen appliances, air purifiers, robot vacuums, meal prep tools, eco-friendly products, multi-functional gadgets',
    'Sports & Outdoors': 'fitness trackers, smart exercise equipment, outdoor tech, recovery devices, sustainable gear, home gym equipment',
    'Health & Personal Care': 'wellness tech, skincare devices, air quality monitors, mental health apps, fitness supplements, sleep optimization',
    'Clothing & Accessories': 'sustainable fashion, smart textiles, athleisure, minimalist accessories, tech-integrated clothing, comfort wear',
    'Beauty': 'skincare tech, clean beauty, personalized products, anti-aging devices, sustainable packaging, K-beauty trends',
    'Automotive': 'electric vehicle accessories, smart car gadgets, dash cams, wireless charging mounts, car air purifiers',
    'Office Products': 'remote work tools, ergonomic accessories, productivity gadgets, digital organization, standing desk accessories',
    'Books': 'self-improvement, productivity guides, mental health resources, sustainable living, technology trends, career development',
    'Toys & Games': 'educational STEM toys, smart toys, eco-friendly options, screen-free activities, interactive learning, creativity kits'
}

# Domain-specific market context
DOMAIN_MARKET_CONTEXT = {
    'us': 'US market',
    'uk': 'UK market', 
    'de': 'German market',
    'fr': 'French market',
    'es': 'Spanish market',
    'it': 'Italian market',
    'ca': 'Canadian market',
    'jp': 'Japanese market',
    'au': 'Australian market',
    'in': 'Indian market'
}

# OpenAI system prompt
OPENAI_SYSTEM_PROMPT = "You are a keyword research expert specializing in Amazon product searches and current market trends. Generate only the most relevant and popular search terms that real customers would use when searching for products on Amazon."

# Keyword filtering settings
KEYWORD_MIN_LENGTH = 3
KEYWORD_MAX_LENGTH = 100
KEYWORD_MAX_WORDS = 6
KEYWORD_SKIP_PATTERNS = [':', '?', '!', ';', '(', ')', '[', ']', 'Here are', 'Keywords:', 'List:', 'Amazon', 'products']

# Default trending topics fallback
DEFAULT_TRENDING_TOPICS = 'smart home, wearables, AI gadgets, portable devices, gaming accessories, wireless charging, VR/AR devices, streaming devices'

# ==================== PERFORMANCE OPTIMIZATION ====================
# Database performance settings
USE_MONGODB_INDEXES = True  # Create indexes for fast lookups
ENABLE_ASYNC_DB_OPERATIONS = True  # Use async operations where possible
CACHE_DB_QUERIES = True  # Cache frequent queries in memory
DB_QUERY_CACHE_SIZE = 1000  # Number of queries to cache
DB_QUERY_CACHE_TTL = 3600  # Cache TTL in seconds

# Scraping optimization with DB
BATCH_KEYWORD_PROCESSING = True  # Process keywords in batches
PRELOAD_SCRAPED_ASINS = True  # Load scraped ASINs into memory at start
ASIN_CACHE_SIZE = 10000  # Number of ASINs to keep in memory cache

# ==================== DATABASE SCHEMA ====================
# Keyword document schema
KEYWORD_SCHEMA = {
    'keyword': str,  # The search keyword
    'category': str,  # Product category
    'domain': str,   # Amazon domain (us, uk, etc.)
    'is_scraped': bool,  # Whether this keyword has been scraped
    'scraped_at': 'datetime',  # When it was scraped
    'created_at': 'datetime',  # When keyword was generated
    'priority': int,  # Scraping priority (1-10)
    'generated_by': str,  # 'openai', 'manual', 'auto'
    'scraping_attempts': int,  # Number of scraping attempts
    'last_attempt_at': 'datetime',  # Last scraping attempt
    'success_count': int,  # Number of successful scrapes
    'error_count': int,  # Number of failed scrapes
    'products_found': int,  # Number of products found for this keyword
}

# Product document schema  
PRODUCT_SCHEMA = {
    'ASIN': str,  # Primary identifier
    'keyword': str,  # Keyword used to find this product
    'domain': str,  # Amazon domain
    'scraped_at': 'datetime',  # When product was scraped
    'updated_at': 'datetime',  # Last update time
    'scrape_count': int,  # Number of times scraped
    
    # Product basic information
    'Title': str,  # Product title
    'ProductURL': str,  # Full Amazon product URL
    'Brand': str,  # Brand/manufacturer name
    
    # Ratings and reviews
    'StarRating': float,  # Average star rating (1-5 scale)
    'NumberOfRatings': int,  # Total number of ratings/reviews
    
    # Pricing information
    'Price': float,  # Current price in USD
    'ShippingCost': float,  # Shipping cost (0.0 if free)
    
    # Rankings
    'BestSellerRank': int,  # Best seller rank position
    'SalesSubRank': str,  # Sales category rank
    'SalesSubSubRank': str,  # Sub-category rank (can be None)
    
    # Delivery information
    'FastestDelivery': str,  # Fastest delivery option text
    'FastestDeliveryDate': str,  # Fastest delivery date
    'SlowestDeliveryDate': str,  # Slowest delivery date
    'DeliveryDays': int,  # Estimated delivery days
    'DeliveryEstimateFastest': str,  # Fastest delivery estimate
    'DeliveryEstimateSlowest': str,  # Slowest delivery estimate
    'DeliveryDaysSlowest': int,  # Slowest delivery in days
    
    # Seller information
    'SoldBy': str,  # Seller name
    'SellerName': str,  # Seller display name
    'FulfilledBy': str,  # Fulfillment provider (usually Amazon)
    'DispatchesFrom': str,  # Shipping origin location
    'CustomerServiceProvider': str,  # Customer service provider
    'SellerOffersCount': int,  # Number of seller offers (can be None)
    'IsBuyBoxWinner': bool,  # Whether this is the buy box winner
    
    # Prime and availability
    'IsPrime': bool,  # Prime eligible
    'Prime': bool,  # Prime status
    'AvailableQuantity': str,  # Stock status (e.g., "In Stock")
    
    # Listing information
    'ListingDate': str,  # When product was first listed
    'PageNumber': int,  # Search result page number
    'Keyword': str,  # Search keyword used
    'Domain': str,  # Amazon domain
    'ScrapedAt': str,  # When product was scraped (ISO format)
}

# ==================== HELPER FUNCTIONS ====================
def get_mongodb_url():
    """Get MongoDB connection URL"""
    return MONGODB_URI

def get_collection_name(collection_type):
    """Get collection name for given type"""
    return MONGODB_COLLECTIONS.get(collection_type, collection_type)

def should_prevent_duplicates(item_type):
    """Check if duplicates should be prevented for item type"""
    if item_type == 'product':
        return PREVENT_DUPLICATE_PRODUCTS
    elif item_type == 'keyword':
        return PREVENT_DUPLICATE_KEYWORDS
    return False