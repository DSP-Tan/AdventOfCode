#!/bin/bash

cat input.txt | tr "\n" "," > format_in.txt
sed -i "s/,,/\\n/g" format_in.txt
