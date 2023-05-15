import tkinter as tk
from PIL import ImageTk, Image

def fazer_login():
    email = entry_email.get()
    senha = entry_senha.get()
    
    # Aqui você pode adicionar a lógica para verificar as credenciais
    # e realizar a ação apropriada, como exibir uma mensagem de sucesso ou erro.

# Cria a janela principal
janela = tk.Tk()
janela.title("Tela de Login")

# Define o tamanho da janela
largura_janela = 800
altura_janela = 400
janela.geometry(f"{largura_janela}x{altura_janela}")

# Configura o background
janela.configure(bg="#023047")

# Divide a janela em duas colunas
coluna1 = tk.Frame(janela, width=largura_janela // 2, height=altura_janela, bg="#023047")
coluna2 = tk.Frame(janela, width=largura_janela // 2, height=altura_janela)

coluna1.pack(side=tk.LEFT, fill=tk.BOTH)
coluna2.pack(side=tk.RIGHT, fill=tk.BOTH)

# Cria os campos de entrada e o botão
frame_centralizado = tk.Frame(coluna1, bg="#023047")
frame_centralizado.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

label_email = tk.Label(frame_centralizado, text="Email:", bg="#023047", fg="#FFFFFF")
label_email.pack(pady=10)
entry_email = tk.Entry(frame_centralizado)
entry_email.pack(pady=5)

label_senha = tk.Label(frame_centralizado, text="Senha:", bg="#023047", fg="#FFFFFF")
label_senha.pack(pady=10)
entry_senha = tk.Entry(frame_centralizado, show="*")
entry_senha.pack(pady=5)

botao_entrar = tk.Button(frame_centralizado, text="Entrar", command=fazer_login, bg="#45C4B0", fg="#FFFFFF")
botao_entrar.pack(pady=10)

# Carrega a imagem
imagem = Image.open("imgs/img1.png")
largura_imagem = largura_janela // 2
altura_imagem = altura_janela
imagem = imagem.resize((largura_imagem, altura_imagem), Image.ANTIALIAS)
imagem = ImageTk.PhotoImage(imagem)

# Cria um rótulo para exibir a imagem
rotulo_imagem = tk.Label(coluna2, image=imagem)
rotulo_imagem.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)

# Inicia a execução da janela
janela.mainloop()
