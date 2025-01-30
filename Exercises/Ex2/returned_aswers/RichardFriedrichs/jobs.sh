#!/bin/bash

for i in {1..10}
do
    ./runnable $i > output_bash_$i.txt &
done