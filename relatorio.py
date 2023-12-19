
# Imports
import requests
import pandas as pd
import win32com.client as win32
import os;
from dotenv import load_dotenv
from datetime import datetime
import json

load_dotenv();

data_hoje = datetime.today().strftime("%d/%m/%Y")
email_remetente =  os.getenv("EMAIL_REMETENTE")
# Na url contém os parametros para retornar todas as transações pix  de valores pagos e recebidos de PJ e PF
response = requests.get("https://olinda.bcb.gov.br/olinda/servico/Pix_DadosAbertos/versao/v1/odata/TransacoesPixPorMunicipio(DataBase=@DataBase)?@DataBase='202311'&$top=10000&$format=json&$select=Estado,VL_PagadorPF,VL_PagadorPJ,VL_RecebedorPF,VL_RecebedorPJ")


objeto_resposta =  json.loads(response.text)
tabela_relatorio  = pd.DataFrame(objeto_resposta)
tabela_relatorio.to_excel("relatorio_pix.xlsx", index=False) # index=False não inclui o index no arquivo excel

# Função contento a logica para envio de e-mail usando o outlook do windows
def enviar_email():
    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = email_remetente
    mail.Subject = f"Relatório de estatística de pix {data_hoje}"
    mail.Body = f"""
    Prezados,

    Segue abaixo o relatório de estatística de pix do banco central {data_hoje} atualizado.
    Qualquer coisa estou à disposição
    Abs,

    Wesley Sanches;
    """
    caminho = os.getcwd();
    anexo = os.path.join(caminho, "Vendas.xlsx")
    mail.Attachments.Add(anexo)
    mail.Send();

