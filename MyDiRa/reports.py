# from datetime import datetime, timedelta

# import core

from random import randint


class ChartData(object):

    @classmethod
    def get_avg_by_day(cls, user, days):
        # now = datetime.now(tz=user.settings.time_zone).date()

        glucose_averages = randint(80, 300)

        data = {'dates': [1,2,3,4,5,6,7,8,9,10], 'values': [100,110,120,130,140,150,160,170,180,190,200]}
        # for avg in glucose_averages:
        #     data['dates'].append(avg['record_date'].)
        #     data['values'].append(core.utils.round_value(avg['avg_value']))

        return data
