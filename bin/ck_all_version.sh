ALL_TAGS=`git tag -l`
OUTPUT=../$1_output/

echo $#
if [ $# -lt 1 ];then
	echo your input is wrong: ch_all_version.sh $filename
	exit;
fi

if [ ! -d $OUTPUT ];then mkdir -p $OUTPUT;fi

for TAG in $ALL_TAGS
do 
	echo "TAG=$TAG $1 ${TAG}_$1"
	git checkout $TAG $1
	cp $1 $OUTPUT/${TAG}_$1
done