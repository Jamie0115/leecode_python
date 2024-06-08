set FILE_PATH=C:/Users/funny/Desktop/result
set LED_COUNT=2
set FAM_FILENAME_LIST=FAM_2.5,FAM_5,FAM_10

python ProcessData.py %FILE_PATH% %LED_COUNT% %FAM_FILENAME_LIST%
pause