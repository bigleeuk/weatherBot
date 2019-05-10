from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput


nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue', interpreter = nlu_interpreter)

input_channel = SlackInput('xoxp-409670869057-411542884774-414532403479-4c0755f307e3f568a5b866a9a00291cc', #app verification token
                           'xoxb-409670869057-412942316001-xCKKRJ0WwYRI4tVxdojjxAJn', # bot verification token
                           'iWK98mXp97ZV4klLF4m2Ta2b', # slack verification token
                           True)

agent.handle_channel(HttpInputChannel(5004, '/', input_channel))
