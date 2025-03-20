import logging, asyncio
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.teams.magentic_one import MagenticOne
from autogen_agentchat import EVENT_LOGGER_NAME, TRACE_LOGGER_NAME
from autogen_agentchat.ui import Console

# Setup the logging configuration.
logging.basicConfig(filename='./logs/sample-2.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# For trace logging.
trace_logger = logging.getLogger(TRACE_LOGGER_NAME)
trace_logger.addHandler(logging.StreamHandler())
trace_logger.setLevel(logging.DEBUG)

# For structured message logging, such as low-level messages between agents.
event_logger = logging.getLogger(EVENT_LOGGER_NAME)
event_logger.addHandler(logging.StreamHandler())
event_logger.setLevel(logging.DEBUG)

# Create and run the M1 agent team.
async def run_m1():
    client = OpenAIChatCompletionClient(model="gpt-4o")
    m1 = MagenticOne(client=client)
    task = "Given information in  folder 'files' map 'CustomPOSchema.txt' to 'ORDER_D96A.xsd' using the mapping rules in 'mapping_rules.txt' and common known expressions to transform values." 
    result = await Console(m1.run_stream(task=task))
    print(result)

# Main entry point.
if __name__ == "__main__":
    asyncio.run(run_m1())