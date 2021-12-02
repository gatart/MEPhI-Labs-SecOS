#!/bin/bash

for ((;;))
do
read line
echo $line | grep "bin" >&2
done
