import re
from fastmcp import FastMCP
from mcp.types import PromptMessage, TextContent

mcp = FastMCP(name="MyFirstMCPServer")


@mcp.tool
def greet(name: str) -> str:
    """Returns a friendly greeting"""
    return f"Hello {name}! Its a pleasure to connect from your first MCP Server."


@mcp.tool
def calculate_readability(text: str) -> float:
    """Calculates the Flesch-Kincaid grade level for the given text."""
    # This is a simplified implementation for demonstration purposes.
    words = len(text.split())
    sentences = len(re.split(r"[.!?]+", text))
    syllables = sum(1 for word in text.split() for c in word.lower() if c in "aeiou")

    # Avoid division by zero
    if words == 0 or sentences == 0:
        return 0.0

    # Flesch-Kincaid Grade Level formula
    score = (0.39 * (words / sentences)) + (11.8 * (syllables / words)) - 15.59
    return round(score, 2)


@mcp.tool
def check_for_weasel_words(text: str) -> list[str]:
    """Identifies and returns a list of ambiguous 'weasel words' from the text."""
    weasel_words = [
        "many",
        "various",
        "several",
        "some",
        "most",
        "often",
        "sometimes",
        "virtually",
    ]
    # Use regex to find all occurrences of any weasel word, ignoring case and matching whole words
    pattern = r"\b(" + "|".join(weasel_words) + r")\b"
    found_words = re.findall(pattern, text, re.IGNORECASE)
    return list(set(found_words))  # Return unique words found


@mcp.prompt
def tech_edit(text_to_review: str) -> PromptMessage:
    """Acts as a senior technical editor to review the provided text."""
    prompt_text = f"""
    You are an expert technical editor. Your goal is to provide a comprehensive and helpful review of 
    the following text.
    
    Please perform the following steps in order:
    1. First, call the `calculate_readability` tool on the text to determine its Flesch-Kincaid grade level.
    2. Next, call the `check_for_weasel_words` tool to find any ambiguous "weasel words".
    3. After using the tools, perform your own analysis of the text for overall clarity, tone, and style.
    Specifically look for passive voice and overly complex sentences.
    4. Finally, synthesize all of your findings (from the tool outputs and your own analysis) into a 
    single, well-structured markdown report with three sections:
        - ### Readability Score
          State the score returned by the tool and briefly explain what it means (e.g., "suitable for a
          general audience").
        - ### Weasel Words
          List any words found by the tool. For each word, explain why it's ambiguous and suggest a more
          specific alternative.
        - ### General Feedback
          Provide your analysis on tone, clarity, and style. Include specific examples from the text and
          offer concrete suggestions for improvement.
    
    Your final output should be ONLY the markdown report.
    
    Here is the text to review:
    ---
    {text_to_review}
    ---
    """
    return PromptMessage(
        role="user", content=TextContent(type="text", text=prompt_text)
    )


if __name__ == "main":
    mcp.run(transport="http", port="8080")
