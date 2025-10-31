#!/usr/bin/env python3
# simple_nmap_json_to_html.py

import json
import sys
from datetime import datetime

def make_html(data):
    # Get current time for report
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    # Start HTML page
    html_code = "<html><head><meta charset='utf-8'>"
    html_code += "<title>Nmap Scan Report</title>"
    html_code += "<style>"
    html_code += "body{font-family:Arial;padding:10px}"
    html_code += "table{border-collapse:collapse;width:100%}"
    html_code += "td,th{border:1px solid #999;padding:5px}"
    html_code += "</style></head><body>"

    # Add report heading
    html_code += f"<h1>Nmap Scan Report</h1>"
    html_code += f"<p><b>Report generated:</b> {now}</p>"
    html_code += f"<p><b>Scan args:</b> {data.get('scan_args', '')}</p>"

    # Go through all hosts found in the scan
    for host in data.get("hosts", []):
        # Collect IP addresses
        addresses = [a["addr"] for a in host.get("addresses", [])]
        html_code += f"<h2>Host: {', '.join(addresses)}</h2>"
        html_code += f"<p>Status: {host.get('status', '')}</p>"

        # Make a table for open ports
        html_code += "<table>"
        html_code += "<tr><th>Port</th><th>Protocol</th><th>State</th><th>Service</th><th>Version</th></tr>"

        # Go through each port
        for port in host.get("ports", []):
            port_id = port.get("port", "")
            proto = port.get("protocol", "")
            state = port.get("state", "")
            service = ""
            version = ""

            # If service info is available
            svc = port.get("service", {})
            if svc:
                service = svc.get("name", "")
                version = svc.get("version", "")

            html_code += f"<tr><td>{port_id}</td><td>{proto}</td><td>{state}</td><td>{service}</td><td>{version}</td></tr>"

        html_code += "</table>"

    # End the HTML page
    html_code += "</body></html>"
    return html_code


# 🧩 Main part of the script
if __name__ == "__main__":
    # Check if user gave a JSON file name
    if len(sys.argv) < 2:
        print("Usage: python3 simple_nmap_json_to_html.py <file.json>")
        sys.exit(1)

    # Read JSON file
    filename = sys.argv[1]
    with open(filename) as f:
        data = json.load(f)

    # Make output HTML filename
    output_file = filename.replace(".json", ".html")

    # Create HTML content
    html_report = make_html(data)

    # Save it as an HTML file
    with open(output_file, "w") as f:
        f.write(html_report)

    print(f"HTML report created: {output_file}")
