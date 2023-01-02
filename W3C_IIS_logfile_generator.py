# IIS W3C sample log generator for testing purposes.
# Log file format is:
# date time s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) cs(Referer) sc-status sc-substatus sc-win32-status time-taken
# 2022-10-11 16:26:48 127.0.0.1 GET /wpad.dat - 80 - 127.0.0.1 WinHttp-Autoproxy-Service/5.1 - 404 0 2 0
# 2022-12-07 18:54:03 192.1.0.1 GET /45187jj4 - 80 - 192.168.0.123 pct - 210 0 0 409

import datetime
import random
import os

# Please change the following variables to suit your needs
num_files = 10
min_num_lines = 100
max_num_lines = 10000
date_start = "2022-12-01"
date_end = "2023-5-01"
log_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "logs")

# Create log path if it doesn't exist
if not os.path.exists(log_path):
    os.makedirs(log_path)
     
# Create list of dates
date_start = datetime.datetime.strptime(date_start, "%Y-%m-%d")
date_end = datetime.datetime.strptime(date_end, "%Y-%m-%d")
date_list = [date_start + datetime.timedelta(days=x) for x in range(0, (date_end-date_start).days + 1)]

# Create list of local and external IPs (1 pr. every 100 request/line).
ip_list = []

# Local IPs
for i in range(0, int(min_num_lines * num_files / 50 + 1)):
    ip_list.append("192.168.0." + str(random.randint(1, 254)))
    
# External IPs
for i in range(0, int(min_num_lines * num_files / 50 + 1)):
    ip_list.append(str(random.randint(1, 254)) + "." + str(random.randint(1, 254)) + "." + str(random.randint(1, 254)) + "." + str(random.randint(1, 254)))
    
# Repeat some IPs multiple times to get a more realistic distribution 
for i in range(0, int(min_num_lines * num_files / 10 + 1)):
    ip_list[random.randint(0, len(ip_list) - 1)] = ip_list[random.randint(0, len(ip_list) - 1)]
    
# Create list of user agents (list from https://www.useragents.me/)
ua_pct = {'ua': {'0': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', '1': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '2': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0', '3': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', '4': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.2 Safari/605.1.15', '5': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', '6': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.46', '7': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.67', '8': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', '9': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36', '10': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:107.0) Gecko/20100101 Firefox/107.0', '11': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', '12': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.42', '13': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:108.0) Gecko/20100101 Firefox/108.0', '14': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35', '15': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.3.818 Yowser/2.5 Safari/537.36', '16': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 SECSSOBrowserChrome', '17': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36 Edg/93.0.961.52', '18': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0', '19': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.62', '20': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36', '21': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', '22': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0', '23': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', '24': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0', '25': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586', '26': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.3.818 Yowser/2.5 Safari/537.36', '27': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36', '28': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0', '29': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54', '30': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.42', '31': 'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 Edg/105.0.1343.27', '32': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0', '33': 'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko', '34': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362', '35': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.42', '36': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36', '37': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36', '38': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.102 Safari/537.36 Edg/104.0.1293.63', '39': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36', '40': 'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36', '41': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}, 'pct': {'0': 36.990199178, '1': 26.5570660765, '2': 6.7341131837, '3': 5.0584887765, '4': 3.0350932659, '5': 2.0233955106, '6': 1.8969332912, '7': 1.7704710718, '8': 1.2646221941, '9': 1.2646221941, '10': 0.7587733165, '11': 0.7587733165, '12': 0.7587733165, '13': 0.7587733165, '14': 0.6323110971, '15': 0.6323110971, '16': 0.6323110971, '17': 0.5058488776, '18': 0.5058488776, '19': 0.5058488776, '20': 0.5058488776, '21': 0.5058488776, '22': 0.5058488776, '23': 0.5058488776, '24': 0.3793866582, '25': 0.3793866582, '26': 0.3793866582, '27': 0.2529244388, '28': 0.2529244388, '29': 0.2529244388, '30': 0.2529244388, '31': 0.2529244388, '32': 0.2529244388, '33': 0.2529244388, '34': 0.2529244388, '35': 0.2529244388, '36': 0.2529244388, '37': 0.2529244388, '38': 0.2529244388, '39': 0.2529244388, '40': 0.2529244388, '41': 0.2529244388}}
user_agents = random.choices(list(ua_pct['ua'].values()), list(ua_pct['pct'].values()), k=100)
user_agents = [i.replace(" ", "") for i in user_agents]

# Create list of random common URI stems for use in the test
common_uri_stems = []
for i in range(0, 100):
    common_uri_stems.append("/" + str(random.randint(0, 1000000)))
    
# Create list of request methods and status codes
request_methods = ["GET", "POST", "PUT", "DELETE", "HEAD", "OPTIONS", "CONNECT", "TRACE", "PATCH"]
status_codes = ["200", "201", "202", "203", "204", "205", "206", "207", "208", "226", "300", "301", "302", "303", "304", "305", "306", "307", "308", "400", "401", "402", "403", "404", "405", "406", "407", "408", "409", "410", "411", "412", "413", "414", "415", "416", "417", "418", "421", "422", "423", "424", "425", "426", "428", "429", "431", "451", "500", "501", "502", "503", "504", "505", "506", "507", "508", "510", "511"]

# Generate logs
for i in range(0, num_files):
    # Create file name (random date)
    file_name = "u_ex" + date_list[random.randint(0, len(date_list) - 1)].strftime("%Y%m%d") + ".log"
    file_name = os.path.join(log_path, file_name)
    
    # Open file
    f = open(file_name, "w")
    
    # Write header
    f.write("#Fields: date time s-ip cs-method cs-uri-stem cs-uri-query s-port cs-username c-ip cs(User-Agent) cs(Referer) sc-status sc-substatus sc-win32-status time-taken\r")
    
    # Write lines
    for j in range(0, random.randint(min_num_lines, max_num_lines)):
        # Create date
        date = date_list[i].strftime("%Y-%m-%d") + " " + str(random.randint(0, 23)).zfill(2) + ":" + str(random.randint(0, 59)).zfill(2) + ":" + str(random.randint(0, 59)).zfill(2)
        
        # Create IP
        ip = ip_list[random.randint(0, len(ip_list) - 1)]
        
        # Create URI stem
        uri_stem = common_uri_stems[random.randint(0, len(common_uri_stems) - 1)]
        
        # Create user agent
        user_agent = user_agents[random.randint(0, len(user_agents) - 1)]
        
        # Create status code
        status_code = status_codes[random.randint(0, len(status_codes) - 1)]
        
        # Create time taken
        time_taken = str(random.randint(0, 1000))
        
        # Get a random request method
        request_method = request_methods[random.randint(0, len(request_methods) - 1)]
        
        # Random port (80 or 443)
        port = random.choices([80, 443], [0.7, 0.3])[0]
        
        # Write line
        f.write(date + " " + ip + " " + request_method + " " + uri_stem + " - " + str(port) + " - " + ip + " " + user_agent + " - " + status_code + " 0 0 " + time_taken + "\r")
        
    # Close file
    f.close()
    
print("Done!")
