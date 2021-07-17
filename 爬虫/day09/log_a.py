import logging

# 设置日志的输出样式
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("this is an info")
    # 2021-07-17 23:37:15,799 - log_a.py[line:10] - INFO: this is an info
