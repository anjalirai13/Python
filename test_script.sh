#!/bin/bash

for (( i=0; i<15; i++))
do
  if [ $i -le 4 ]; then
    echo "Scenario 1"
  elif [ $i -le 9 ]; then
    echo "Scenario 2"
  else
    echo "Scenario 3"
  fi
done