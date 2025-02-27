from otree.api import BasePlayer, BaseSubsession, BaseConstants, BaseGroup, Page, WaitPage, models, widgets
import json, itertools
class C(BaseConstants):
    NAME_IN_URL = 'css'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 10
    NETWORKS = ["type_I", "type_II"]
    MAPPING = {i: chr(64 + i) for i in range(1, 5)}  # Dynamically generate 'A', 'B', 'C', 'D'

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    threshold = models.IntegerField(
        label="Please enter a threshold value",
        choices=[1, 2, 3, 4],
    )

    revolt = models.BooleanField(
        label="Do you want to revolt?",
        choices=[True, False],
    )

class Group(BaseGroup):
    treatment = models.StringField()

def creating_session(subsession: Subsession):
    # treatment = itertools.cycle(C.NETWORKS)
    # for group in subsession.get_groups():
    #     if group.get_player_by_id(1).round_number == 1:
    #         group.treatment = next(treatment)
    pass

class WelcomePage(Page):
    @staticmethod
    def is_displayed(player):
        if player.round_number == 1:
            return True
        return False

    @staticmethod
    def vars_for_template(player):
        pass

    @staticmethod
    def before_next_page(player, timeout_happened):
        pass

class IntroPage(Page):
    @staticmethod
    def is_displayed(player):
        if player.round_number == 1:
            return True
        return False

    @staticmethod
    def vars_for_template(player):
        return {
            'num_rounds': C.NUM_ROUNDS
        }

class RulePhase1Page(Page):
    @staticmethod
    def is_displayed(player):
        if player.round_number == 1:
            return True
        return False

class RulePhase2Page(Page):
    @staticmethod
    def is_displayed(player):
        if player.round_number == 1:
            return True
        return False
    
    @staticmethod
    def vars_for_template(player):
        network_file = f"_static/networks/{player.session.config['network']}.json"

        with open(network_file, "r") as f:
            data = json.load(f)

        return {
            "me": json.dumps(C.MAPPING.get(player.id_in_group, "Unknown")),
            "nodes": json.dumps(data.get("nodes", [])),
            "links": json.dumps(data.get("links", [])),
        }
    
class RulePhase3Page(Page):
    @staticmethod
    def is_displayed(player):
        if player.round_number == 1:
            return True
        return False
    
class RulePhase4Page(Page):
    @staticmethod
    def is_displayed(player):
        if player.round_number == 1:
            return True
        return False
    
    @staticmethod
    def vars_for_template(player):
        rewards_file = "_static/rewards.json"
        with open(rewards_file, "r") as f:
            data = json.load(f)
        
        return {
            "rewards": data,
            # TODO: Set up the example data
            "revolt_outcome": json.dumps(True),
            "num_participants": "3",
            "rewards": 100,
        }

class Phase1Page(Page):
    form_model = 'player'
    form_fields = ['threshold']

    @staticmethod
    def is_displayed(player):
        return True

    @staticmethod
    def vars_for_template(player):
        return {
            "round_number": player.round_number
        }

    @staticmethod
    def before_next_page(player, timeout_happened):
        # TODO: Implement the logic for the threshold
        pass

class Phase2Page(Page):
    @staticmethod
    def is_displayed(player):
        return True

    @staticmethod
    def vars_for_template(player):
        network_file = f"_static/networks/{player.session.config['network']}.json"

        with open(network_file, "r") as f:
            data = json.load(f)

        return {
            "round_number": player.round_number,
            "me": json.dumps(C.MAPPING.get(player.id_in_group, "Unknown")),
            "nodes": json.dumps(data.get("nodes", [])),
            "links": json.dumps(data.get("links", [])),
        }

class Phase3Page(Page):
    form_model = 'player'
    form_fields = ['revolt']

    @staticmethod
    def is_displayed(player):
        return True

    @staticmethod
    def vars_for_template(player):
        pass

    @staticmethod
    def before_next_page(player, timeout_happened):
        pass
        # TODO: Calculate the outecome here

class Phase4Page(Page):
    @staticmethod
    def is_displayed(player):
        return True

    @staticmethod
    def vars_for_template(player):
        rewards_file = "_static/rewards.json"
        with open(rewards_file, "r") as f:
            data = json.load(f)
        
        return {
            "rewards": data,

            # TODO: Replace the example data
            "round_number": player.round_number,
            "revolt_outcome": json.dumps(True),
            "num_participants": "3",
            "rewards": 100,
        }

class ArrivalPage(WaitPage):
    # group_by_arrival_time = True

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

# page_sequence = [ArrivalPage, WelcomePage, IntroPage, RulePhase1Page, RulePhase2Page, RulePhase3Page, RulePhase4Page, ArrivalPage]
# page_sequence = [WelcomePage, IntroPage, RulePhase1Page, RulePhase2Page, RulePhase3Page, RulePhase4Page]
page_sequence = [Phase1Page, Phase2Page, Phase3Page, Phase4Page]
