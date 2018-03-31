# Redis数据库地址
REDIS_HOST = '127.0.0.1'

# Redis端口
REDIS_PORT = 6379

# Redis密码，如无填None
REDIS_PASSWORD = None

REDIS_KEY = 'proxies'

# 代理分数
MAX_SCORE = 100
MIN_SCORE = 90
INITIAL_SCORE = 90

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 50000
#代理池最低数量界限
POOL_LOWER_THRESHOLD = 1800

# 检查周期
TESTER_CYCLE = 20
# 获取周期
GETTER_CYCLE = 300

# 测试API，建议抓哪个网站测哪个
# TEST_URL = 'http://www.baidu.com'
TEST_URL = 'http://www.xiaohongshu.com/'

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5556

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIZE = 30
