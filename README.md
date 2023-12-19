# COLETA BANCO DE DADOS ABERTO DE ESTATÍSTICA DE PIX DO BANCO CENTRAL POR ESTADO
Para criar a aplicação foi relizado um get na url da api do banco central de dados abertos de estatística de pix onde como parametro foi passado para listar todos os estados passando como parametro direto na url os parametros da busca como data, tipo de busca e parametros para retorno da pesquisa.

Objetivo final é pegar a resposta desta chamada e transformar em um arquivo xlsx"Excel" e enviar um relatório por email utilizando o outlook máquina local. No arquivo deve conter os Estados
Quantidade Pagador PF | Quantidade pagador PJ | Quantidade recebedor PF | quantidade recebedor PJ
