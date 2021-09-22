#!/bin/zsh
cd `dirname $0` || exit 1
/opt/anaconda3/envs/nlp/bin/python auto_sign_in.py >> run.log 2>&1

# crontab 执行
# 每天10点执行
# 0 10 * * * /Users/ken/PycharmProjects/hm_15/spider/exercise/cartoon/sign_in.sh >> /Users/ken/PycharmProjects/hm_15/spider/exercise/cartoon/run.log 2>&1