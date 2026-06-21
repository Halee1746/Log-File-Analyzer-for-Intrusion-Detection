# Log File Analyzer for Intrusion Detection

## Introduction

The Log File Analyzer for Intrusion Detection is a simple Python-based cybersecurity project that analyzes login log records to identify suspicious activity. In many systems, login logs are useful for monitoring user activity and detecting unusual behavior such as repeated failed login attempts. This project focuses on checking log entries, identifying failed logins, and finding suspicious IP addresses that may indicate a brute-force attack.

## Objective

The main objective of this project is to understand how log analysis can be used in cybersecurity for intrusion detection. The program is designed to scan login records, count failed login attempts, and generate alerts when the same IP address shows repeated failures.

## Features

* Reads login records from a log file
* Detects failed login attempts
* Counts failed attempts from each IP address
* Identifies suspicious IP activity
* Detects possible brute-force attack behavior
* Displays a simple analysis report

## Working of the Project

The program reads the log data line by line and checks whether a login attempt has failed. If a failed login is found, the program increases the total failed login count and extracts the IP address from that log entry. It then stores the number of failed attempts for each IP address. At the end of the analysis, the program shows the suspicious IP addresses and prints an alert if an IP has crossed the brute-force threshold.

## Technologies Used

* Python
* Text file handling
* GitHub
* Programiz Python Compiler / Python IDE

## Learning Outcome

Through this project, I learned how login log analysis can be used to detect suspicious activity in cybersecurity. I also improved my understanding of Python concepts such as loops, conditions, dictionaries, and string operations. This project gave me practical knowledge of how repeated failed login attempts can be tracked and used to identify possible intrusion attempts.

## Conclusion

This project demonstrates a simple way to analyze login logs for intrusion detection. By monitoring failed login attempts and suspicious IP addresses, the program helps in identifying possible brute-force attacks and understanding the role of log analysis in cybersecurity.
