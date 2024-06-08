#!/bin/bash

FILE_PATH='/Users/erenwu/Documents/JamieDemo'
LED_COUNT=2
FAM_FILENAME_LIST='FAM_2.5,FAM_5,FAM_10'
python3 ProcessData.py ${FILE_PATH} ${LED_COUNT} ${FAM_FILENAME_LIST}