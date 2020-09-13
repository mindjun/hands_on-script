"""
获取站点和路线信息
"""
import re
import requests


class DataFetch(object):
    def __init__(self):
        self.lines_dict = dict()
        self.stations_dict = dict()

    @staticmethod
    def _requests(url, method):
        return requests.request(method, url)

    def get_all_station(self):
        response = self._requests('http://service.shmetro.com/skin/js/pca.js', 'GET')
        lines = re.findall(re.compile('var lines = {\r\n(.*?)\r\n}', re.S), response.text)
        for line in lines[0].split('\r\n'):
            line_name, line_stations = line.split(':')
            self.lines_dict[line_name.replace('"', '')] = line_stations[1:-2].replace('"', '').split(',')
        stations = re.findall(re.compile('var stations = {(.*?)}', re.S), response.text)
        for station in stations[0].split(','):
            line_no, station_name = station.split(':')
            self.stations_dict[line_no.replace('"', '')] = station_name.replace('"', '')


data_fetch = DataFetch()
data_fetch.get_all_station()
print(data_fetch.stations_dict)
print(data_fetch.lines_dict)
