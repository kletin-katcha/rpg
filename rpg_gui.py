import subprocess
import threading
import queue
import tkinter as tk
from tkinter import scrolledtext

class RPGGui:
    def __init__(self, root):
        self.root = root
        self.root.title("RPG - Interface Gráfica")
        self.root.geometry("800x500")
        self.root.configure(bg="black")  # fundo preto

        # Título completo estiloso
        self.titulo = tk.Label(
            root,
            text="Crônicas de Aethelgard: A Sombra do Rei Demônio",
            font=("Algerian", 24, "bold"),  # fonte elegante
            fg="blue",  # título azul
            bg="black"
        )
        self.titulo.pack(pady=(15, 10))

        # Caixa de texto com rolagem
        self.output = scrolledtext.ScrolledText(
            root,
            wrap="word",
            font=("Consolas", 11),
            state="disabled",
            bg="black",
            fg="white"
        )
        self.output.pack(fill="both", expand=True, padx=8, pady=(0, 0))

        # Definição de tags (cores do texto)
        self.output.tag_config("opcao", foreground="cyan")  # azul para opções

        # Entrada para digitar comandos
        self.entry = tk.Entry(root, font=("Consolas", 11), bg="gray20", fg="white", insertbackground="white")
        self.entry.pack(fill="x", padx=8, pady=8)
        self.entry.bind("<Return>", self.send_input)

        self.q = queue.Queue()
        self.proc = None
        self.start_process()

        # checa a saída continuamente
        self.root.after(100, self.check_output)

    def start_process(self):
        self.proc = subprocess.Popen(
            ["python", "rpg.py"],  # roda seu jogo
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1
        )

        threading.Thread(target=self.read_output, daemon=True).start()

    def read_output(self):
        for line in self.proc.stdout:
            self.q.put(line)

    def check_output(self):
        while not self.q.empty():
            line = self.q.get_nowait()
            self.output.configure(state="normal")

            # Se a linha parece ser opção (1), 2), etc.), mostra em azul
            if line.strip().startswith(("1", "2", "3", "4", "5")):
                self.output.insert("end", line, "opcao")
            else:
                self.output.insert("end", line)

            self.output.see("end")
            self.output.configure(state="disabled")
        self.root.after(100, self.check_output)

    def send_input(self, event=None):
        text = self.entry.get()
        self.entry.delete(0, tk.END)
        if self.proc and self.proc.stdin:
            self.proc.stdin.write(text + "\n")
            self.proc.stdin.flush()

if __name__ == "__main__":
    root = tk.Tk()
    RPGGui(root)
    root.mainloop()


