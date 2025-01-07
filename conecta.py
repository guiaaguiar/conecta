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

# Função otimizada para capturar e reconhecer áudio do microfone
def ouvir_microfone(timeout=5, phrase_time_limit=7):
    """
    Captura e reconhece o áudio do microfone com alta precisão e rapidez.

    Args:
        timeout (int): Tempo máximo para o microfone aguardar o início da fala.
        phrase_time_limit (int): Tempo máximo permitido para o usuário falar.

    Returns:
        str: Transcrição da fala do usuário (em minúsculas).
        None: Caso o reconhecimento falhe ou o tempo limite seja excedido.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        # Ajusta o microfone ao ruído do ambiente
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Estou ouvindo... Pode falar.")
        try:
            # Captura o áudio
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            # Transcreve o áudio usando a API Google
            transcricao = recognizer.recognize_google(audio, language="pt-BR").lower()
            print(f"Transcrição: {transcricao}")
            return transcricao
        except sr.UnknownValueError:
            print("Não entendi o que foi dito.")
            return None
        except sr.WaitTimeoutError:
            print("Tempo de espera excedido. Nenhum som detectado.")
            return None
        except sr.RequestError as e:
            print(f"Erro na API de reconhecimento de fala: {e}")
            return None

# Função para escutar e reconhecer o que você fala
def monitora_audio():
    while True:
        print('Diga "Conecta" para ativar ou "desligar" para desativar...')
        mensagem = ouvir_microfone()
        if mensagem:
            if "conecta" in mensagem:  # Ativa o assistente
                cria_audio("conecta.mp3", "Estou te ouvindo. Como posso ajudar?")
                executa_comandos()
            elif "desligar" in mensagem:  # Desliga o assistente
                cria_audio("desligar.mp3", "Assistente desligado.")
                break

# Função para executar comandos quando o assistente estiver ativado
def executa_comandos():
    # Dicionário com palavras-chave e respectivos links
    comandos = {
        'coreto': ("http://coreto.recife.pe.gov.br", "Aqui está o que encontrei sobre Coreto."),
        'conecta recife': ("http://conecta.recife.pe.gov.br", "Aqui está o que encontrei sobre Conecta Recife."),
        'conectar recife': ("http://conecta.recife.pe.gov.br", "Aqui está o que encontrei sobre Conecta Recife."),
        'go recife': ("http://gorecife.pe.gov.br", "Aqui está o que encontrei sobre o Go Recife."),
        'gol recife': ("http://gorecife.pe.gov.br", "Aqui está o que encontrei sobre o Go Recife."),
        'edit ai': ("http://editai.recife.pe.gov.br", "Aqui está o que encontrei sobre o Edit Ai."),
        'edit aí': ("http://editai.recife.pe.gov.br", "Aqui está o que encontrei sobre o Edit Ai."),
        'edite aí': ("http://editai.recife.pe.gov.br", "Aqui está o que encontrei sobre o Edit Ai."),
        'edite ai': ("http://editai.recife.pe.gov.br", "Aqui está o que encontrei sobre o Edit Ai."),
        'edith aí': ("http://editai.recife.pe.gov.br", "Aqui está o que encontrei sobre o Edit Ai."),
        'edith ai': ("http://editai.recife.pe.gov.br", "Aqui está o que encontrei sobre o Edit Ai."),
    }
    
    while True:
        print("Comando ativado. Diga algo ou 'desligar' para parar.")
        mensagem = ouvir_microfone()
        if mensagem:
            for chave, (url, resposta) in comandos.items():
                if chave in mensagem:
                    webbrowser.open(url)
                    cria_audio(f"{chave}.mp3", resposta)
                    break
            else:
                if 'desligar' in mensagem:
                    cria_audio("desligar.mp3", "Assistente desligado.")
                    break  # Sai do loop e desliga o assistente
                else:
                    cria_audio("resposta.mp3", f"Você disse: {mensagem}")

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
