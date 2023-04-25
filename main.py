import pandas as pd
from bcb import currency
import matplotlib.pyplot as plt
from tkcalendar import DateEntry
from datetime import datetime, timedelta
from tkinter import *
from tkinter import ttk
import requests
from forex_python.converter import CurrencyRates
from tkinter import Tk, PhotoImage
conversor = CurrencyRates()

class conversor_moeda:
    def __init__(self,master):
        #Criando a janela
        self.master = master 
        
        # Definindo dimensoes da janela
        master.geometry('340x260+300+100')
        master.title('Conversor de Moedas')
        master.resizable(width=0, height=0)
      
        #Criado as abas
        self.notebook = ttk.Notebook(master)
        self.notebook.place(x=6, y=0, width=330, height=255)
        
        self.conv = Frame(master, bg='#00BFFF', borderwidth=2, relief='sunken')
        self.grafic = Frame(master,bg='#6A5ACB', borderwidth=2, relief='sunken')
        self.selic = Frame(master,bg='#0000FF', borderwidth=2, relief='sunken')
        
        # Adicione as abas ao notebook
        self.notebook.add(self.grafic, text='Gráfico')
        self.notebook.add(self.conv, text='Conversor')
        self.notebook.add(self.selic, text='Selic')
        
        # Criando a entradas
        self.dat = Label(self.grafic, bg='#6A5ACB',foreground='white', text="Escolha a Moeda desejada para plotagem do gráfico:")
        self.dat.place(x=0, y=80)
        
        self.label_dat = Label(self.grafic, bg='#6A5ACB',foreground='white', text="Escolha a data inicial para plotagem do gráfico de variação:")
        self.label_dat.place(x=0, y=0)
    
        self.cal = DateEntry(self.grafic, bg='#0000FF',foreground='white', width=8, background='darkblue',  borderwidth=2)
        self.cal.place(x=0, y=25)
        
        # Criando o botão de plotar gráfico
        self.plotar_grafico_button = Button(self.grafic, bg='#808080', foreground='white', text="Plotar Gráfico", command=self.gerar_grafico)
        self.plotar_grafico_button.place(x=90,y=170)
        
        # Definir as opções para o ComboBox
        self.moedas = ['Dólar (USD)', 'Euro (EUR)', 'Libra (GBP)', 'Dolar canadense (CAD)']       
        self.moedas_con = ['USD', 'EUR', 'GBP', 'CAD', 'BRL']
        self.moedas_con2 = ['USD', 'EUR', 'GBP', 'CAD', 'BRL']

        # Criar o ComboBox
        
        self.combo_moedas = ttk.Combobox(self.grafic, values=self.moedas, width=20)
        self.combo_moedas.set('Dólar (USD)')
        self.combo_moedas.place(x=0, y=105)
        
        #--------------------------------------Parte do conversor--------------------------------------
        
        # Receber o valor para converter fornecido pelo usuário
        self.labb_entr = Label(self.conv, bg='#00BFFF', foreground='black', text='Valor a ser convertido:')
        self.labb_entr.place(x=0, y=0)
        
        self.entrada_origem = Entry(self.conv, width=5)
        self.entrada_origem.place(x=0, y=23)
        
        
        self.labb = Label(self.conv, bg='#00BFFF', foreground='black', text='Selecione a moeda a ser convertida:')
        self.labb.place(x=0, y=50)
 
        self.destin = ttk.Combobox(self.conv, values=self.moedas_con, width=5)
        self.destin.set('USD')
        self.destin.place(x=0, y=73)
        
        self.labb2 = Label(self.conv, bg='#00BFFF', foreground='black', text='Selecione a moeda de destino:')
        self.labb2.place(x=0, y=110)
        
        self.fin = ttk.Combobox(self.conv, values=self.moedas_con2, width=5)
        self.fin.set('BRL')
        self.fin.place(x=0, y=133)

        # Criando o botão de conversão        
        self.converss = Button(self.conv, bg='#808080', foreground='white', text='Converter', command=self.convo)
        self.converss.place(x=100,y=170)
        
        # Criando personalização das abas         
        self.style = ttk.Style()
        self.style.configure('TNotebook.Tab', width=15, padding=(12, 6), tabposition='wn')
        
        #--------------------------------------Parte do conversor--------------------------------------
        #Adiciona o seletor de data
        self.calen = DateEntry(self.selic, width=12, background='darkblue', foreground='white', borderwidth=2)
        self.calen.pack(padx=10, pady=10)

        #Adiciona o botão para gerar o gráfico
        self.gerar_botao = Button(self.selic, text="Gerar Gráfico", command=self.gerar_graafico)
        self.gerar_botao.pack(padx=10, pady=10)

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
        valor = float(self.entrada_origem.get())
        moeda_origem = self.destin.get()
        moeda_destino = self.fin.get()
        resultado = conversor.convert(moeda_origem, moeda_destino, valor)
        texto_resultado = StringVar()
        texto_resultado.set(f'{valor:.2f} {moeda_origem} equivalem a {resultado:.2f} {moeda_destino}')
        rotulo_resultado = Label(self.conv, textvariable=texto_resultado)
        rotulo_resultado.place(x=1,y=260)
    
    def gerar_graafico(self):
        # Recupera a data selecionada do seletor de data
        self.data_selecionada = self.calen.get_date()

        #Formata a data no formato dd/mm/yyyy
        self.data_formatada = self.data_selecionada.strftime('%d/%m/%Y')

        #Carrega os dados da SELIC a partir da data selecionada até a última data disponível
        self.serie = CarregaSELIC(self.data_formatada, "28/02/2023")
        self.serie1 = self.serie.replace({',':'.'}, regex=True)
        self.serie1['valor'] = self.serie1['valor'].astype(float)
        self.serie1['data'] = pd.to_datetime(self.serie1['data'], format='%d/%m/%Y')
        self.serie1['ano_mes'] = self.serie1['data'].dt.strftime('%Y-%m')

        #Plota o gráfico da SELIC
        self.serie1.plot.line(x="ano_mes",y="valor",title="SELIC taxas ao ano",legend=False)
        plt.show()
        
def CarregaSELIC(data_inicial,data_final):
    url_bcb = f"http://api.bcb.gov.br/dados/serie/bcdata.sgs.4189/dados?formato=csv&dataInicial={data_inicial}&dataFinal={data_final}"
    serie_SELIC = pd.read_csv(url_bcb, sep=";")
    return serie_SELIC

master = Tk()
janela = conversor_moeda(master)
master.mainloop()
