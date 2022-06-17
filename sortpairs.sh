if [ ! -e tmp/ ]
then
	mkdir tmp/
fi
if [ -z "$1" ]
then
	echo "Need order of PAF files to sort on"
	exit
fi
export LC_ALL=C
n=$1
d=1
l=$((n/d))
echo "ORDER $n: Sort compression pairs"
for c in `seq 0 4`
do
	if [ -n "$2" ] && [ $2 -ne $c ] && [ $2 -ne -1 ]
	then
		continue
	fi
 	if [ -e matchings/$n.$c.$l.AB.pafs.txt ]
 	then
	 	SECONDS=0
 		echo "ORDER $n: Sort compression $c: Sort pairs"
 		sort -T tmp/ matchings/$n.$c.$l.AB.pafs.txt > matchings/$n.$c.$l.AB.pafs.sorted.txt
		DIFF=$SECONDS
 		printf "  Case $c: AB PAFs sorted in %.2f seconds\n" $DIFF
 		echo $DIFF > timings/$n.$c.$l.AB.sorttime
 	fi
	if [ -e matchings/$n.$c.$l.CD.pafs.txt ]
	then
		SECONDS=0
		sort -T tmp/ matchings/$n.$c.$l.CD.pafs.txt > matchings/$n.$c.$l.CD.pafs.sorted.txt
		DIFF=$SECONDS
		printf "  Case $c: CD PAFs sorted in %.2f seconds\n" $DIFF
		echo $DIFF > timings/$n.$c.$l.CD.sorttime
	fi
done