#!/bin/sh
cd `dirname $0` || exit 1
/opt/anaconda3/envs/nlp/bin/python test.py >> run.log 2>&1

# crontab 执行
# * * * * * /Users/ken/PycharmProjects/hm_15/爬虫/day12/run.sh >> /Users/ken/PycharmProjects/hm_15/爬虫/day12/run.log 2>&1