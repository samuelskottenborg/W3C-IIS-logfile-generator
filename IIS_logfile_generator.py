# IIS sample log generator for testing purposes.
# Log file format is:
# date time s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) cs(Referer) sc-status sc-substatus sc-win32-status time-taken

# Please change the following variables to suit your needs

num_files = 10
num_lines = 1000
date_start = "2018-01-01"
date_end = "2018-01-01"
log_path = r"C:\Users\user\Documents\logs"


import datetime
import random
import os
import sys

# Start at date_start and end at date_end. Create num_files files with num_lines lines each. Log file name format is u_exYYMMDDHH.log.
