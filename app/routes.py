from flask import Blueprint, render_template, jsonify, request
import datetime
import platform

main = Blueprint('main', __name__)


def wants_json():
    accept = request.headers.get('Accept', '')
    return 'text/html' not in accept


def api_page(title, subtitle, data, color="#38bdf8"):
    rows = ''.join(
        f'<div class="kv"><span class="kv-k">{k}</span>'
        f'<span class="kv-v">{v}</span></div>'
        for k, v in data.items()
    )
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width,initial-scale=1.0"/>
  <title>{title}</title>
  <link href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&family=IBM+Plex+Sans:wght@400;500;600&display=swap" rel="stylesheet"/>
  <style>
    *,*::before,*::after{{margin:0;padding:0;box-sizing:border-box}}
    :root{{
      --bg:#080c14;--panel:#0d1525;--panel2:#111d30;
      --border:#1e2d47;--text:#e2e8f0;--muted2:#6b87a8;
      --accent:{color};--mono:'IBM Plex Mono',monospace;--sans:'IBM Plex Sans',sans-serif;
    }}
    body{{font-family:var(--sans);background:var(--bg);color:var(--text);
          min-height:100vh;display:flex;align-items:center;justify-content:center;padding:24px}}
    .card{{background:var(--panel);border:1px solid var(--border);border-radius:12px;
            width:100%;max-width:500px;overflow:hidden}}
    .card-top{{padding:22px 26px;border-bottom:1px solid var(--border);
               background:var(--panel2);position:relative}}
    .card-top::before{{content:'';position:absolute;top:0;left:0;right:0;
                        height:3px;background:var(--accent)}}
    .back{{display:inline-flex;align-items:center;gap:6px;font-family:var(--mono);
            font-size:0.68rem;color:var(--muted2);text-decoration:none;margin-bottom:14px;
            padding:4px 10px;border:1px solid var(--border);border-radius:4px;transition:all .14s}}
    .back:hover{{color:var(--text);border-color:var(--muted2)}}
    .badge{{font-family:var(--mono);font-size:0.6rem;font-weight:600;
             background:#38bdf818;color:#38bdf8;border:1px solid #38bdf840;
             padding:2px 8px;border-radius:3px;display:inline-block;margin-bottom:10px}}
    .title{{font-size:1.25rem;font-weight:600;margin-bottom:3px}}
    .subtitle{{font-size:0.75rem;color:var(--muted2)}}
    .kv{{display:flex;align-items:center;justify-content:space-between;
          padding:13px 26px;border-bottom:1px solid var(--border)}}
    .kv:last-child{{border-bottom:none}}
    .kv-k{{font-size:0.8rem;color:var(--muted2)}}
    .kv-v{{font-family:var(--mono);font-size:0.8rem;color:var(--accent)}}
    .footer{{padding:12px 26px;border-top:1px solid var(--border);background:var(--panel2);
              display:flex;justify-content:space-between;align-items:center}}
    .footer-note{{font-family:var(--mono);font-size:0.62rem;color:var(--muted2)}}
    .ok{{font-family:var(--mono);font-size:0.62rem;color:#22c55e;background:#14532d22;
          border:1px solid #22c55e33;padding:3px 10px;border-radius:3px}}
  </style>
</head>
<body>
  <div class="card">
    <div class="card-top">
      <a class="back" href="/">← dashboard</a>
      <div class="badge">GET {request.path}</div>
      <div class="title">{title}</div>
      <div class="subtitle">{subtitle}</div>
    </div>
    <div>{rows}</div>
    <div class="footer">
      <span class="footer-note">cicd-demo-app · CodTech</span>
      <span class="ok">200 OK</span>
    </div>
  </div>
</body>
</html>'''


@main.route('/')
def home():
    return render_template('index.html')


@main.route('/health')
def health():
    data = {
        'status': 'healthy',
        'timestamp': datetime.datetime.now().isoformat(),
        'service': 'cicd-demo-app'
    }
    if wants_json():
        return jsonify(data)
    return api_page('Health Check', 'Service is running normally', data, '#22c55e')


@main.route('/api/info')
def info():
    data = {
        'app': 'CI/CD Demo Application',
        'version': '1.0.0',
        'python_version': platform.python_version(),
        'environment': 'production'
    }
    if wants_json():
        return jsonify(data)
    return api_page('App Info', 'Application metadata', data, '#a855f7')


@main.route('/api/pipeline-status')
def pipeline_status():
    data = {
        'stages': 'lint → test → build → push → deploy → notify',
        'status': 'all passing',
        'last_updated': datetime.datetime.now().isoformat()
    }
    if wants_json():
        return jsonify(data)
    return api_page('Pipeline Status', 'GitHub Actions CI/CD pipeline', data, '#a3e635')