Install fastmcp
uv pip install fastmcp

Run Server
fastmcp run server.py --transport="http" --port="8080"

To launch MCP Inspector
fastmcp dev server.py --ui-port="9080" --server-port="6277"