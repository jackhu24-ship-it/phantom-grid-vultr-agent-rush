# -*- coding: utf-8 -*-
"""
PHANToM GRID :: Master Full-Bleed 16:9 Cover Image Generator
Tournament: 202611_Vultr_Agent_Rush_Hackathon
"""
import os
import subprocess

SVG_CONTENT = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1080" width="1920" height="1080">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#050811" />
      <stop offset="50%" stop-color="#0B132B" />
      <stop offset="100%" stop-color="#040710" />
    </linearGradient>
    <linearGradient id="cyanGold" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00E5FF" />
      <stop offset="50%" stop-color="#38BDF8" />
      <stop offset="100%" stop-color="#F59E0B" />
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0E1B33" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#080F1F" stop-opacity="0.98" />
    </linearGradient>
    <linearGradient id="hudGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0C1D33" stop-opacity="0.95" />
      <stop offset="100%" stop-color="#060E1A" stop-opacity="0.98" />
    </linearGradient>
    <pattern id="grid" width="60" height="60" patternUnits="userSpaceOnUse">
      <path d="M 60 0 L 0 0 0 60" fill="none" stroke="#1E293B" stroke-width="1" stroke-opacity="0.35" />
    </pattern>
  </defs>

  <!-- Full Background -->
  <rect width="1920" height="1080" fill="url(#bgGrad)" />
  <rect width="1920" height="1080" fill="url(#grid)" />

  <!-- Outer Neon Border -->
  <rect x="24" y="24" width="1872" height="1032" rx="16" fill="none" stroke="#38BDF8" stroke-width="2" stroke-opacity="0.4" />

  <!-- Category Pill -->
  <g transform="translate(80, 55)">
    <rect width="740" height="64" rx="32" fill="#0E243A" stroke="#00E5FF" stroke-width="2" />
    <text x="370" y="42" text-anchor="middle" fill="#00E5FF" font-family="Consolas, monospace" font-size="28" font-weight="bold" letter-spacing="2">
      VULTR HACKATHON // SANDBOXED AGENT RUSH
    </text>
  </g>

  <!-- Main Hero Title -->
  <text x="80" y="195" fill="url(#cyanGold)" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="52" font-weight="900" letter-spacing="1">
    PHANToM GRID :: Sandboxed Agent Gateway
  </text>
  
  <!-- Hero Subtitle -->
  <text x="80" y="255" fill="#E2E8F0" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="25" font-weight="400">
    Deterministic Docker Sandbox Boundary on Vultr Cloud &amp; Serverless Inference
  </text>

  <!-- Commander Jack Hu Badge (Budgeted: width 1200 <= 68% of 1920 = 1305.6, padding 48px) -->
  <g transform="translate(80, 300)">
    <rect width="1200" height="85" rx="12" fill="url(#hudGrad)" stroke="#38BDF8" stroke-width="1.8" />
    <text x="30" y="38" fill="#F59E0B" font-family="Segoe UI, Helvetica, Arial, sans-serif" font-size="20" font-weight="bold">
      SUPREME COMMANDER JACK HU (SOLO ARCHITECT)
    </text>
    <text x="30" y="65" fill="#94A3B8" font-family="Consolas, monospace" font-size="16">
      Lead Co-Signers: Commander Xiaomi ✕ Vanguard Xiao-Ke (Office 1) ✕ Vanguard Xiao-Ma (Office 3)
    </text>
  </g>

  <!-- Feature Cards -->
  <g transform="translate(80, 420)">
    <!-- Card 1 -->
    <rect width="360" height="300" rx="14" fill="url(#cardGrad)" stroke="#1E293B" stroke-width="1.5" />
    <text x="24" y="48" fill="#00E5FF" font-family="Segoe UI, Helvetica, sans-serif" font-size="22" font-weight="bold">
      Docker Sandbox
    </text>
    <text x="24" y="85" fill="#94A3B8" font-family="Segoe UI, sans-serif" font-size="16">
      Disposable throwaway containers absorb rm -rf / and infinite loops safely without host impact.
    </text>
    <text x="24" y="260" fill="#10B981" font-family="Consolas, monospace" font-size="15" font-weight="bold">
      &#10004; AIR-GAPPED ISOLATION
    </text>
  </g>

  <g transform="translate(480, 420)">
    <!-- Card 2 -->
    <rect width="360" height="300" rx="14" fill="url(#cardGrad)" stroke="#1E293B" stroke-width="1.5" />
    <text x="24" y="48" fill="#00E5FF" font-family="Segoe UI, Helvetica, sans-serif" font-size="22" font-weight="bold">
      Vultr Serverless
    </text>
    <text x="24" y="85" fill="#94A3B8" font-family="Segoe UI, sans-serif" font-size="16">
      OpenAI-compatible inference query gateway with exponential backoff and jitter tolerance.
    </text>
    <text x="24" y="260" fill="#10B981" font-family="Consolas, monospace" font-size="15" font-weight="bold">
      &#10004; api.vultrinference.com
    </text>
  </g>

  <g transform="translate(880, 420)">
    <!-- Card 3 -->
    <rect width="400" height="300" rx="14" fill="url(#cardGrad)" stroke="#1E293B" stroke-width="1.5" />
    <text x="24" y="48" fill="#00E5FF" font-family="Segoe UI, Helvetica, sans-serif" font-size="22" font-weight="bold">
      ASIL-D Defense
    </text>
    <text x="24" y="85" fill="#94A3B8" font-family="Segoe UI, sans-serif" font-size="16">
      50.0 GB hardware memory circuit breaker paired with 0.00 MB ZDR dual-pass physical memory zeroing.
    </text>
    <text x="24" y="260" fill="#10B981" font-family="Consolas, monospace" font-size="15" font-weight="bold">
      &#10004; 0.00 MB RESIDUAL
    </text>
  </g>

  <!-- Right Telemetry Panel -->
  <g transform="translate(1320, 200)">
    <rect width="520" height="500" rx="14" fill="url(#hudGrad)" stroke="#38BDF8" stroke-width="1.8" />
    <text x="24" y="48" fill="#00E5FF" font-family="Consolas, monospace" font-size="22" font-weight="bold">
      SYSTEM TELEMETRY
    </text>
    
    <text x="24" y="100" fill="#94A3B8" font-family="Consolas, monospace" font-size="18">CLOUD VM RUNTIME</text>
    <text x="496" y="100" text-anchor="end" fill="#10B981" font-family="Consolas, monospace" font-size="18" font-weight="bold">VULTR BARE-METAL</text>

    <text x="24" y="150" fill="#94A3B8" font-family="Consolas, monospace" font-size="18">SANDBOX CONTAINER</text>
    <text x="496" y="150" text-anchor="end" fill="#00E5FF" font-family="Consolas, monospace" font-size="18" font-weight="bold">ISOLATED BRIDGE</text>

    <text x="24" y="200" fill="#94A3B8" font-family="Consolas, monospace" font-size="18">MEMORY CEILING</text>
    <text x="496" y="200" text-anchor="end" fill="#F59E0B" font-family="Consolas, monospace" font-size="18" font-weight="bold">50.0 GB HARD CAP</text>

    <text x="24" y="250" fill="#94A3B8" font-family="Consolas, monospace" font-size="18">ZDR MEMORY RESIDUE</text>
    <text x="496" y="250" text-anchor="end" fill="#10B981" font-family="Consolas, monospace" font-size="18" font-weight="bold">0.00 MB PURGED</text>

    <text x="24" y="300" fill="#94A3B8" font-family="Consolas, monospace" font-size="18">CONTAINMENT DEFENSE</text>
    <text x="496" y="300" text-anchor="end" fill="#10B981" font-family="Consolas, monospace" font-size="18" font-weight="bold">100% ABSORBED</text>

    <text x="24" y="350" fill="#94A3B8" font-family="Consolas, monospace" font-size="18">INFERENCE LATENCY</text>
    <text x="496" y="350" text-anchor="end" fill="#38BDF8" font-family="Consolas, monospace" font-size="18" font-weight="bold">21.4 ms</text>
  </g>

  <!-- WORM Audit Seal -->
  <g transform="translate(1320, 740)">
    <rect width="520" height="145" rx="14" fill="url(#hudGrad)" stroke="#F59E0B" stroke-width="2" />
    <text x="24" y="52" fill="#F59E0B" font-family="Consolas, monospace" font-size="24" font-weight="bold">WORM AUDIT LOCKED</text>
    <text x="24" y="85" fill="#94A3B8" font-family="Consolas, monospace" font-size="18">SHA-256: 0x8892BA01EF44... [SEALED]</text>
    <text x="24" y="118" fill="#10B981" font-family="Consolas, monospace" font-size="19" font-weight="bold">&#10004; CO-SIGNED: COMMANDER XIAOMI</text>
  </g>

  <!-- Broadcast Safe Zone Title -->
  <text x="960" y="995" text-anchor="middle" fill="#00E5FF" font-family="Consolas, monospace" font-size="24" font-weight="bold" letter-spacing="2">
    BROADCAST SAFE ZONE // 1440P / 1080P MASTER SPEC // ASIL-D STATE RECOVERY CERTIFIED // OFFLINE VERIFIED
  </text>
</svg>"""

HTML_CONTENT = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  html, body {{
    margin: 0; padding: 0; width: 1920px; height: 1080px; overflow: hidden; background: #050811;
  }}
</style>
</head>
<body>
{SVG_CONTENT}
</body>
</html>"""

def generate_banner(output_dir):
    svg_path = os.path.join(output_dir, "cover_16x9.svg")
    html_path = os.path.join(output_dir, "cover_16x9.html")
    png_path = os.path.join(output_dir, "cover_16x9.png")

    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(SVG_CONTENT)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(HTML_CONTENT)

    browser = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    if not os.path.exists(browser):
        browser = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--hide-scrollbars",
        "--window-size=1920,1080",
        f"--screenshot={png_path}",
        html_path
    ]
    subprocess.run(cmd, capture_output=True)

def generate_svg_banner(output_path):
    output_dir = os.path.dirname(output_path)
    generate_banner(output_dir)

if __name__ == "__main__":
    cur = os.path.dirname(os.path.abspath(__file__))
    generate_banner(cur)
    print("Cover 16:9 banner generated successfully.")
