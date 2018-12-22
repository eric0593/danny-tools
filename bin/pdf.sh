files=`find . -name "*.pdf" | tr " " "\?"`
echo $files
sum=0
for file in $files
do
let sum=sum+1
base=`basename "$file"`
echo base="$base.$sum.0001"
pdftk "$file" burst
mv pg_0001.pdf $base.$sum.0001
rm -rf pg_*.pdf
done
pdftk *0001 cat output merge.pdf
