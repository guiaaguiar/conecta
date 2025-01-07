import webbrowser
import speech_recognition as sr
import pygame
import os
from gtts import gTTS

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

                if "desligar" in mensagem:
                    cria_audio("desligar.mp3", "Assistente desligado.")
                    break

                processa_comando(mensagem)

            except sr.UnknownValueError:
                print("Não entendi o que foi dito.")
            except sr.RequestError as e:
                print(f"Erro na API de reconhecimento de fala: {e}")
                cria_audio("erro_api.mp3", "Erro na conexão com o serviço de reconhecimento de fala.")
            except Exception as e:
                print(f"Erro inesperado: {e}")

# Função para processar os comandos reconhecidos
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
    }

    for chave, (url, resposta) in comandos.items():
        if chave in mensagem:
            webbrowser.open(url)
            cria_audio(f"{chave}.mp3", resposta)
            return

    cria_audio("resposta.mp3", f"Você disse: {mensagem}")

# Função principal que coordena o assistente
def main():
    try:
        cria_audio("ola.mp3", "Olá, sou o Conecta, sua assistente virtual! Diga algo para começar.")
        escuta_continua()
    except Exception as e:
        print(f"Erro na execução principal: {e}")
        cria_audio("erro_execucao.mp3", "Ocorreu um erro ao iniciar o assistente.")

if __name__ == '__main__':
    main()
