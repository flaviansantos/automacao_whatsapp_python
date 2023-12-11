import webbrowser
from time import sleep
import pyautogui
import requests
import json

headers={
  'Accept':'*/*',
  'Accept-Language':'zh-CN,zh;q=0.9,en;q=0.8,ja;q=0.7',
  'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
};

request = requests.get("http://localhost:5186/WhatsApp/GetMessageAVencer",headers=headers)
todos = json.loads(request.content, encoding='utf-8')

for i in todos:
    telefone = i['telefone']
    mensagem = i['mensagem']
    link_mensagem_whatsapp = f'https://web.whatsapp.com/send?phone={telefone}&text={mensagem}'
    webbrowser.open(link_mensagem_whatsapp)
    sleep(20)
    seta = pyautogui.locateCenterOnScreen('seta.png')
    sleep(10)
    pyautogui.click(seta[0], seta[1])
    sleep(10)
    pyautogui.hotkey('ctrl','w')    
    sleep(10)   


    




