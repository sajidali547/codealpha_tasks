@'
#!/usr/bin/env python3
"""CodeAlpha Task 4: NIDS Alert Monitor and Dashboard"""

import os
import re
import time
import threading
from datetime import datetime
from flask import Flask, render_template_string, jsonify

app = Flask(__name__)
ALERT_FILE = "/var/log/snort/alert"
alerts = []
MAX_ALERTS = 100

DASHBOARD_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>CodeAlpha NIDS Dashboard</title>
    <meta http-equiv="refresh" content="5">
    <style>
        body { font-family: Arial; background: #1e1e2e; color: #cdd6f4; margin: 20px; }
        h1 { color: #89b4fa; }
        table { width: 100%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #45475a; padding: 10px; text-align: left; }
        th { background: #313244; color: #f5c2e7; }
        tr:nth-child(even) { background: #181825; }
        .severity-high { color: #f38ba8; font-weight: bold; }
    </style>
</head>
<body>
    <h1>CodeAlpha NIDS Dashboard</h1>
    <p>Monitoring Snort alerts. Total: {{ alerts|length }}</p>
    <table>
        <tr><th>Time</th><th>Source IP</th><th>Dest IP</th><th>Protocol</th><th>Alert</th></tr>
        {% for a in alerts %}
        <tr>
            <td>{{ a.time }}</td><td>{{ a.src }}</td><td>{{ a.dst }}</td>
            <td>{{ a.proto }}</td><td class="severity-high">{{ a.msg }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

def parse_alert_line(line):
    alert = {}
    try:
        m = re.search(r'\[\*\*\] \[\d+:\d+:\d+\] (.+?) \[\*\*\]', line)
        if m: alert['msg'] = m.group(1)
        ip = re.search(r'(\d+\.\d+\.\d+\.\d+)\s*->\s*(\d+\.\d+\.\d+\.\d+)', line)
        if ip:
            alert['src'] = ip.group(1)
            alert['dst'] = ip.group(2)
        p = re.search(r'(ICMP|TCP|UDP)', line)
        if p: alert['proto'] = p.group(1)
        alert['time'] = datetime.now().strftime('%H:%M:%S')
        return alert if 'msg' in alert else None
    except Exception:
        return None

def tail_alert_file():
    global alerts
    if not os.path.exists(ALERT_FILE):
        print("[!] Alert file not found: " + ALERT_FILE)
        return
    with open(ALERT_FILE, 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                alert = parse_alert_line(line)
                if alert:
                    alerts.append(alert)
                    if len(alerts) > MAX_ALERTS:
                        alerts.pop(0)
                    print("[ALERT]", alert)
            else:
                time.sleep(0.5)

@app.route('/')
def dashboard():
    return render_template_string(DASHBOARD_HTML, alerts=alerts[::-1])

@app.route('/api/alerts')
def api_alerts():
    return jsonify(alerts)

if __name__ == '__main__':
    print("="*60)
    print("  CodeAlpha NIDS Monitor")
    print("Watching: " + ALERT_FILE)
    print("Dashboard: http://localhost:5000")
    print("="*60)
    t = threading.Thread(target=tail_alert_file, daemon=True)
    t.start()
    app.run(host='0.0.0.0', port=5000, debug=False)
'@ | Out-File -FilePath ids_monitor.py -Encoding utf8