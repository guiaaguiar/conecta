import webbrowser
import speech_recognition as sr
import pygame
import os
from gtts import gTTS
import re

# Função para gerar áudio de repetição
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

# Função de tratamento de erros de reconhecimento de fala e rede
def tratamento_excecoes(erro, tipo="reconhecimento"):
    if tipo == "reconhecimento":
        if isinstance(erro, sr.UnknownValueError):
            print("Não entendi, pode repetir?")
        else:
            print("Erro ao reconhecer o áudio")
    elif tipo == "rede":
        print("Erro de conexão com o serviço de reconhecimento.")
    else:
        print(f"Erro inesperado: {erro}")

# Função para escutar e reconhecer o que você fala
def monitora_audio():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        recon.adjust_for_ambient_noise(source)  # Ajusta o reconhecimento para o ambiente
        while True:
            print('Diga "Conecta" para ativar ou "desligar" para desativar...')
            audio = recon.listen(source)  # Captura o áudio
            try:
                # Reconhecimento de fala via Google
                mensagem = recon.recognize_google(audio, language='pt-br').lower()
                print(f'Você disse: {mensagem}')

                if "conecta" in mensagem:  # Ativa o assistente
                    cria_audio("conecta.mp3", "Estou te ouvindo. Como posso ajudar?")
                    executa_comandos()
                elif "desligar" in mensagem:  # Desliga o assistente
                    cria_audio("desligar.mp3", "Assistente desligado.")
                    break
            except Exception as e:
                tratamento_excecoes(e, "reconhecimento")

# Função para verificar e executar comandos
def executa_comandos():
    recon = sr.Recognizer()
    with sr.Microphone() as source:
        recon.adjust_for_ambient_noise(source)  # Ajusta o reconhecimento para o ambiente
        comandos = {
            'coreto': ("http://coreto.recife.pe.gov.br", "Aqui está o que encontrei sobre Coreto."),
            'conecta recife': ("http://conecta.recife.pe.gov.br", "Aqui está o que encontrei sobre Conecta Recife."),
            'go recife': ("http://gorecife.recife.pe.gov.br", "Aqui está o que encontrei sobre o Go Recife."),
            'edit ai': ("http://editai.recife.pe.gov.br", "Aqui está o que encontrei sobre o Edit Ai.")
        }

        while True:
            print("Comando ativado. Diga algo ou 'desligar' para parar.")
            audio = recon.listen(source)
            try:
                # Reconhecimento de fala
                mensagem = recon.recognize_google(audio, language='pt-br').lower()
                print(f'Você disse: {mensagem}')

                comando_executado = False
                for chave, (url, resposta) in comandos.items():
                    if re.search(r'\b' + re.escape(chave) + r'\b', mensagem):
                        webbrowser.open(url)
                        cria_audio(f"{chave}.mp3", resposta)
                        comando_executado = True
                        break

                if not comando_executado:
                    if 'desligar' in mensagem:
                        cria_audio("desligar.mp3", "Assistente desligado.")
                        break  # Sai do loop e desliga o assistente
                    else:
                        cria_audio("resposta.mp3", f"Você disse: {mensagem}")
            except Exception as e:
                tratamento_excecoes(e, "reconhecimento")

# Função principal que coordena o assistente
def main():
    try:
        cria_audio("ola.mp3", "Olá, sou o Conecta, sua assistente virtual! Diga 'Conecta' para começar.")
        monitora_audio()  # Inicia o monitoramento de comandos
    except Exception as e:
        print(f"Erro na execução principal: {e}")
        cria_audio("erro_execucao.mp3", "Ocorreu um erro ao iniciar o assistente.")

if __name__ == '__main__':
    main()
