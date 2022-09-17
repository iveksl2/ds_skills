#!/usr/bin/env bash

# https://www.youtube.com/watch?v=0XI8FPVnNzY

export IMDB="https://www.imdb.com"
export TITLE="tt0944947"
curl "${IMDB}/title/${TITLE}/episodes?season=1"

seq 8 | parallel --jobs 1 --bar 'curl -s "${IMDB}/title/${TITLE}/episodes?season={}" > season-{}.html'

cat season-*.html | grep "ipl-rating-star__rating" | grep "\." | tr -cd '.[0-9]\n' > ratings
cat season-*.html | grep ", Ep" | tr -dc ',[0-9]\n' > episodes
paste -d, <(seq $(<ratings wc -l)) episodes ratings

paste -d, episodes ratings | nl -w1 -s, > ratings.csv 

# https://fedingo.com/how-to-add-header-in-csv-file-using-shell-script/
echo "id,season,episode,rating" > header.csv && cat ratings.csv >> header.csv && mv header.csv ratings.csv 



