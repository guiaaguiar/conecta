# Conecta - Assistente Virtual da Prefeitura do Recife

**Conecta** é um assistente virtual desenvolvido para auxiliar os cidadãos de Recife, oferecendo informações rápidas e acessíveis sobre serviços municipais e outras consultas gerais. Ele utiliza reconhecimento de fala, síntese de voz e integração com o ChatGPT para criar uma interação amigável e eficiente.

---

## Funcionalidades

- **Reconhecimento de fala em tempo real**: Identifica e interpreta comandos de voz em português.
- **Execução de comandos específicos**: Acesso a serviços como Coreto, Conecta Recife, Edit Ai, e outros portais relevantes.
- **Respostas dinâmicas**: Consulta o ChatGPT para responder perguntas gerais.
- **Sintetização de voz**: Responde ao usuário com mensagens audíveis em português.
- **Desligamento por comando de voz**: O assistente pode ser encerrado ao ouvir o comando "desligar".

---

## Como Funciona

1. **Reconhecimento de Fala**: O assistente escuta comandos usando a biblioteca `SpeechRecognition`.
2. **Processamento de Comandos**: Identifica comandos específicos e realiza ações predefinidas, como abrir sites ou gerar respostas.
3. **Consulta ao ChatGPT**: Para perguntas não relacionadas a comandos, o assistente interage com a API do OpenAI.
4. **Resposta Audível**: A resposta é sintetizada em áudio utilizando a biblioteca `gTTS` e reproduzida via `pygame`.

---

## Tecnologias Utilizadas

- **Linguagem**: Python
- **Bibliotecas**:
  - [SpeechRecognition](https://pypi.org/project/SpeechRecognition/): Reconhecimento de fala.
  - [gTTS](https://pypi.org/project/gTTS/): Geração de áudio para respostas.
  - [Pygame](https://www.pygame.org/): Reprodução de áudio.
  - [OpenAI API](https://platform.openai.com/): Integração com ChatGPT.
  - [Webbrowser](https://docs.python.org/3/library/webbrowser.html): Navegação web.

---

## Como Executar o Projeto

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/seu-usuario/conecta-assistente.git
   cd conecta-assistente

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

4. Execute o assistente:
   ```bash
   python conecta.py
   ```

## Arquivo `requirements.txt`

As dependências do projeto estão listadas no arquivo `requirements.txt`:
```
SpeechRecognition==3.12.0
pygame==2.6.1
gTTS==2.5.4
openai==0.28.0
```
