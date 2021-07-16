# 输出目录的缺省值
o=./
while getopts ":i:o:" opt
do
    case $opt in
        i)
        i=`echo $OPTARG`
        ;;
        o)
        o=`echo $OPTARG`
        ;;
        ?)
        echo "未知参数"
        exit 1;;
    esac
done
# 激活conda环境
source /opt/anaconda3/bin/activate nlp
# `pwd`表示当前终端的路径，而不是当前shell脚本所在的路径
python /Users/ken/PycharmProjects/hm_15/爬虫/exercise/aozora/uncompress.py `pwd` $i $o