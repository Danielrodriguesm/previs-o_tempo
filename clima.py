import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
Cidade = "Rio de Janeiro"

link =f"https://api.openweathermap.org/data/2.5/weather?q={Cidade}&appid={API_KEY}&lang=pt_br"

requisicao = requests.get(link)
requisicao_dic =(requisicao.json())
descricao = requisicao_dic ['weather'][0]['description']
temperatura = round(requisicao_dic ['main']['temp'] - 273.15, 1)
print(descricao, f"{temperatura:.1f}ºC")                                                                                                                                                                                                                                          