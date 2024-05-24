# Create a malicious script that will be executed by the subprocess module.
# The script will print the flag to the console.

import subprocess

domain = input("Enter a domain: ")
output = subprocess.check_output(f"nslookup {domain}", shell=True, encoding="UTF-8")
print(output)
