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

class IntroPage(Page):
    @staticmethod
    def is_displayed(player):
        pass

    @staticmethod
    def vars_for_template(player):
        pass

    @staticmethod
    def before_next_page(player, timeout_happened):
        pass

class NetworksPage(Page):
    @staticmethod
    def is_displayed(player):
        pass

    @staticmethod
    def vars_for_template(player):
        pass

    @staticmethod
    def before_next_page(player, timeout_happened):
        pass

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

page_sequence = [IntroPage, NetworksPage, Phase1Page, Phase2Page, Phase3Page, Phase4Page]
