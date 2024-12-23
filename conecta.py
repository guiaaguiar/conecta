import speech_recognition as sr
import pyttsx3
import tkinter as tk
import threading
import queue

# Inicializa o sintetizador de fala e fila para mensagens
engine = pyttsx3.init()
fila_fala = queue.Queue()

# Variável de controle
assistente_ativo = False

# Função para falar (não bloqueante)
def falar(mensagem):
    engine.say(mensagem)
    engine.runAndWait()

# Função de escuta contínua
def ouvir_microfone(timeout=10):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        try:
            audio = recognizer.listen(source, timeout=timeout)
            return recognizer.recognize_google(audio, language="pt-BR").lower()
        except (sr.UnknownValueError, sr.WaitTimeoutError):
            return None

# Processa o comando de voz ou texto
def processar_comando(comando):
    comando = comando.strip().lower()
    if "desligar" in comando:
        return "Desligando o sistema."
    if "conecta" in comando:
        return "Olá, sou Conecta, seu assistente virtual. Pode falar."
    return comando  # Repete o comando

# Função para desenhar balões de fala com cantos arredondados
def desenhar_balao(canvas, texto, lado, y_pos):
    padding = 10  # Margem interna do balão
    largura = 200  # Largura do balão
    balao_height = 40 + (texto.count('\n') * 20)  # Ajuste do tamanho do balão para várias linhas

    # Ajuste da posição e cor do balão dependendo do lado
    if lado == 'esquerda':
        x1, x2 = 10, largura
    else:
        x1, x2 = largura - 10, largura + 140
    
    # Desenha o retângulo com bordas arredondadas
    create_rounded_rect(canvas, x1, y_pos, x2, y_pos + balao_height, 20, fill="#cce5ff", outline="#a0c4ff", width=1)
    canvas.create_text(x1 + padding, y_pos + padding, text=texto, anchor="w", font=("Arial", 12), fill="#000")

# Função para criar um retângulo com bordas arredondadas
def create_rounded_rect(canvas, x1, y1, x2, y2, r, **kwargs):
    points = [
        x1 + r, y1, x2 - r, y1,  # Linha superior
        x2, y1, x2, y2 - r,  # Linha direita
        x2, y2, x1 + r, y2,  # Linha inferior
        x1, y2, x1, y1 + r  # Linha esquerda
    ]
    return canvas.create_polygon(points, smooth=True, **kwargs)

# Função para exibir resposta e atualizar o chat
def exibir_resposta(remetente, mensagem):
    global y_pos
    # Calcula a posição y para o balão
    y_pos += 80

    if remetente == "Conecta":
        lado = "esquerda"
    else:
        lado = "direita"

    desenhar_balao(canvas, mensagem, lado, y_pos)

    fila_fala.put(mensagem)

# Função para escutar e processar comandos
def escutar_continuamente():
    global assistente_ativo
    while True:
        comando = ouvir_microfone()
        if comando:
            if "conecta" in comando:
                assistente_ativo = True
                exibir_resposta("Conecta", "Olá, sou Conecta, seu assistente virtual. Pode falar.")
            elif assistente_ativo:
                resposta = processar_comando(comando)
                exibir_resposta("Conecta", resposta)
                if "desligar" in comando:
                    assistente_ativo = False
                    exibir_resposta("Conecta", "Sistema desligado. Voltando a escutar.")
                    exibir_resposta("Conecta", "Diga 'Conecta' para começar.")
        else:
            continue

# Função para enviar comando via digitação
def enviar_comando():
    comando = entrada.get().strip()
    entrada.delete(0, tk.END)
    if comando:
        exibir_resposta("Você", comando)
        exibir_resposta("Conecta", processar_comando(comando))

# Função para iniciar a escuta sem bloquear a interface
def iniciar_assistente():
    threading.Thread(target=falar_na_fila, daemon=True).start()

# Função para falar as mensagens da fila
def falar_na_fila():
    while True:
        if not fila_fala.empty():
            mensagem = fila_fala.get()
            falar(mensagem)

# Configuração da interface gráfica
root = tk.Tk()
root.title("Conecta - Assistente Virtual")
root.geometry("500x600")
root.config(bg="#f8f9fa")

# Criar o chat com o canvas
chat_frame = tk.Frame(root, bg="#f8f9fa")
chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

canvas = tk.Canvas(chat_frame, bg="#f8f9fa", height=500)
canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entrada de texto com estilo
entrada_frame = tk.Frame(root, bg="#f8f9fa")
entrada_frame.pack(padx=10, pady=5, fill=tk.X)

entrada = tk.Entry(entrada_frame, width=40, font=("Arial", 12))
entrada.pack(side=tk.LEFT, padx=5, pady=5, fill=tk.X, expand=True)

botao_enviar = tk.Button(entrada_frame, text="Enviar", command=enviar_comando, font=("Arial", 12), bg="#007bff", fg="white", relief="flat")
botao_enviar.pack(side=tk.RIGHT, padx=5, pady=5)

# Variável para controlar a posição dos balões de fala
y_pos = 20

# Mensagem inicial
root.after(1000, lambda: exibir_resposta("Conecta", "Diga 'Conecta' para começar ou 'Desligar' para encerrar."))

# Inicia a escuta contínua
threading.Thread(target=escutar_continuamente, daemon=True).start()

# Inicia a interface
iniciar_assistente()
root.mainloop()
