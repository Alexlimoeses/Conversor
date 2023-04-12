import requests
import matplotlib.pyplot as plt
from alpha_vantage.foreignexchange import ForeignExchange
from datetime import datetime, timedelta

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
               
    def ttk(self,master):
        #Criando a janela
        self.master = master
        master.geometry('500x400')
        self.master.title('Conversor de Moedas')

        # Criando as labels
        self.moeda_label = Label(self.master, text="Selecione a moeda:")
        self.dat = Label(self.master, text="Escolha a data para a plotagem do gráfico:")

        # Criando as opções de moeda
        self.moeda_var = StringVar()
        self.moeda_var.set("USDBRL")
        self.moeda_usd = Radiobutton(self.master, text="Dólar americano (USD)", variable=self.moeda_var, value="USDBRL")
        self.moeda_eur = Radiobutton(self.master, text="Euro (EUR)", variable=self.moeda_var, value="EURBRL")
        self.moeda_btc = Radiobutton(self.master, text="Bitcoin (BTC)", variable=self.moeda_var, value="BTCBRL")
        self.moeda_jpy = Radiobutton(self.master, text="Iene japonês (JPY)", variable=self.moeda_var, value="JPYBRL")

        # Criando as entradas de data
        self.dat_var = StringVar()
        self.dat_var.set("Um dia")
        self.dat_dia = Radiobutton(self.master, text="Um dia", variable=self.dat_var, value="Um dia")
        self.dat_sem = Radiobutton(self.master, text="Uma semana", variable=self.dat_var, value="Uma semana")
        self.dat_mes = Radiobutton(self.master, text="Um mês", variable=self.dat_var, value="Um mês")
        self.dat_ano = Radiobutton(self.master, text="Um ano", variable=self.dat_var, value="Um ano")
        

        # Criando o botão de plotar gráfico
        self.plotar_grafico_button = Button(self.master, text="Plotar Gráfico", command=self.graff)

        # Posicionando os widgets
        self.moeda_label.grid(row=0, column=0)
        self.moeda_usd.grid(row=1, column=0)
        self.moeda_eur.grid(row=2, column=0)
        self.moeda_btc.grid(row=3, column=0)
        self.moeda_jpy.grid(row=4, column=0)

        self.dat.grid(row=0, column=1)
        self.dat_dia.grid(row=1, column=1)
        self.dat_sem.grid(row=2, column=1)
        self.dat_mes.grid(row=3, column=1)
        self.dat_ano.grid(row=4, column=1)

        self.plotar_grafico_button.grid(row=5, column=1)
        


    def graff(self):
        self.api_key = 'SUA_CHAVE_API'
        self.fx = ForeignExchange(key=self.api_key)
        
        try:
        # Defina a chave da API da Alpha Vantage

            if self.dat_var == "Um dia":
                
                self.end_date = datetime.now().strftime('%Y-%m-%d')
                self.start_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
                        
                if self.moeda_var == "USDBRL":
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='USD', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                    
                    # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show() 
                
                elif self.moeda_var == "EURBRL":
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='EUR', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                    # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show() 
                    
                elif self.moeda_var == "BTCBRL":
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='BTC', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                    # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show() 

                else:
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='JPY', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                    # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show()

            elif self.dat_var == "Uma semana":
                self.end_date = datetime.now().strftime('%Y-%m-%d')
                self.start_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
                
                if self.moeda_var == "USDBRL":
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='USD', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                    
                    # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show() 
                
                elif self.moeda_var == "EURBRL":
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='EUR', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                    # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show() 
                    
                elif self.moeda_var == "BTCBRL":
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='BTC', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                    # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show() 
    
                else:
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='JPY', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                                # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show()
            
            elif self.dat_var == "Um mês":
                self.end_date = datetime.now().strftime('%Y-%m-%d')
                self.start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
                
                if self.moeda_var == "USDBRL":
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='USD', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                    
                    # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show() 
                
                elif self.moeda_var == "EURBRL":
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='EUR', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                    # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show() 

                elif self.moeda_var == "BTCBRL":
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='BTC', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                    # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show() 

                
                else:
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='JPY', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                                # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show()
                
            else:
                self.end_date = datetime.now().strftime('%Y-%m-%d')
                self.start_date = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

                if self.moeda_var == "USDBRL":
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='USD', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                    
                    # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show() 
                
                elif self.moeda_var == "EURBRL":
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='EUR', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                    # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show() 
                    
                elif self.moeda_var == "BTCBRL":
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='BTC', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                    # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show() 

                else:
                    self.data, _ = self.fx.get_currency_exchange_daily(from_symbol='JPY', to_symbol='BRL', outputsize='full')
                    self.data = pd.DataFrame.from_dict(self.data, orient='index').sort_index()
                    self.data = self.data.loc[self.start_date:self.end_date]
                                # Calcule a taxa de variação diária da moeda
                    self.daily_returns = self.data['4. close'].astype(float).pct_change()

                    # Plote o gráfico da taxa de variação diária
                    plt.plot(self.daily_returns.index, self.daily_returns)
                    plt.title(f'Taxa de variação diária de {self.moeda_var} em {self.dat_var}')
                    plt.xlabel('Data')
                    plt.ylabel('Taxa de variação diária')
                
                    # Remove o eixo x
                    plt.gca().axes.xaxis.set_visible(False)
                
                    plt.show()
        except:
            print('erro')          
    
        
master = Tk()
janela = conversor_moeda()
janela.ttk(master)
master.mainloop()
