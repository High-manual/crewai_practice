from crewai.tools import tool

@tool("CountLengthTool")
def count_length(text: str) -> str:
    """주어진 텍스트의 글자 수를 반환합니다."""
    length = len(text)
    return f"글자 수는 {length}자 입니다."