from mcp.server.fastmcp import FastMCP 

mcp = FastMCP("Test")

@mcp.prompt
def agent(username:str, user_title:str) -> str:
    """Global level instruction for the agent"""
    return f""" you are a helpful agent for {username} ({user_title}). You help them with tasks that you can perform. 

    ** preferences**
    - Keep communications concise short and friendly.
    """ 