import vasttrafik
import dash_html_components as html
import configparser



KEY_HEADER_MAPPING = {'name': 'Name',
		'sname': 'Number',
		'type': 'Type',
		'stopid': 'Stop ID',
		'stop': 'Station', 
		'time': 'Departure',
		'date': 'Date',
		'journeyid': 'Journey ID',
		'direction': 'Direction',
		'track': 'Track',
		'rtTime': 'Real-time Departure',
		'rtDate': 'Real-time Date',
		'fgColor': 'fgColor',
		'bgColor': 'bgColor',
		'stroke': 'Stroke',
		'accessibility': 'accessibility'} 


class VTInfo(object):
	def __init__(self, station, travel_information):
		self.station = station
		self.travel_information = travel_information
		self.data = VTDataReader(self.station).read_departure_board_station()

	def display_info(self):
		headers = [KEY_HEADER_MAPPING[x] for x in self.travel_information]
		table_header = [html.Tr([html.Th(col) for col in headers])]
		table_body = []
		for departure in self.data:
			table_row = []
			for elem in [departure[x] for x in self.travel_information]:
				table_row.append(html.Td(elem))
			table_body.append(html.Tr(children=table_row, style={'backgroundColor': departure['fgColor']}))
		title = html.Div(self.station)
		table = html.Table(table_header + table_body)
		return html.Div(children=[self.station, table])



class VTDataReader(object):
	def __init__(self, station):
		key, secret = self.get_key_secret()
		self.jp = vasttrafik.JournyPlanner(key=key, secret=secret)
		self.station = station
	
	def read_departure_board_station(self):
		station_id = self.jp.location_name(self.station)[0]['id']
		return self.jp.departureboard(station_id)

	def get_key_secret(self):
		configParser = configparser.RawConfigParser()
		configParser.read('config.txt')
		key = configParser.get('Vasttrafik', 'KEY')
		secret = configParser.get('Vasttrafik', 'SECRET')
		return key, secret




if __name__ == '__main__':
	station = 'Bifrost'
	travel_information = ['name', 'time', 'rtTime']
	print(VTInfo(station, travel_information).display_info())
