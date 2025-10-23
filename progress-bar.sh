#!/bin/bash

total_steps=5

for (( progress=0; progress<=total_steps; progress++ )); do
  let filled=progress*20/total_steps
  bar=""
  for ((i=0; i <filled; i++)); do
    bar="${bar}#"
  done

  echo -ne "\r[${bar}]"
  sleep 0.5

done

