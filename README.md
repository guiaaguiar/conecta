# Conecta - Assistente Virtual

O **Conecta** é um assistente virtual desenvolvido em Python que permite interação por comandos de voz. O assistente responde a comandos como "conecta recife", "coreto", "go recife" e outros, abrindo sites de interesse e fornecendo informações relevantes.

## Funcionalidades

- **Comandos de voz**: O assistente é ativado por voz com o comando "Conecta" e responde a uma série de palavras-chave.
- **Respostas em áudio**: O assistente converte suas respostas em áudio utilizando a API do Google Text-to-Speech (gTTS).
- **Abertura de sites**: O assistente pode abrir URLs diretamente no navegador padrão.
- **Tratamento de exceções**: O sistema trata erros como falhas de conexão com o serviço de reconhecimento de fala ou problemas de áudio.

## Instalação

Para instalar o projeto, siga as instruções abaixo:

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/conecta.git

2. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt

3. Execute o programa:

      ```bash
   python conecta.py
    
## Dependências

- `speech_recognition`: Para reconhecimento de voz.
- `pygame`: Para tocar arquivos de áudio.
- `gTTS`: Para conversão de texto para fala.
- `webbrowser`: Para abrir URLs no navegador.

## Como Funciona

1. O assistente ouve continuamente em busca do comando de ativação ("Conecta").
2. Quando ativado, o assistente espera por novos comandos.
3. Ao reconhecer um comando, o assistente executa a ação associada (abrir sites, responder com uma mensagem, etc.).
4. O assistente pode ser desligado a qualquer momento com o comando "desligar".

## Exemplo de Comandos

- **"Conecta Recife"**: Abre o site Conecta Recife.
- **"Go Recife"**: Abre o site Go Recife.
- **"Coreto"**: Abre o site Coreto Recife.
- **"Edit Ai"**: Abre o site Edit Ai.
