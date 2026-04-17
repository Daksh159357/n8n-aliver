import os
import subprocess

# Get Render port
port = os.environ.get("PORT", "5678")

# Set correct environment variables
os.environ["N8N_PORT"] = port
os.environ["N8N_HOST"] = "0.0.0.0"
os.environ["NODE_ENV"] = "production"

# Start n8n
subprocess.run(f"npx n8n start --port {port}", shell=True)
