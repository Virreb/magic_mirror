import vasttrafik
import dash_html_components as html
from datetime import datetime, timedelta
from math import ceil

KEY = "x6rHJ4c6XA4wk7Z9rDwv9WIL0awa"
SECRET = "GUwBHbT2lRlKjB8uqaRogVycar8a"


KEY_HEADER_MAPPING = {'name': 'Name',
        'sname': 'Linje',
        'type': 'Type',
        'stopid': 'Stop ID',
        'stop': 'Station',
        'time': 'Avgår',
        'date': 'Date',
        'journeyid': 'Journey ID',
        'direction': 'Mot',
        'track': 'Hållplats',
        'rtTime': 'Avgår (korr)',
        'rtDate': 'Real-time Date',
        'fgColor': 'fgColor',
        'bgColor': 'bgColor',
        'stroke': 'Stroke',
        'accessibility': 'accessibility'}


class VTInfo(object):
    def __init__(self, station, travel_information, forecast_minutes, max_departures):
        self.station = station
        self.travel_information = travel_information
        self.forecast_minutes = forecast_minutes
        self.max_departures = max_departures
        self.data = VTDataReader(self.station).read_departure_board_station()

    def display_info(self):
        headers = [KEY_HEADER_MAPPING[x] for x in self.travel_information]
        table_header = [html.Tr([html.Th(col) for col in headers])]
        table_body = []
        current_time = datetime.today().time()
        nbr_shown_departures = 0

        for departure in self.data:
            table_row = []

            time = datetime.strptime(departure['time'], '%H:%M')
            break_time = (time + timedelta(minutes=self.forecast_minutes)).time()

            if current_time > break_time or nbr_shown_departures >= self.max_departures:
                continue

            if 'rtTime' in departure:
                rt_time = datetime.strptime(departure['rtTime'], '%H:%M')

                if rt_time >= time:
                    delayed = rt_time - time
                else:
                    delayed = time - rt_time

                delayed = ceil(delayed.seconds/60)
                if delayed < 0:
                    departure['time'] += f' - {delayed}'
                else:
                    departure['time'] += f' + {delayed}'
            else:
                departure['rtTime'] = None

            for elem in [departure[x] for x in self.travel_information]:
                table_row.append(html.Td(elem))

            table_body.append(html.Tr(children=table_row, style={'backgroundColor': departure['fgColor']}))
            nbr_shown_departures += 1

        title = html.H4(self.station)
        table = html.Table(table_header + table_body)
        return html.Div(children=[title, table])


class VTDataReader(object):
    def __init__(self, station):
        self.jp = vasttrafik.JournyPlanner(key=KEY, secret=SECRET)
        self.station = station

    def read_departure_board_station(self):
        station_id = self.jp.location_name(self.station)[0]['id']
        return self.jp.departureboard(station_id)
