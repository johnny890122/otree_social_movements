from otree.api import BasePlayer, BaseSubsession, BaseConstants, BaseGroup, Page, WaitPage, models
import json, itertools
class C(BaseConstants):
    NAME_IN_URL = 'css'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 10
    NETWORKS = ["type_I", "type_II"]

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    pass

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

        mapping = {i: chr(64 + i) for i in range(1, 5)}  # Dynamically generate 'A', 'B', 'C', 'D'

        return {
            "me": json.dumps(mapping.get(player.id_in_group, "Unknown")),
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

class Phase1Page(Page):
    @staticmethod
    def is_displayed(player):
        pass

    @staticmethod
    def vars_for_template(player):
        pass

    @staticmethod
    def before_next_page(player, timeout_happened):
        pass

class Phase2Page(Page):
    @staticmethod
    def is_displayed(player):
        pass

    @staticmethod
    def vars_for_template(player):
        pass

    @staticmethod
    def before_next_page(player, timeout_happened):
        pass

class Phase3Page(Page):
    @staticmethod
    def is_displayed(player):
        pass

    @staticmethod
    def vars_for_template(player):
        pass

    @staticmethod
    def before_next_page(player, timeout_happened):
        pass

class Phase4Page(Page):
    @staticmethod
    def is_displayed(player):
        pass

    @staticmethod
    def vars_for_template(player):
        pass

    @staticmethod
    def before_next_page(player, timeout_happened):
        pass


class ArrivalPage(WaitPage):
    # group_by_arrival_time = True

    @staticmethod
    def is_displayed(player):
        return player.round_number == 1

# page_sequence = [ArrivalPage, WelcomePage, IntroPage, RulePhase1Page, RulePhase2Page, RulePhase3Page, RulePhase4Page, ArrivalPage]
page_sequence = [WelcomePage, IntroPage, RulePhase1Page, RulePhase2Page, RulePhase3Page, RulePhase4Page]
