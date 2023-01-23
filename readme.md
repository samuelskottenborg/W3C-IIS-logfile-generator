# IIS log generator
## Introduction
This script generates IIS log files which is useful for testing log analysis tools. The status codes, HTTP/HTTPS ratio and request methods all follow customizable random distributions.

To make the logs more realistic, lot's of small tweaks has been made. For example, each IP is assigned a unique probability of making a request instead of having equal traffic from every IP.

It follows the [W3C Extended Log File Format](https://www.w3.org/TR/WD-logfile.html) and generates a log file with the following fields:

- date
- time
- s-ip
- cs-method
- cs-uri-stem
- cs-uri-query
- s-port
- cs-username
- c-ip
- cs(User-Agent)
- cs(Referer)
- sc-status
- sc-substatus
- sc-win32-status
- time-taken



## Usage
Change the variables in the top of the script to suit your needs and run it.


## TODO
- More realistic distributation of traffic 
