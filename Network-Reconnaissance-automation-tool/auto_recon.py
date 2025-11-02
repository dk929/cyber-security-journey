#!/usr/bin/env python3

import subprocess, json, sys, os
from datetime import datetime

def run_cmd(cmd):
    """Sefely run shell command and capture output"""
    try:
        result = subprocess.run(cmd, shell=True, text=True, capture_output=True, timeout=60)
        return result.stdout.strip()
    except subprocess.TimeoutExpired:
        return "Command timed out"
    
def recon(domain):
    data = {"domain": domain, "timestamp": str(datetime.utcnow())}

    print(f"[+] Running WHOIS lookup..")
    data["whois"] = run_cmd(f"whois {domain}")

    print(f"[+] Running Nmap scan..")
    data["nmap"] = run_cmd(f"nmap -sS -T4 -pn {domain}")

    print(f"[+] Running subfinder..")
    data["subdomain"] = run_cmd(f"subfinder -d {domain}")

    return data

def save_report(data):
    filename = f"report_{data['domain'].replace('.', '_')}.json"
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print(f"Report save as {filename}")

if __name__ =="__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 auto_recon.py <domain>")
        sys.exit(1)
    domain = sys.argv[1]
    result = recon(domain)
    save_report(result)
