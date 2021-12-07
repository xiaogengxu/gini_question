from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class MyPage(Page):
    form_model = "player"
    form_fields = ['slider_top20', 'slider_second20', 'slider_third20', 'slider_fourth20',
                   'check_slider1', 'check_slider2', 'check_slider3', 'check_slider4']

    def check_slider1_error_message(self, value):
        if not value:
            return 'Please touch and move every slider for each quintile.'

    def check_slider2_error_message(self, value):
        if not value:
            return 'Please touch and move every slider for each quintile.'

    def check_slider3_error_message(self, value):
        if not value:
            return 'Please touch and move every slider for each quintile.'

    def check_slider4_error_message(self, value):
        if not value:
            return 'Please touch and move every slider for each quintile.'


# class ResultsWaitPage(WaitPage):
#     pass
#
#
# class Results(Page):
#     pass


page_sequence = [MyPage]
