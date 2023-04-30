import random
from langchain.llms import OpenAI
from langchain.agents import load_tools, initialize_agent, AgentType


def handle_response(message):
    p_message = message.lower()
    
    if p_message == 'hello':
        return 'Hello Jeff and Alex! I am MunchLax Bot! Here to Lick, Tackle, and sleep!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`This is a help message!`"
    
    if message.startswith("!gpt:"):
        return handle_llm_message(message.replace("!gpt:", ""))


def handle_llm_message(message):
    llm = OpenAI(temperature=0.9)
    # Next, let's load some tools to use. Note that the `llm-math` tool uses an LLM, so we need to pass that in.
    tools = load_tools(["serpapi", "llm-math"], llm=llm)
    # Finally, let's initialize an agent with the tools, the language model, and the type of agent we want to use.
    agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)
    print(f"LLM Handler Received message: {message}")
    return agent.run(message)