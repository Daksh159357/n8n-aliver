FROM n8nio/n8n:latest

# Set environment
ENV NODE_ENV=production

# Expose n8n default port
EXPOSE 5678

# Start n8n
CMD ["n8n"]
