from otree.api import BasePlayer, Page, BaseSubsession, BaseConstants, BaseGroup

class C(BaseConstants):
    NAME_IN_URL = 'css'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 10

class Subsession(BaseSubsession):
    pass

class Player(BasePlayer):
    pass

class Group(BaseGroup):
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

page_sequence = [WelcomePage, IntroPage, RulePhase1Page, RulePhase2Page, RulePhase3Page, RulePhase4Page]
