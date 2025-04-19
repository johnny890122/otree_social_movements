from otree.api import BasePlayer, BaseSubsession, BaseConstants, BaseGroup, Page, WaitPage, models, widgets
import json, itertools
import networkx as nx
import social_movements.utils as utils
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
        label="How many people (including self) does it take to motivate a person to participate in the revolt?",
        choices=[1, 2, 3, 4], 
    )

    revolt = models.BooleanField(
        label="Do you want to revolt?",
        choices=[True, False],
    )

    endownment = models.CurrencyField(default=100)
    my_label = models.StringField()

class Group(BaseGroup):
    treatment = models.StringField()

def creating_session(subsession: Subsession):
    for group in subsession.get_groups():
        for player in group.get_players():
            player.my_label = C.MAPPING.get(player.id_in_group, "Unknown")

class WelcomePage(Page):
    @staticmethod
    def is_displayed(player):
        if player.round_number == 1:
            return True
        return False

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

class Phase1Page(Page):

    form_model = 'player'
    form_fields = ['threshold']

    @staticmethod
    def is_displayed(player):
        return True
    
    @staticmethod
    def vars_for_template(player):
        networks_data = utils.load_network_data(player.session.config["network"])
        rewards_data = utils.load_rewards_data()
        for node in networks_data["nodes"]:
            if node["id"] == player.my_label:
                my_threshold = node["example_threshold"]
                break
        
        is_practice = True if player.round_number == 1 else False

        return {
            "example_threshold": my_threshold,
            "rewards": rewards_data,
            "is_practice": is_practice,
            "round_number": player.round_number - 1,
        }

class RulePhase2Page(Page):
    @staticmethod
    def is_displayed(player):
        if player.round_number == 1:
            return True
        return False
    
    @staticmethod
    def vars_for_template(player):
        network_data = utils.load_network_data(player.session.config["network"])
        rewards_data = utils.load_rewards_data()
        for node in network_data["nodes"]:
            if node["id"] == player.my_label:
                join_revolt = node["example_join_revolt"]
                break


        G = nx.Graph()
        G.add_nodes_from(
            [node["id"] for node in network_data["nodes"]]
        ) 
        G.add_edges_from(
            [(edge["source"], edge["target"]) for edge in network_data["links"] if edge["show"]]
        )
        my_neighbors = list(G.neighbors(player.my_label))
        for node in network_data["nodes"]:
            if node["id"] not in my_neighbors and node["id"] != player.my_label:
                node["example_threshold"] = "Unknown (Not your neighbor)"

        return {
            "me": json.dumps(player.my_label),
            "nodes": json.dumps(network_data.get("nodes", [])),
            "links": json.dumps(network_data.get("links", [])),
            "join_revolt": join_revolt,
            "rewards": rewards_data,
        }
    
class RulePhase3Page(Page):
    @staticmethod
    def is_displayed(player):
        if player.round_number == 1:
            return True
        return False
    
    @staticmethod
    def vars_for_template(player):
        rewards_data = utils.load_rewards_data()
        network_data = utils.load_network_data(player.session.config["network"])
        revolt_success = network_data.get("revolt_success", False)

        num_participants = 0   
        for node in network_data["nodes"]:
            if node["example_join_revolt"]:
                num_participants += 1
        
        for reward in rewards_data:
            if reward["participants"] == num_participants:
                reward_from_game = reward["rewardSuccess"]
                loss_from_game = reward["lossFailed"]
                break

        for node in network_data["nodes"]:
            if node["id"] == player.my_label:
                join_revolt = node["example_join_revolt"]
                break

        if revolt_success and join_revolt:
            gain_or_loss = reward_from_game
        elif not revolt_success and join_revolt:
            gain_or_loss = -loss_from_game
        else:
            gain_or_loss = 0


        return {
            "rewards": rewards_data,
            "revolt_success": revolt_success,
            "num_participants": num_participants,
            "gain_or_loss": gain_or_loss,
            "payoff": player.endownment + gain_or_loss,
            "join_revolt": join_revolt,
        }

class Phase2Page(Page):
    @staticmethod
    def is_displayed(player):
        return True

    @staticmethod
    def vars_for_template(player):
        data = utils.load_network_data(player.session.config["network"])

        return {
            "round_number": player.round_number,
            "me": json.dumps(player.my_label),
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

# page_sequence = [ArrivalPage,  RulePhase1Page, RulePhase2Page, RulePhase3Page, RulePhase4Page, ArrivalPage]
page_sequence = [WelcomePage, IntroPage, RulePhase1Page, RulePhase2Page, RulePhase3Page]
# page_sequence = [Phase1Page, Phase2Page, Phase3Page, Phase4Page]
