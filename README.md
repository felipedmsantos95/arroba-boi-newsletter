# Newsletter do Boi Gordo 🐃 🐂 🐄

## Sobre

Às vezes eu acabo passando do horário de acordar pra assistir o Globo Rural, ficar por dentro da cotação do Arroba do Boi Gordo e saber se está na hora de fazer aquele investimento maroto em umas cabeças de gado. Então fiz essa automação em Python para enviar a cotação do arroba do boi gordo para mim e possíveis inscritos via email.

## Requisitos

-   [Python 3.6](https://www.python.org/) ou superior

## Executando o projeto

### Clonando o projeto

```bash
$ git clone https://github.com/felipedmsantos95/arroba-boi-newsletter
$ cd arroba-boi-newsletter

```
Após isso devemos instalar as dependêcias do projeto, pode ser feito de duas formas

#### Instalando dependências no ambiente virtual Python (Recomendado)

É necessário ter instalado o pacote `virtualenv` no sistema, que pode ser obtido pelo comando seguinte:

```bash
$ sudo pip3 install virtualenv
```
Feito isso, dentro do diretório do projeto, podemos executar o seguinte: 

```bash
$ virtualenv --python='/usr/bin/python3' whatsapp-bot-venv
$ source whatsapp-bot-venv/bin/activate
(whatsapp-bot-venv) $ pip3 install http smtplib ssl socketserver decouple datetime email pynliner pandas requests bs4
```
NOTA: para verificar o diretório correto do Python 3 em seu sistema, pode-se executar `which python3`


#### Instalando dependências diretamente no sistema

```bash
$ pip3 install http smtplib ssl socketserver decouple datetime email pynliner pandas requests bs4
```

### Configurando .env para destinatários e remetentes do email


### Executando os scripts