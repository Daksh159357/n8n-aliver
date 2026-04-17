import os
import subprocess

port = os.environ.get("PORT", "10000")

env = os.environ.copy()
env["N8N_PORT"] = port
env["N8N_HOST"] = "0.0.0.0"
env["NODE_ENV"] = "production"

subprocess.run(
    ["bash", "-c", f"npx --yes n8n start --port {port}"],
    env=env
)
