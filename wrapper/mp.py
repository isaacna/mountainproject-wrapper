import requests

class MP(object):
    #init with member variables
    def __init__(self, key, email):
        self.key = key
        self.email = email
        self.base_url = 'https://www.mountainproject.com/data/'

    #create getUser endpoint and get JSON 
    def get_user(self):
        url = self.base_url + 'get-user?'
        url += ('email=' + self.email)
        url += ('&key=' + self.key)
        r = requests.get(url)
        return r.json()
    
    #create getTicks endpoint and get JSON
    def get_ticks(self):
        url = self.base_url + 'get-ticks?'
        url += ('email=' + self.email)
        url += ('&key=' + self.key)
        r = requests.get(url)
        return r.json()

    #create getToDos endpoint and get JSON
    def get_to_dos(self,start_index=0):
        url = self.base_url + 'get-to-dos?'
        url += ('email=' + self.email)
        url += ('&key=' + self.key)
        url += ('&startPos=' + str(start_index))
        r = requests.get(url)
        return r.json()

    #create getRoutesLatLon endpoint and get JSON
    def get_routes_lat_lon(self, lat, lon, limit=15, dist=10):
        url = self.base_url + 'get-routes-for-lat-lon?'
        url += ('lat=' + str(lat))
        url += ('&lon=' + str(lon))
        url += ('&key=' + self.key)
        url += ('&maxResults=' + str(limit))
        url += ('&maxDistance=' + str(dist))
        r = requests.get(url)
        return r.json()

