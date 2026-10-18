#17/9/26 code starts
#building an ai agent
from langchain_ollama import ChatOllama
from fifteenthsept import read_file,count_log_levels,show_docker_containers
from langchain_core.tools import tool
from langchain.agents import create_agent
#LLM
llm = ChatOllama (
    model ="llama3.2",
    url ="http://localhost:11434",
    temperature=0
    )
#Tools
@tool
def analyze_log_files(path):# always remember that an ai agent must have a docstring in its tool describing what the tool does
    """
    this tool counts the LOg levels, INFO and DEBUG from a given file path 
    
    """
    return count_log_levels(read_file(path))

@tool
def get_docker_containers():
    """
    Gets information about all Docker containers.
    """
    return show_docker_containers()
    

#LLM + Tools = AGent
TOOLS = [analyze_log_files,get_docker_containers]
SYSTEM_PROMPT= """

You are a DevOps assistant that can analyze application logs and inspect Docker containers using the available tools.

When a user provides a log file path, use the analyze_log_files tool to inspect the logs.

When a user asks about Docker containers, container status, running containers, stopped containers, or Docker-related issues, use the get_docker_containers tool.

For log analysis, provide:
* Log file overview
* INFO and DEBUG counts returned by the tool
* Critical errors or warnings found in the logs
* Notable patterns or trends
* Relevant metrics when they are actually available
* Practical recommendations for improvement

For Docker analysis, provide:
* Total number of containers
* Running containers
* Exited/stopped containers
* Container names, IDs, and status when available
* Any obvious issues or unusual container states
* Practical recommendations when appropriate

When a question involves both logs and Docker, use both tools and correlate the results where possible.

IMPORTANT:
* Do not invent, estimate, or assume metrics or errors that were not provided by the tools.
* Clearly distinguish between information obtained from the tools and general recommendations.
* Keep the final response clear, concise, and structured.
* If a tool does not provide enough information to answer something, explicitly state that the information is unavailable.


 
"""


agent = create_agent(llm,tools= TOOLS,system_prompt =SYSTEM_PROMPT)

question =input("Enter your question for devops agent")

print("\nTHINKING...\n")
result = agent.invoke({
    "messages": [
        {"role": "user", "content": question}
    ]
})

    #the last message is the agent's final answer
print(result["messages"][-1].content)


