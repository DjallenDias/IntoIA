import time
import tkinter as tk
from tkinter import ttk

import classes

class Busca8PuzzleApp:
    def __init__(self, root, resultados):
        self.root = root
        self.resultados = resultados
        self.root.title("Jogo 8 Puzzle")
        
        # Configura a tela com valores padrão
        self.label = ttk.Label(root, text="Resultados da Busca:")
        self.label.pack()
        
        self.resultados_frame = ttk.Frame(root)
        self.resultados_frame.pack()
        
        # Botão para iniciar a visualização dos resultados
        self.visualizar_button = ttk.Button(root, text="Visualizar Resultados", command=self.visualizar_resultados)
        self.visualizar_button.pack()
    
    def visualizar_resultados(self):
        for resultado in self.resultados:
            self.atualizar_tela(resultado)
            self.root.update()  # Atualiza a tela
            time.sleep(1.25)  # Pausa para visualização
    
    def atualizar_tela(self, matriz):
        # Remove os widgets antigos
        for widget in self.resultados_frame.winfo_children():
            widget.destroy()
        
        # Exibe a nova matriz em uma grade 3x3
        for i, linha in enumerate(matriz):
            for j, valor in enumerate(linha):
                valor_label = ttk.Label(self.resultados_frame, text=str(valor), relief="solid", width=4, font=("Helvetica", 28), anchor="center")
                valor_label.grid(row=i, column=j, padx=10, pady=10)
        

estado = [
    [1,2,3],
    [4,5,0],
    [6,7,8],
]

estado_objetivo = [
    [1,2,3],
    [4,5,6],
    [7,8,0],
]

no = classes.No(estado, None, None, None)
problema = classes.Problema(no, lambda no: no.estado == estado_objetivo)
buscaL = classes.BuscaLargura(problema)
buscaL.executar()

if buscaL.situacao == classes.BUSCA_FALHOU:
    exit() # encerra o programa caso a busca tenha falho

sol = buscaL.solucao

sol_matrizes = []

for s in sol:
    sol_matrizes.append(s.estado)

root = tk.Tk()
app = Busca8PuzzleApp(root, sol_matrizes)
root.mainloop()