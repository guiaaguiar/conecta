# Conecta - Assistente Virtual

Conecta é uma assistente virtual desenvolvida para ouvir comandos de voz, processá-los e executar ações como abrir páginas da web ou responder com mensagens de áudio. Este projeto utiliza Python e bibliotecas como `speech_recognition`, `pygame` e `gTTS` para oferecer uma experiência interativa ao usuário.

## Funcionalidades

1. **Reconhecimento de Fala**:
   - Escuta comandos de voz continuamente e reconhece palavras-chave.
   - Suporte para a linguagem portuguesa (pt-BR).

2. **Respostas em Áudio**:
   - Gera respostas em áudio utilizando a biblioteca `gTTS`.

3. **Execução de Comandos**:
   - Abre páginas da web com base em palavras-chave específicas.

4. **Desligamento por Comando**:
   - Desativa o assistente ao detectar o comando "desligar".

## Pré-requisitos

Antes de executar o projeto, certifique-se de ter o Python instalado em sua máquina. É recomendável usar um ambiente virtual para gerenciar as dependências.

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie um ambiente virtual e ative-o:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/MacOS
   venv\Scripts\activate   # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

## Uso

1. Execute o programa:
   ```bash
   python conecta.py
   ```

2. O assistente irá saudar você e começará a escutar comandos. Exemplos de comandos suportados:
   - "Coreto"
   - "Conecta Recife"
   - "Go Recife"
   - "Desligar" (para encerrar o assistente)

3. Caso um comando válido seja reconhecido, a página correspondente será aberta no navegador e uma resposta será gerada em áudio.

## Personalização

Você pode adicionar mais comandos personalizando o dicionário na função `processa_comando` no arquivo `conecta.py`:
```python
comandos = {
    'novo comando': ("http://link.com", "Mensagem de resposta."),
}
```

## Arquivo `requirements.txt`

As dependências do projeto estão listadas no arquivo `requirements.txt`:
```
gTTS==2.2.3
pygame==2.1.2
SpeechRecognition==3.8.1
```
