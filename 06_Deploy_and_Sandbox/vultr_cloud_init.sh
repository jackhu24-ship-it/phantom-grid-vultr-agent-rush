#!/bin/bash
# ==============================================================================
# PHANToM GRID :: Vultr Cloud-Init Automation Script
# Provisions Ubuntu 22.04 LTS / 24.04 LTS VM on Vultr Cloud Compute
# Configures Docker, Python 3.11, Isolated Bridge, and FastAPI Gateway Service
# ==============================================================================

set -euo pipefail

echo "==> [STEP 1/5] Updating system packages..."
apt-get update -y
apt-get upgrade -y
apt-get install -y --no-install-recommends \
    ca-certificates \
    curl \
    gnupg \
    lsb-release \
    python3 \
    python3-pip \
    python3-venv \
    git \
    ufw

echo "==> [STEP 2/5] Installing Docker Engine..."
mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update -y
apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
systemctl enable docker
systemctl start docker

echo "==> [STEP 3/5] Creating Air-Gapped Docker Network..."
docker network create --internal --opt com.docker.network.bridge.enable_icc=false airgap_sandbox || true

echo "==> [STEP 4/5] Deploying PHANToM GRID Gateway..."
mkdir -p /opt/phantom_grid
cd /opt/phantom_grid

cat << 'EOF' > /etc/systemd/system/phantom-vultr-agent.service
[Unit]
Description=PHANToM GRID Vultr Agent Gateway
After=network.target docker.service
Requires=docker.service

[Service]
Type=simple
User=root
WorkingDirectory=/opt/phantom_grid
Environment=VULTR_INFERENCE_URL=https://api.vultrinference.com/v1/chat/completions
Environment=VULTR_MODEL=llama-3.3-70b-instruct
ExecStart=/usr/bin/python3 -m uvicorn backend.app:app --host 0.0.0.0 --port 8000
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

echo "==> [STEP 5/5] Configuring Firewall & UFW..."
ufw default deny incoming
ufw default allow outgoing
ufw allow 22/tcp
ufw allow 80/tcp
ufw allow 443/tcp
ufw allow 8000/tcp
echo "y" | ufw enable

echo "==> [OK] Vultr Cloud VM Provisioned and Ready for Autonomous Agent Workloads."
