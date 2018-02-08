import requests, json
from base64 import b64encode
from multiprocessing import Pool
import os

class teste():
    def __init__(self):
        self.__url = os.environ('url')
        self.__header = {'Content-Type': 'application/x-www-form-urlencoded'}
        self.__grant_type = 'client_credentials'
        self.__client_id = os.environ('client_id')
        self.__client_secret = os.environ('client_secret')
        self.__auth = self.get_auth()

    @property
    def ip(self):
        uri = '/testecarga/ip'
        self.__header.update({'authorization': 'Bearer %s' % self.__auth})
        r = requests.get(('%s%s' % (self.__url, uri)), headers=self.__header)
        return json.loads(r.text)['origin'], r.elapsed
        #return r.text, r.elapsed
    def get_auth(self):
        uri = '/testecarga/oauth/token/'

        self.__header.update({'authorization': 'Basic %s' % str(
            b64encode((self.__client_id + ':' + self.__client_secret).encode('utf-8')))[2:-1]})
        data = {'grant_type': self.__grant_type, 'client_id': self.__client_id, 'client_secret': self.__client_secret}
        r = requests.post(('%s%s' % (self.__url, uri)), data=data, headers=self.__header)

        return json.loads(r.text)['access_token']


def exec_calls(c):
    teste_1 = teste()
    count = 0
    while count < 500:
        count += 1
        result, elapsed = teste_1.ip

    print('Thread %s - Teste %s - %s - %s' % (c,count, result, elapsed))


if __name__ == '__main__':

    with Pool(25) as p:

        p.map(exec_calls,[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25])