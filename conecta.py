import openai
import webbrowser
import speech_recognition as sr
import pygame
import os
from gtts import gTTS

# Configuração da API do OpenAI
openai.api_key = "SUA_CHAVE_API"  # Substitua pela sua chave de API

# Função para gerar áudio da resposta
def cria_audio(audio, mensagem, lang='pt-br'):
    try:
        tts = gTTS(mensagem, lang=lang)
        tts.save(audio)  # Salva o arquivo de áudio

        # Inicializa o pygame mixer para tocar o áudio
        pygame.mixer.init()
        pygame.mixer.music.load(audio)  # Carrega o áudio
        pygame.mixer.music.play()  # Reproduz o áudio

        # Aguarda até que o áudio termine de ser reproduzido
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(5)

        pygame.mixer.music.stop()  # Para a reprodução do áudio
        pygame.mixer.quit()  # Fecha o mixer do pygame
        os.remove(audio)  # Remove o arquivo de áudio após reprodução
    except Exception as e:
        print(f"Erro ao gerar ou reproduzir áudio: {e}")

# Função para processar comandos conhecidos
def processa_comando(mensagem):
    comandos = {
        'coreto': ("http://coreto.recife.pe.gov.br", "Aqui está o que encontrei sobre Coreto."),
        'conecta recife': ("http://conecta.recife.pe.gov.br", "Aqui está o que encontrei sobre Conecta Recife."),
        'conectar recife': ("http://conecta.recife.pe.gov.br", "Aqui está o que encontrei sobre Conecta Recife."),
        'go recife': ("http://gorecife.recife.pe.gov.br", "Aqui está o que encontrei sobre o Go Recife."),
        'gol recife': ("http://gorecife.recife.pe.gov.br", "Aqui está o que encontrei sobre o Go Recife."),
        'edit ai': ("http://editai.recife.pe.gov.br", "Aqui está o que encontrei sobre o Edit Ai."),
        'edit aí': ("http://editai.recife.pe.gov.br", "Aqui está o que encontrei sobre o Edit Ai."),
        'edite aí': ("http://editai.recife.pe.gov.br", "Aqui está o que encontrei sobre o Edit Ai."),
        'edite ai': ("http://editai.recife.pe.gov.br", "Aqui está o que encontrei sobre o Edit Ai."),
        'edith aí': ("http://editai.recife.pe.gov.br", "Aqui está o que encontrei sobre o Edit Ai."),
        'edith ai': ("http://editai.recife.pe.gov.br", "Aqui está o que encontrei sobre o Edit Ai."),
        'gestor recife': ("https://recifegestor.com.br/", "Aqui está o que encontrei sobre o Gestor Recife."),
        'recife gestor': ("https://recifegestor.com.br/", "Aqui está o que encontrei sobre o Gestor Recife."),
        'desligar': (None, "Assistente desligado."),  # Comando para desligar
    }

    for chave, (url, resposta) in comandos.items():
        if chave in mensagem:
            if chave == "desligar":
                cria_audio(f"{chave}.mp3", resposta)
                return "desligar"  # Retorna um sinal para encerrar o programa
            if url:
                webbrowser.open(url)
                cria_audio(f"{chave}.mp3", resposta)
                return True  # Retorna True para indicar que o comando foi processado

    return False  # Retorna False caso nenhum comando tenha sido encontrado

# Função otimizada para escuta contínua
def escuta_continua():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Assistente ativado. Diga algo ou 'desligar' para encerrar.")
        while True:
            try:
                print("Estou ouvindo...")
                audio = recognizer.listen(source, timeout=None, phrase_time_limit=7)
                mensagem = recognizer.recognize_google(audio, language="pt-BR").lower()
                print(f"Você disse: {mensagem}")

                # Verifica se a mensagem contém um comando reconhecido
                resultado = processa_comando(mensagem)
                if resultado == "desligar":
                    break  # Encerra o loop principal se o comando for "desligar"
                elif resultado:
                    continue  # Se for um comando conhecido, volta a escutar

                # Caso contrário, faz a consulta ao ChatGPT
                resposta_chatgpt(mensagem)

            except sr.UnknownValueError:
                print("Não entendi o que foi dito.")
            except sr.RequestError as e:
                print(f"Erro na API de reconhecimento de fala: {e}")
                cria_audio("erro_api.mp3", "Erro na conexão com o serviço de reconhecimento de fala.")
            except Exception as e:
                print(f"Erro inesperado: {e}")

# Função para enviar mensagem ao ChatGPT
def resposta_chatgpt(mensagem):
    try:
        mensagens = [
            {"role": "system", "content": "Você é Conecta, o assistente virtual da Prefeitura do Recife. Ajude o usuário com informações relevantes e amigáveis."},
            {"role": "user", "content": mensagem}
        ]

        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=mensagens,
            max_tokens=150,
            temperature=0.7,
        )

        resposta_texto = resposta['choices'][0]['message']['content'].strip()
        print(f"Conecta: {resposta_texto}")

        cria_audio("resposta.mp3", resposta_texto)

    except Exception as e:
        print(f"Erro ao obter resposta do ChatGPT: {e}")
        cria_audio("erro_resposta.mp3", "Ocorreu um erro ao processar sua solicitação.")

# Função principal que coordena o assistente
def main():
    try:
        cria_audio("ola.mp3", "Olá, sou o Conecta, sua assistente virtual da Prefeitura do Recife. Como posso ajudar?")
        escuta_continua()
    except Exception as e:
        print(f"Erro na execução principal: {e}")
        cria_audio("erro_execucao.mp3", "Ocorreu um erro ao iniciar o assistente.")

if __name__ == '__main__':
    main()
