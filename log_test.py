
#!/usr/bin/python
#-*-coding:utf-8-*-
import logging
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
log_dir = '{}/log'.format(current_dir)
print(log_dir)
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

FILE_NAME = log_dir + os.sep + "my.log"

logger = logging.getLogger('umd_can')

logger.setLevel(logging.INFO)


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


file_handler = logging.FileHandler(FILE_NAME)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

for i in range(10):
	logger.info('{0}'.format(i))