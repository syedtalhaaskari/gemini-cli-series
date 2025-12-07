from fastmcp import FastMCP

mcp = FastMCP(name="MyFirstMCPServer")


@mcp.tool
def greet(name: str) -> str:
    """Returns a friendly greeting"""
    return f"Hello {name}! Its a pleasure to connect from your first MCP Server."


if __name__ == "main":
    mcp.run(transport="http", port="8080")
