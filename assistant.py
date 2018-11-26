from __future__ import print_function
import json
from watson_developer_cloud import AssistantV2

#########################
# Credentials
#########################
assistant = AssistantV2(
     version='2018-09-20',
     url='https://gateway-fra.watsonplatform.net/assistant/api',
     iam_apikey='AAAA')
assistant_id='BBBB'

#########################
# Sessions
#########################
session = assistant.create_session(assistant_id).get_result()
session_id=session["session_id"]
#print("Dump session..." + json.dumps(session, indent=2))

#########################
# Message
#########################

message = assistant.message(
    assistant_id,
    session_id,
    input={'text': 'What is Kodi?'},
    ).get_result()
print(json.dumps(message, indent=2))

assistant.delete_session(assistant_id, session_id).get_result()

