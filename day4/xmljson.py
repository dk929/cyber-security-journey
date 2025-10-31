#!/usr/bin/env python3
# nmap_xml_to_json.py
import xml.etree.ElementTree as ET
import json
import sys

def parse_nmap_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    report = {"scan_start": root.attrib.get("startstr", ""),
              "scan_args": root.attrib.get("args",""),
              "hosts": []}
    for host in root.findall('host'):
        h = {"addresses": [], "status": "", "ports": []}
        status = host.find('status')
        if status is not None:
            h["status"] = status.attrib.get("state","")
        for addr in host.findall('address'):
            h["addresses"].append({"addr": addr.attrib.get("addr"),
                                   "addrtype": addr.attrib.get("addrtype")})
        ports = host.find('ports')
        if ports is not None:
            for port in ports.findall('port'):
                p = {}
                p['port'] = int(port.attrib.get('portid', 0))
                p['protocol'] = port.attrib.get('protocol')
                state = port.find('state')
                svc = port.find('service')
                p['state'] = state.attrib.get('state') if state is not None else ''
                if svc is not None:
                    p['service'] = {
                        'name': svc.attrib.get('name',''),
                        'product': svc.attrib.get('product',''),
                        'version': svc.attrib.get('version',''),
                        'extrainfo': svc.attrib.get('extrainfo','')
                    }
                scripts = []
                for scr in port.findall('script'):
                    scripts.append({'id': scr.attrib.get('id'), 'output': scr.attrib.get('output')})
                if scripts:
                    p['scripts'] = scripts
                h['ports'].append(p)
        report['hosts'].append(h)
    return report

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 nmap_xml_to_json.py <file.xml>")
        sys.exit(1)
    xmlf = sys.argv[1]
    out = xmlf.replace('.xml', '.json')
    data = parse_nmap_xml(xmlf)
    with open(out, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Saved {out}")
