#!/bin/bash

mkdir -p AOC_7_Bash && cd AOC_7_Bash 
echo "#!/bin/bash" > Salve.sh

sed "s@\/@${PWD}@g" ../example.txt >> Salve.sh
sed -i "s@\$ cd@cd@g"                 Salve.sh
sed -i "s@dir@mkdir -p@g"             Salve.sh
sed -i "/\$ ls/d"                     Salve.sh
sed -i '/^[1-9]/s/[^0-9]*//g'         Salve.sh
sed -i "/^[1-9]/s/^/touch /g"         Salve.sh

chmod +x Salve.sh
./Salve.sh

ls -R . | grep "[0-9]" | awk '{s+=$1} END {print s}'
ls -R a | grep "[0-9]" | awk '{s+=$1} END {print s}'
ls -R d | grep "[0-9]" | awk '{s+=$1} END {print s}'

cd ../
