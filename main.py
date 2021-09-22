import requests
import time
import logging

def raw_art_request(art_number, retries = 5):
  """
    @title: Raw ART data web request
    @name: raw_art_request
    @description: Function that requests ARTs data, verifies if the data received is valid and returns it if so or None if not. 
    It also retries the request if a Exception is raised, after this subtracts the retries value.

    @param art_number: number
    @param retries: defined in params number
    @return data dict 

    @examples
    raw_art_request(IN00214132) return {'numero':'IN00214132',...}
    raw_art_request(1) return None
  """
  try:
    url = f"https://portalservicos.crea-rj.org.br/rest-api/crea/art/{art_number}"

    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

    response = requests.get(url, headers=headers)
    response = response.json()
    raw_data = response.get('data', [])
    
    if type(art_number) == int:
      art_number = str(art_number)
    if raw_data.get('numero') == art_number:  
      return raw_data

    else:
      return None
    
  except Exception as e:
    if retries > 0:
      time.sleep(2)
      return raw_art_request(art_number, retries - 1)

    raise e.CallableException()

def collect_raw_art_data(art_number):
  """
    @title: Collect raw ART data
    @name: collect_raw_art_data
    @description: Function that collects raw ART data coming within 'raw_art_request' function and verify within 'verif_response_data' helpers function.

    @param art_number: number
    @return data dict

    @examples
    collect_raw_art_data(2020180028152) return {'numero':'2020200056031',...}
    collect_raw_art_data(1) return "Dados crus da ART 1 não encontrados."
  """

  raw_data = raw_art_request(art_number)

  if raw_data != None:
    return raw_data

  else:
    return f"Dados crus da ART {art_number} não encontrados."

def companies_list_for_mock_test():
    companies_list = ["Atlas Schindler", "Thyssenkrupp", "Olgen Elevators", "Otis", "MONTELE LTDA"]
    return companies_list