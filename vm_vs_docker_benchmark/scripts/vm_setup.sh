#!/bin/bash
echo "🖥️ Setting up VM environment..."

sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip sysbench git curl procps

python3 -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

echo "✅ VM environment setup complete!"
echo "➡️ Run Flask server: source venv/bin/activate && python3 app.py"
echo "➡️ Run Jupyter notebook: source venv/bin/activate && jupyter notebook --ip=0.0.0.0 --allow-root"
