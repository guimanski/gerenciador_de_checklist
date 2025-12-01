from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def confirmar_conclusao():
    resposta = messagebox.askyesno(
        title='Confirmar a conclusão do Checklist',
        message='Tem certeza que deseja concluir o checklist?'
    )
    if resposta == 'Sim':
        pass
    else:
        return



janela = Tk()
janela.title('Checklist')
frm = ttk.Frame(janela, padding=10)

# Rota
texto_rota = ttk.Label(janela, text='Rota: ', padding=10)
texto_rota.grid(row=0, column=0, sticky='W')

insert_doca = ttk.Entry(janela, width=10)
insert_doca.grid(row=0, column=1)

# Doca
texto_doca = ttk.Label(janela, text='Doca: ', padding=10)
texto_doca.grid(row=0, column=2, sticky='W')

insert_doca = ttk.Entry(janela, width=10)
insert_doca.grid(row=0, column=3)

# Janela Bells
texto_janela_bells = ttk.Label(janela, text='Janela Bells: ', padding=10)
texto_janela_bells.grid(row=1, column=0, sticky='W')

insert_janela_bells = ttk.Entry(janela, width=10)
insert_janela_bells.grid(row=1, column=1)

# Janela Diário
texto_janela_diario = ttk.Label(janela, text='Janela Diário: ', padding=10)
texto_janela_diario.grid(row=1, column=2, sticky='W')

insert_janela_diario = ttk.Entry(janela, width=10)
insert_janela_diario.grid(row=1, column=3)


# Hora de chegada
texto_hora_chegada = ttk.Label(janela, text='Hora de chegada: ', padding=10)
texto_hora_chegada.grid(row=2, column=0, sticky='W')

insert_hora_chegada = ttk.Entry(janela, width=10)
insert_hora_chegada.grid(row=2, column=1)

# Hora de Saída
texto_hora_saida = ttk.Label(janela, text='Hora de saída: ', padding=10)
texto_hora_saida.grid(row=2, column=2, sticky='W')

insert_hora_saida = ttk.Entry(janela, width=10)
insert_hora_saida.grid(row=2, column=3)

# Cliente
texto_cliente = ttk.Label(janela, text='Cliente: ', padding=10)
texto_cliente.grid(row=3, column=0, sticky='W')

insert_cliente = ttk.Entry(janela, width=10)
insert_cliente.grid(row=3, column=1)

# Transportadora
texto_transportadora = ttk.Label(janela, text='Transportadora: ', padding=10)
texto_transportadora.grid(row=3, column=2, sticky='W')

insert_transportadora = ttk.Entry(janela, width=10)
insert_transportadora.grid(row=3, column=3, padx=10)

# Data
texto_data = ttk.Label(janela, text='Data: ', padding=10)
texto_data.grid(row=4, column=0, sticky='W')

insert_data = ttk.Entry(janela, width=10)
insert_data.grid(row=4, column=1, padx=10)

# Conferente
texto_conferente = ttk.Label(janela, text='Conferente: ', padding=10)
texto_conferente.grid(row=4, column=2, sticky='W')

insert_conferente = ttk.Entry(janela, width=10)
insert_conferente.grid(row=4, column=3, padx=10)


### Botões
btn_concluir = ttk.Button(janela,
                          text='Concluir',
                          padding=5,
                          command=confirmar_conclusao)
btn_concluir.grid(row=5, column=2, pady=30)

btn_cancelar = ttk.Button(janela, text='Cancelar', padding=5)
btn_cancelar.grid(row=5, column=3, padx=15, pady=30)



janela.mainloop()