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

from typing import Any, Text, Dict, List, Union, Optional

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction


def create_log(**kwargs):
    for k, v in kwargs.items():
        print(k, v)
    return True


class ValidateDailyReflectionForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_daily_reflection_form"

    async def validate_confirm_exercise(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:

        # (TODO): Decide how and what to validate form
        if value:
            # return {"confirm_exercise": True}
            return {}
        else:
            # return {"exercise": "None", "confirm_exercise": False}
            return {}


class ActionSubmitResults(Action):
    def name(self) -> Text:
        return "action_submit_results"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:

        feelings = tracker.get_slot("feelings")
        stuck_to_plans = tracker.get_slot("stuck_to_plans")
        focus_on_tasks = tracker.get_slot("focus_on_tasks")
        strategic = tracker.get_slot("strategic")
        improvements = tracker.get_slot("improvements")
        self_reflection = tracker.get_slot("self_reflection")

        response = create_log(
            feelings=feelings,
            stuck_to_plans=stuck_to_plans,
            focus_on_tasks=focus_on_tasks,
            strategic=strategic,
            improvements=improvements,
            self_reflection=self_reflection
        )

        dispatcher.utter_message("Thanks, your answers have been recorded!")
        return []
