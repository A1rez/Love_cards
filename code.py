import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk
import random

# Lista de mensagens
mensagens = [
    "Você é a pessoa mais incrível que eu conheço!",
    "Te amo mais do que as palavras podem expressar.",
    "Sua presença ilumina meu dia!",
    "Você é meu sol em dias nublados.",
    "Cada momento com você é um presente.",
    "Te abraço em pensamento a cada instante.",
    "Seu sorriso é a coisa mais linda que já vi.",
    "Você é meu mundo, meu tudo.",
    "Agradeço aos céus por ter você na minha vida.",
    "Você faz meu coração bater mais rápido.",
    "Meu amor por você cresce a cada dia.",
    "Você é a razão da minha felicidade.",
    "Meu amor por você é infinito.",
    "Você é minha melhor amiga e meu grande amor.",
    "Com você, tudo é mais bonito.",
    "Te amo\nTe amo\nTe amo",
    "Sou louco por você",
    "Sou completamente apaixonado por você",
]

# Caminho fixo para a imagem de fundo e a fonte
bg_image_path = "C:\\Users\\jeyso\\OneDrive\\Desktop\\coracoes-vermelhos-romantico-branco-fundo-vetor-dia-dos-namorados-copia-espaco-cartao-de-felicitacoes_55997-2110.jpg"
font_path = "C:\\Users\\jeyso\\OneDrive\\Desktop\\Stylissa.ttf"


def create_card():
    # Seleciona uma mensagem aleatória
    message = random.choice(mensagens)

    # Abre a imagem de fundo
    bg_image = Image.open(bg_image_path)

    # Define a fonte e o tamanho
    font = ImageFont.truetype(font_path, 50)

    # Cria uma instância de ImageDraw
    draw = ImageDraw.Draw(bg_image)

    # Função para dividir a mensagem em várias linhas
    def wrap_text(text, font, max_width):
        lines = []
        words = text.split()
        while words:
            line = ''
            while words and draw.textlength(line + words[0], font=font) <= max_width:
                line += (words.pop(0) + ' ')
            lines.append(line)
        return lines

    # Define a largura máxima para o texto
    max_width = bg_image.size[0] - 350  # Margem de 20 pixels de cada lado
    lines = wrap_text(message, font, max_width)

    # Calcula a altura total do texto
    text_height = sum(draw.textbbox((0, 0), line, font=font)[3] for line in lines)
    y_offset = (bg_image.size[1] - text_height) // 2  # Centraliza verticalmente

    # Desenha cada linha de texto centralizada
    for line in lines:
        text_width = draw.textlength(line, font=font)
        x_offset = (bg_image.size[0] - text_width) // 2  # Centraliza horizontalmente
        draw.text((x_offset, y_offset), line, font=font, fill="red")
        y_offset += draw.textbbox((0, 0), line, font=font)[3]

    # Exibe a imagem na tela antes de salvar
    display_image(bg_image)


def display_image(image):
    # Cria uma nova janela para exibir a imagem
    img_window = tk.Toplevel()
    img_window.title("Visualização do Cartão")

    # Converte a imagem para um formato compatível com o tkinter
    img_tk = ImageTk.PhotoImage(image)

    # Cria um rótulo para exibir a imagem
    img_label = tk.Label(img_window, image=img_tk)
    img_label.image = img_tk
    img_label.pack()

    # Função para salvar a imagem
    def save_image():
        save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                                 filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
        if save_path:
            image.save(save_path)
            messagebox.showinfo("Salvo", "Cartão de amor salvo com sucesso!")
        else:
            messagebox.showwarning("Cancelado", "Operação cancelada!")
        img_window.destroy()

    # Função para fechar a janela sem salvar
    def close_window():
        img_window.destroy()

    # Botões para decidir se deseja salvar a imagem
    button_frame = tk.Frame(img_label)
    button_frame.pack(pady=350, padx=350)
    button_frame.place(x=10, y=10)

    yes_button = tk.Button(button_frame, text="Salvar", command=save_image)
    yes_button.pack(side=tk.LEFT, padx=5)

    no_button = tk.Button(button_frame, text="Não Salvar", command=close_window)
    no_button.pack(side=tk.LEFT, padx=5)


def save_image(image):
    save_path = filedialog.asksaveasfilename(defaultextension=".png",
                                             filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
    if save_path:
        image.save(save_path)
        messagebox.showinfo("Salvo", "Cartão de amor salvo com sucesso!")
    else:
        messagebox.showwarning("Cancelado", "Operação cancelada!")


# Cria a interface gráfica
root = tk.Tk()
root.title("Gerador de Cartões de Amor")

a=tk.Button(root, text="Criar Cartão", command=create_card).pack(pady=20)




root.mainloop()
