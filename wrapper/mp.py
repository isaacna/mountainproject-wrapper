import requests

class MP(object):
    def __init__(self, key, email):
        self.key = key
        self.email = email
        self.base_url = 'https://www.mountainproject.com/data/'

    def data(self):
        return {'key' : self.key, 'email' : self.email}
    
    def get_user(self):
        url = self.base_url + 'get-user?'
        url += ('email=' + self.email)
        url += ('&key=' + self.key)
        r = requests.get(url)
        return r.json()
    
    def get_ticks(self):
        url = self.base_url + 'get-ticks?'
        url += ('email=' + self.email)
        url += ('&key=' + self.key)
        r = requests.get(url)
        return r.json()

    def get_to_dos(self):
        url = self.base_url + 'get-to-dos?'
        url += ('email=' + self.email)
        url += ('&key=' + self.key)
        r = requests.get(url)
        return r.json()

    def get_routes_lat_lon(self, lat, lon):
        url = self.base_url + 'get-routes-for-lat-lon?'
        url += ('lat=' + str(lat))
        url += ('&lon=' + str(lon))
        url += ('&key=' + self.key)
        r = requests.get(url)
        return r.json()

