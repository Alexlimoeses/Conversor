from bcb import currency
import matplotlib.pyplot as plt
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from tkinter import *
from tkinter import ttk
import requests


class conversor_moeda:
    def __init__(self,master):
        #Criando a janela
        self.master = master
        
        # Definindo dimensoes da janela
        master.geometry('500x400')
        self.master.title('Conversor de Moedas')

        # Criando as labels
        self.moeda_label = Label(self.master, text="Selecione a moeda:")
        self.dat = Label(self.master, text="Escolha a data para a plotagem do gráfico:")

        # Definir as opções para o ComboBox
        self.moedas = ['Dólar (USD)', 'Euro (EUR)', 'Libra (GBP)', 'Dolar canadense (CAD)']
        
        self.moedas_con = ['Dólar (USD)', 'Euro (EUR)', 'Libra (GBP)', 'Dolar canadense (CAD), Real(BRL)']
        self.moedas_con2 = ['Dólar (USD)', 'Euro (EUR)', 'Libra (GBP)', 'Dolar canadense (CAD), Real(BRL)']

        # Criar o ComboBox
        self.combo_moedas = ttk.Combobox(self.master, values=self.moedas)
        self.destin = ttk.Combobox(self.master, values=self.moedas_con, width=31)
        self.fin = ttk.Combobox(self.master, values=self.moedas_con2, width=31)

        # Definir o valor padrão
        self.combo_moedas.set('Selecione uma moeda')
        self.destin.set('Selecione a moeda a ser convertida')
        self.fin.set('Selecione a sua moeda final')

        # Criando o botão de plotar gráfico
        self.plotar_grafico_button = Button(self.master, text="Plotar Gráfico", command=self.gerar_grafico)
        self.converss = Button(self.master, text='Converter', command=self.convo)
        
        #Criar entrada para data
        self.cal = DateEntry(master, width=12, background='darkblue', foreground='white', borderwidth=2)

        # Posicionando os widgets
        self.combo_moedas.place(x=356,y=0)
        self.destin.place(x=1,y=200)
        self.fin.place(x=290,y=200)
        self.cal.place(x=1, y=0)
        self.plotar_grafico_button.place(x=200,y=22)
        self.converss.place(x=218,y=230)


 
    def gerar_grafico(self):

        data_selecionada = self.cal.get_date()
        monedas = self.combo_moedas.get()

        if monedas == "Dólar (USD)":
            
            # Define as moedas e o período de tempo
            moedas = ['USD']
            data_inicio = data_selecionada.strftime('%Y-%m-%d')
            data_fim = datetime.now().strftime('%Y-%m-%d')

            # Recupera as taxas de câmbio usando o módulo bcb.currency
            taxas = currency.get(moedas, start=data_inicio, end=data_fim)

            # Plota as taxas de câmbio em um gráfico usando o matplotlib
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(taxas.index, taxas['USD'], label='USD')
            ax.legend()
            ax.set_xlabel('Data')
            ax.set_ylabel('Taxa de câmbio')
            ax.set_title('Taxas de câmbio USD')
            plt.show()
        
        elif monedas == "Euro (EUR)":
            
            # Define as moedas e o período de tempo
            moedas = ['EUR']
            data_inicio = data_selecionada.strftime('%Y-%m-%d')
            data_fim = datetime.now().strftime('%Y-%m-%d')

            # Recupera as taxas de câmbio usando o módulo bcb.currency
            taxas = currency.get(moedas, start=data_inicio, end=data_fim)

            # Plota as taxas de câmbio em um gráfico usando o matplotlib
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(taxas.index, taxas['EUR'], label='EUR')
            ax.plot(taxas.index, taxas['EUR'], label='EUR')
            ax.legend()
            ax.set_xlabel('Data')
            ax.set_ylabel('Taxa de câmbio')
            ax.set_title('Taxas de câmbio EUR')
            plt.show()
        
        elif monedas == "Libra (GBP)":
            
            # Define as moedas e o período de tempo
            moedas = ['GBP']
            data_inicio = data_selecionada.strftime('%Y-%m-%d')
            data_fim = datetime.now().strftime('%Y-%m-%d')

            # Recupera as taxas de câmbio usando o módulo bcb.currency
            taxas = currency.get(moedas, start=data_inicio, end=data_fim)

            # Plota as taxas de câmbio em um gráfico usando o matplotlib
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(taxas.index, taxas['GBP'], label='GBP')
            ax.legend()
            ax.set_xlabel('Data')
            ax.set_ylabel('Taxa de câmbio')
            ax.set_title('Taxas de câmbio GBP')
            plt.show()

        elif monedas == "Dolar canadense (CAD)":
            
            # Define as moedas e o período de tempo
            moedas = ['CAD']
            data_inicio = data_selecionada.strftime('%Y-%m-%d')
            data_fim = datetime.now().strftime('%Y-%m-%d')

            # Recupera as taxas de câmbio usando o módulo bcb.currency
            taxas = currency.get(moedas, start=data_inicio, end=data_fim)

            # Plota as taxas de câmbio em um gráfico usando o matplotlib
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(taxas.index, taxas['CAD'], label='CAD')
            ax.legend()
            ax.set_xlabel('Data')
            ax.set_ylabel('Taxa de câmbio')
            ax.set_title('Taxas de câmbio CAD')
            plt.show()

        else:
            root = tk.Tk()
            root.title('Gráfico de Taxas de Câmbio')
            root.geometry('300x200')

            # Adiciona o seletor de data
            cal = DateEntry(root, width=12, background='darkblue', foreground='white', borderwidth=2)
            cal.pack(padx=10, pady=10)

            # Adiciona o botão para gerar o gráfico
            gerar_botao = ttk.Button(root, text="Gerar Gráfico", command=gerar_grafico)
            gerar_botao.pack(padx=10, pady=10)

            root.mainloop()
            
    def convo(self):
        self.conversao = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,JPY-BRL,USD-BRLT")
        #Pega as moedas disponíveis no site (Atualizado a cada 30 segundos) e armazena
        
        self.requisicao = self.conversao.json()
        
        self.cotacao_dolar = self.requisicao["USDBRL"]["bid"]
        self.cotacao_euro = self.requisicao["EURBRL"]["bid"]
        self.cotacao_libra = self.requisicao["GBPBRL"]["bid"]
        self.cotacao_dolcad = self.requisicao["CADBRL"]["bid"]

master = Tk()
janela = conversor_moeda(master)
master.mainloop()
