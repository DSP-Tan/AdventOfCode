sed -e "s:\/:${PWD}:g"        -e "s:\$ cd:cd:g"  \
    -e "s:dir:mkdir -p:g"     -e "/\$ ls/d" \
    -e '/^[1-9]/s/[^0-9]*//g' -e "/^[1-9]/s/^/touch /g" \
    ../input.txt >> Salve.sh && chmod +x Salve.sh && ./Salve.sh

directs=$(ls -R | grep : | tr ":" " ")
weight_dir(){
   for i in $directs ; do
      ls -R $i | grep [0-9] | awk '{s+=$1} END {print s}' ; done }

# Part 1
weight_dir  | awk '{if($1<= 100000) s+=$1} END {print s}'

# Part 2
Total=70000000; Needs=30000000;
UsedS=$(ls -R . | grep [0-9] | awk '{s+=$1} END {print s}')
Smlst=$( echo "$Needs - ($Total - $UsedS)" | bc )

weight_dir | awk '{if($1 >= '$Smlst') print $1}' | sort -n | head -n1
