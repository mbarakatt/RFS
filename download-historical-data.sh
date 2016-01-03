#!/bin/bash

curl "http://www.google.co.uk/finance/historical" \
    "\?q=$1" \
    "\&startdate=$2" \
    "\&enddate=$3" \
    "\&output=csv"
