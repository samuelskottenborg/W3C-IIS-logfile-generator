# IIS log generator
## Introduction
This script generates IIS log files which is useful for testing log analysis tools.

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

To keep the logs realistic, the same pages and IP addresses are used multiple times, other fields are randomly generated.

## Usage
Change the variables in the top of the script to suit your needs and run it.
