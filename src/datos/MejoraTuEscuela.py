import requests, sys
from requests.exceptions import HTTPError
import json, logging
import pandas as pd
from pandas.io.json import json_normalize
#import time
# logger
logging.basicConfig(filename='escuelas.log',level=logging.INFO,format='%(asctime)s : %(levelname)s : %(name)s : %(message)s')
log = logging.getLogger(__name__)
def getData():
    URL='http://www.mejoratuescuela.org/api/escuelas/?pagination=100'
    data = json.loads('{"entidad":null,"municipio":null,"localidad":null,"p":1,"sort":"Sem\xE1foro de Resultados Educativos","type_test":"planea","schoolStatus":1,"niveles":""}')    
    for page in range(1,2821): # 46997 +1
        data['p']=page
        try:
            response = requests.post(URL, data=data, verify=False)
            response.raise_for_status()
            jsonResponse = response.json()
            #log.info(f'page: {page} - {jsonResponse["escuelas"]}')
            log.info(f'page: {page} - 2821')
            df = json_normalize(jsonResponse['escuelas'],sep="_")
            with open('escuelas.csv', 'a') as f:
                df.to_csv(f, header=f.tell()==0)
            #time.sleep(2) # << Por si el servidor no aguanta los madrazos 
        except HTTPError as http_err:
            log.error(f'HTTP error occurred: {http_err}')
        except Exception as err:
            log.error(f'Other error occurred: {err}')
def run():
    getData()
if __name__ == '__main__':
    try:
        run()
    except KeyboardInterrupt:
        sys.exit(0)