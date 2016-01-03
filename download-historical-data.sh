#!/bin/bash

wget "http://www.google.com/finance/historical?q=$1&startdate=$2&enddate=$3&output=csv" -O -
