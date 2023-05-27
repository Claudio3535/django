import requests
import random
import time
from telegram import Bot
import os
from datetime import datetime, timedelta

# Token do seu bot (obtido ao criar o bot no BotFather) (@botsend_bot)
TOKEN = '5995938268:AAFlzM_KMUogAktNVtldFYWFgG-6rn6ubWs'

# ID do chat ou grupo em que você deseja postar a mensagem
CHAT_ID = '-1001929637740'

# URL da API do Telegram
telegram_api_url = f'https://api.telegram.org/bot5995938268:AAFlzM_KMUogAktNVtldFYWFgG-6rn6ubWs/sendMessage'

# Mapeamento dos jogos para as imagens correspondentes
imagens_jogos = {
    '🐯 FORTUNE TIGER': 'imagens/tigre.png',
    '🐭 FORTUNE MOUSE': 'imagens/mouse.png',
    '🐃 FORTUNE OX': 'imagens/ox_fortun.png',
    '🐰 FORTUNE RABBIT': 'imagens/rabbit.png',
    '🐘 GANESHA GOLD': 'imagens/ganesha_gold.png',
    '🐲 DRAGON TIGER LUCK': 'imagens/dgt.png',
    '🐉 DRAGON HATCH': 'imagens/dragon_hatch.png'
}

# Criação do objeto Bot
bot = Bot(token=TOKEN)

# Função para preencher campos aleatórios
def preencher_campos():
    nome = ['🐯 FORTUNE TIGER',
            '🐭 FORTUNE MOUSE',
            '🐃 FORTUNE OX',
            '🐰 FORTUNE RABBIT',
            '🐘 GANESHA GOLD',
            '🐲 DRAGON TIGER LUCK',
            '🐉 DRAGON HATCH']
    
    jogadas = ['4', '7', '9', '12', '15']
    porcentagem = ['96%', '89%', '90%', '91%', '92%', '93%', '85%', '94%', '87%']
    validade = ['2', '3', '4']
    
    oportunidade = "IDENTIFICADA"
    nome = random.choice(nome)
    jogadas = random.choice(jogadas)
    porcentagem = random.choice(porcentagem)
    validade_minutos = int(random.choice(validade))

    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_imagem = os.path.join(diretorio_atual, imagens_jogos[nome])

    hora_atual = datetime.now()
    validade_horario = hora_atual + timedelta(minutes=validade_minutos)
    validade = validade_horario.strftime("%H:%M:%S")

    mensagem = f'''
    ✅✅ OPORTUNIDADE {oportunidade} ✅✅
     {nome}
    🫰TOTAL DE JOGADAS: {jogadas}
    🎯ACERTIVIDADE: {porcentagem}
    ⏱ Expira às: {validade}
    '''

    return mensagem, caminho_imagem

# Função para enviar mensagem sem imagem
def enviar_mensagem_texto(texto):
    payload = {
        'chat_id': CHAT_ID,
        'text': texto,
        'parse_mode': 'HTML'
    }
    response = requests.post(telegram_api_url, data=payload)
    response.raise_for_status()

# Função para enviar mensagem com imagem
def enviar_mensagem_imagem(texto, caminho_imagem):
    bot.send_photo(chat_id=CHAT_ID, photo=open(caminho_imagem, 'rb'), caption=texto)

# Função principal
def executar():
    while True:
        mensagem, caminho_imagem = preencher_campos()
        enviar_mensagem_imagem(mensagem, caminho_imagem)
        
        # Espera 15 segundos antes de enviar a próxima mensagem
        time.sleep(15)

# Chamada da função principal
if __name__ == '__main__':
    executar()



