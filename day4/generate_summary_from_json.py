#!/usr/bin/env python3
# generate_summary_from_json.py
import json, sys
from collections import defaultdict

def score_port(port, service):
    # simple rules
    high_ports = {21,23,25,69,445,3389}
    if port in high_ports:
        return "High"
    if service and service.get('name') in ['ftp','telnet','smtp','ms-sql','microsoft-ds','rpcbind']:
        return "High"
    # services often medium
    if service and service.get('name') in ['http','https','mysql','postgresql','ssh']:
        return "Medium"
    return "Low"

def summarize(jpath, outpath):
    with open(jpath) as f:
        data = json.load(f)
    hosts = data.get('hosts', [])
    lines = []
    if data.get('scan_args'):
        lines.append(f"**Scan args:** {data.get('scan_args')}\n")
    for idx, host in enumerate(hosts,1):
        addrs = ", ".join([a['addr'] for a in host.get('addresses',[])])
        lines.append(f"## Host {idx}: {addrs}\n")
        top = []
        for p in host.get('ports',[]):
            svc = p.get('service',{})
            portnum = p.get('port')
            state = p.get('state')
            servname = svc.get('name','') if svc else ''
            severity = score_port(portnum, svc)
            note = ""
            if p.get('scripts'):
                note = " | ".join([f"{s['id']}: {s.get('output','')[:200]}" for s in p.get('scripts')])
            top.append((severity, portnum, servname, state, note))
        # sort High -> Medium -> Low and by port
        top_sorted = sorted(top, key=lambda x: (['High','Medium','Low'].index(x[0]), x[1]))
        lines.append("|Severity|Port|Service|State|Notes|\n|---|---:|---|---|---|\n")
        for sev, portnum, servname, state, note in top_sorted:
            lines.append(f"|{sev}|{portnum}|{servname}|{state}|{note}|\n")
        lines.append("\n")
    with open(outpath, "w") as o:
        o.write("# Automated Scan Summary\n\n")
        o.write("\n".join(lines))
    print(f"Wrote summary to {outpath}")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: generate_summary_from_json.py <scan.json> <out_summary.md>")
        sys.exit(1)
    summarize(sys.argv[1], sys.argv[2])
