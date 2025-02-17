if [ -z "$1" ]
then
	echo "Use ./driver.sh n to enumerate good matrices of odd orders n divisible by 3"
	echo "or ./driver.sh n m to enumerate good matrices of odd orders between n and m divisible by 3"
	exit
else
	if [ -z "$2" ]
	then
		u=$1
	else
		u=$2
	fi
	if [ $((u%2)) -eq 0 ]
	then
		echo "Order must be odd"
		exit
	fi
	mkdir -p bin
	for n in `seq $1 2 $u`
	do
		make bin/generate_matching_instances_comp_$n bin/generate_pairedmatchings_$n bin/join_pairedmatchings_$n bin/remove_equivalent_matchedpairs_$n
		bin/generate_matching_instances_comp_$n
		bin/generate_pairedmatchings_$n
		./sortpairs.sh $n
		bin/join_pairedmatchings_$n
		bin/remove_equivalent_matchedpairs_$n
	done
fi
