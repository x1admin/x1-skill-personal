from ovos_utils import classproperty
from ovos_utils.process_utils import RuntimeRequirements
from ovos_workshop.decorators import intent_handler
from ovos_workshop.skills import OVOSSkill
from ovos_bus_client.message import Message


class PersonalSkill(OVOSSkill):
    @classproperty
    def runtime_requirements(self):
        return RuntimeRequirements(internet_before_load=False,
                                   network_before_load=False,
                                   gui_before_load=False,
                                   requires_internet=False,
                                   requires_network=False,
                                   requires_gui=False,
                                   no_internet_fallback=True,
                                   no_network_fallback=True,
                                   no_gui_fallback=True)

#START OF CUSTOM INTENTS
    
    @intent_handler("Gender.intent")
    def handle_gender_intent(self, message: Message):
        self.speak_dialog("gender")
        
    @intent_handler("DoYouRhyme.intent")
    def handle_do_you_rhyme(self, message: Message):
        self.speak_dialog("tell.a.rhyme")

    @intent_handler("DoYouDream.intent")
    def handle_do_you_dream(self, message: Message):
        self.speak_dialog("dream")
        
#END OF CUSTOM INTENTS
    
    @intent_handler("WhenWereYouBorn.intent")
    def handle_when_were_you_born_intent(self, message: Message):
        self.speak_dialog("when.was.i.born",
                          {"year": self.settings.get("year_of_birth", 2015)})

    @intent_handler("WhereWereYouBorn.intent")
    def handle_where_were_you_born_intent(self, message: Message):
        self.speak_dialog("where.was.i.born",
                          {"location": self.settings.get("location_of_birth", "Lawrence Kansas")})

    @intent_handler("WhoMadeYou.intent")
    def handle_who_made_you_intent(self, message: Message):
        self.speak_dialog("who.made.me",
                          {"creator": self.settings.get("creator", "OpenVoiceOS")})

    @intent_handler("WhoAreYou.intent")
    def handle_who_are_you_intent(self, message: Message):
        assistant_name = self.settings.get("assistant_name")
        if not assistant_name:
            assistant_name = self._parse_name_from_ww(
                self.config_core.get("listener", {}).get("wake_word", "mycroft"))
        self.speak_dialog("who.am.i", {"name": assistant_name})

    def _parse_name_from_ww(self, ww):
        if ww.startswith("o_"):  # Portuguese wakewords
            ww = ww.replace("o_", "")
        if ww.startswith("ó_"):  # Portuguese wakewords
            ww = ww.replace("ó_", "")
        if ww.startswith("ei_"):  # Portuguese wakewords
            ww = ww.replace("ei_", "")
        name = ww.lower().replace("_", " ").replace("-", " ").replace("hey ", "").replace("say ", "")
        return name

    @intent_handler("WhatAreYou.intent")
    def handle_what_are_you_intent(self, message: Message):
        self.speak_dialog("what.am.i")
