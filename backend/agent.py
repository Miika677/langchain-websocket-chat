from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

#Turn this into a class once multiple users may chat at the same time and per-user state is needed

@tool
def post_to_db(query: str) -> str:
    """Only use this tool if user explicitly wants to post a word.
    After successfully posting a word, the chat is done. Errors occurring during the post should lead to profuse apologizing.
    You can jazz up your answer instead of going with a generic "Post Successful".
    """
    print("Posted")
    return "Post successful!"

agent = create_agent(
    model=ChatGoogleGenerativeAI(model="gemini-2.5-flash"),
    tools=[post_to_db],
    system_prompt="You are a helpful assistant. Use tools as you see fit. If no tool is chosen, wish the assistee a good day."
)

def call_agent(input : dict):
    response = agent.invoke(input)

    content = response["messages"][-1].content

    #Agent can sometimes return a list of dicts; extract text value from first list item
    if isinstance(content, list):
        return content[0]["text"]

    return content