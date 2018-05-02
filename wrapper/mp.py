import requests, urlparse

class MP(object):
    #init with member variables
    def __init__(self, key, email):
        self.key = key
        self.email = email
        self.base_url = 'https://www.mountainproject.com/data/'

    #create getUser endpoint and get JSON 
    def get_user(self):
        url = urlparse.urljoin(self.base_url,'get-user')
        vals = {'email' : self.email, 'key' : self.key} 
        r = requests.get(url, params=vals)
        return r.json()
    
    #create getTicks endpoint and get JSON
    def get_ticks(self):
        url = urlparse.urljoin(self.base_url,'get-ticks')
        vals = {'email' : self.email, 'key' : self.key} 
        r = requests.get(url, params=vals)
        return r.json()

    #create getToDos endpoint and get JSON
    def get_to_dos(self, start_index=0):
        url = urlparse.urljoin(self.base_url,'get-to-dos')
        vals = {'email' : self.email, 'key' : self.key, 'startPos' : start_index} 
        r = requests.get(url, params=vals)
        return r.json()

    #create getRoutesLatLon endpoint and get JSON
    def get_routes_lat_lon(self, lat, lon, limit=15, dist=10):
        url = urlparse.urljoin(self.base_url,'get-routes-for-lat-lon')
        vals = {'lat' : lat, 'lon' : lon, 'key' : self.key, 'maxResults' : limit, 'maxDistance' : dist} 
        r = requests.get(url, params=vals)
        return r.json()

