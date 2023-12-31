# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
{
  "next_action": "string",
  "sender_id": "string",
  "tracker": {
    "conversation_id": "default",
    "slots": {},
    "latest_message": {},
    "latest_event_time": 1537645578.314389,
    "followup_action": "string",
    "paused": false,
    "events": [],
    "latest_input_channel": "rest",
    "active_loop": {},
    "latest_action": {}
  },
  "domain": {
    "config": {},
    "session_config": {},
    "intents": [],
    "entities": [],
    "slots": {},
    "responses": {},
    "actions": [],
    "forms": {},
    "e2e_actions": []
  },
  "version": "version"
}