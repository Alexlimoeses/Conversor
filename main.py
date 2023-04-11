import requests
import matplotlib.pyplot as plt
from alpha_vantage.foreignexchange import ForeignExchange
from datetime import datetime, timedelta
import pandas as pd
from tkinter import *


class conversor_moeda:
    def _init_(self):
        self.conversao = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL,JPY-BRL,USD-BRLT")
        #Pega as moedas disponíveis no site (Atualizado a cada 30 segundos) e armazena
        
        self.requisicao = self.conversao.json()
        
        self.cotacao_dolar = self.requisicao["USDBRL"]["bid"]
        self.cotacao_euro = self.requisicao["EURBRL"]["bid"]
        self.cotacao_bitc = self.requisicao["BTCBRL"]["bid"]
        self.cotacao_yene = self.requisicao["JPYBRL"]["bid"]
        self.cotacao_dolartur = self.requisicao["USDBRLT"]["bid"]
        #Armazena cada moeda em sua devida variavel
        
        
    def graff(self):
        # Defina a chave da API da Alpha Vantage
        self.api_key = 'SUA_CHAVE_API'

        # Defina o símbolo da moeda que você deseja obter os dados
        self.symbol = 'USDBRL'

        # Defina a data de um mês atrás e a data atual
        self.end_date = datetime.now().strftime('%Y-%m-%d')
        self.start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        

        # Obtenha os dados históricos da moeda usando a API da Alpha Vantage
        self.fx = ForeignExchange(key=self.api_key)
        self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='USD', to_symbol='BRL', outputsize='full')
        self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
        self.data = self.data.loc[self.start_date:self.end_date]

        # Calcule a taxa de variação diária da moeda
        self.daily_returns = self.data['4. close'].astype(float).pct_change()

        # Plote o gráfico da taxa de variação diária
        plt.plot(self.daily_returns.index, self.daily_returns)
        plt.title(f'Taxa de variação diária de {self.symbol} em um mês')
        plt.xlabel('Data')
        plt.ylabel('Taxa de variação diária')
        
        # Remove o eixo x
        plt.gca().axes.xaxis.set_visible(False)
        
        plt.show()       
        
    def ttk(self,master):
        
        self.master = master
        master.geometry('500x400')
        self.master.title('Conversor de Moedas')

        # Criando as labels
        self.moeda_label = Label(self.master, text="Selecione a moeda:")
        self.data_inicio_label = Label(self.master, text="Data inicial:")
        self.data_fim_label = Label(self.master, text="Data final:")

        # Criando as opções de moeda
        self.moeda_var = StringVar()
        self.moeda_var.set("USD")
        self.moeda_usd = Radiobutton(self.master, text="Dólar americano (USD)", variable=self.moeda_var, value="USD")
        self.moeda_eur = Radiobutton(self.master, text="Euro (EUR)", variable=self.moeda_var, value="EUR")
        self.moeda_btc = Radiobutton(self.master, text="Bitcoin (BTC)", variable=self.moeda_var, value="BTC")
        self.moeda_jpy = Radiobutton(self.master, text="Iene japonês (JPY)", variable=self.moeda_var, value="JPY")

        # Criando as entradas de data
        self.data_inicio_entry = Entry(self.master)
        self.data_inicio_entry.insert(END, (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d'))
        self.data_fim_entry = Entry(self.master)
        self.data_fim_entry.insert(END, datetime.now().strftime('%Y-%m-%d'))

        # Criando o botão de plotar gráfico
        self.plotar_grafico_button = Button(self.master, text="Plotar Gráfico", command=self.graff)

        # Posicionando os widgets
        self.moeda_label.grid(row=0, column=0)
        self.moeda_usd.grid(row=1, column=0)
        self.moeda_eur.grid(row=2, column=0)
        self.moeda_btc.grid(row=3, column=0)
        self.moeda_jpy.grid(row=4, column=0)

        self.data_inicio_label.grid(row=0, column=1)
        self.data_inicio_entry.grid(row=1, column=1)
        self.data_fim_label.grid(row=2, column=1)
        self.data_fim_entry.grid(row=3, column=1)

        self.plotar_grafico_button.grid(row=4, column=1)
        
master = Tk()
janela = conversor_moeda()
janela.ttk(master)
master.mainloop()
