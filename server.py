from mcp.server.fastmcp import FastMCP 

mcp = FastMCP("Test")

@mcp.prompt()
def agent(username:str, user_title:str) -> str:
    """Global level instruction for the agent"""
    return f""" you are a helpful agent for {username} ({user_title}). You help them with tasks that you can perform. 

    ** preferences**
    - Keep communications concise short and friendly.
    """ 


@mcp.resource("email-examples://3-way-intro")
def write_3way_intro() -> str:
    """Write a 3-way introduction email"""
    with open("email-examples/3-way-intro.md", "r") as f:
        return f.read()


@mcp.tool()
def write_email(
    subject: str, body: str, to: str, cc: str = "", bcc: str = "") -> str:
    """Write an email with the given subject and body
    
    Args:
        subject (str): The subject of the email
        body (str): The body of the email
        to (str): The recipient of the email
        cc (str, optional): CC recipients of the email. Defaults to "".
        bcc (str, optional): BCC recipients of the email. Defaults to "".
    Returns:
        str: A formatted email string ready to be sent

    
    """
    return f"""Subject: {subject}
To: {to}
CC: {cc}
BCC: {bcc}
{body}
"""

@mcp.tool()
def send_email()-> str:
    """Send an email using the configured email service
    Note : This is a placeholder function and does not actually send an email. For learning purposes only.
    """
    return "Email sent successfully!"



if __name__ == "__main__":
    mcp.run(transport='stdio')