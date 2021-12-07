from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


author = 'Your name here'

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'gini_new'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    slider_top20 = models.IntegerField()
    slider_second20 = models.IntegerField()
    slider_third20 = models.IntegerField()
    slider_fourth20 = models.IntegerField()

    check_slider1 = models.IntegerField(blank=True)
    check_slider2 = models.IntegerField(blank=True)
    check_slider3 = models.IntegerField(blank=True)
    check_slider4 = models.IntegerField(blank=True)

