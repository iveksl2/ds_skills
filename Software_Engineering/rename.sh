#!/bin/bash

for file in *.HTM; do
    name=$(basename "$file" .HTM) 
    echo mv "$file" "$name.html" #echo not run fully the first time. Little trick
done


