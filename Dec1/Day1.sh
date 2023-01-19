#!/bin/bash

calsPerElf() { cat input.txt | tr "\n" "+" | sed -e "s/++/\n/g" -e "$ s/+$/\n/g" | bc | sort -n ; }

# Part 1
calsPerElf | tail -n1

# Part 2
calsPerElf | tail -n3 | tr "\n" "+" | sed "$ s/+$/\n/g" | bc 
