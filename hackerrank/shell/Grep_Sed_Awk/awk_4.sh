#!/bin/bash
source ~/.bash_profile
cd `dirname $0`

awk 'ORS=NR%2?";":"\n"'

