#!/usr/bin/env python
# coding: utf-8

# Esse script foi desenvolvido para facilitar o envio de e-mails às listas
# brasileiras de Python e é utilizado pela APyB para enviar convites aos
# eventos da comunidade, notificações etc.
# Obviamente, o e-mail do remetente precisa ser cadastrado nas listas para
# enviar e-mails a elas (a maioria fica no Google Groups).
# Em alguns casos (como no caso da PyBr[8]), o remetente utilizado foi
# <organizacao@python.org.br>; já em outros e-mails pessoais são utilizados por
# quem quer fazer a notificação.

# Author: Álvaro Justen aka Turicas <http://turicas.info/>
# Licença: GPLv3

import getpass
import smtplib
import sys
import time


remetente = '"Seu nome" <seu@email.com>'
msg = '''Subject: Assunto do e-mail
From: %s
To: {email}

Aqui vai a sua mensagem...
Você pode substituir com os "campos" de cada entrada na lista de e-mails.
Por exemplo: {gentilico}

Atenciosamente,
    Diretoria da Associação Python Brasil''' % remetente


class EmailConnection(object):
    def __init__(self, host, port, username, password):
        self.username = username
        self.password = password
        self.host = host
        self.port = port

    def connect(self):
        self.connection = smtplib.SMTP(self.host, self.port)
        self.connection.ehlo()
        self.connection.starttls()
        self.connection.ehlo()
        self.connection.login(self.username, self.password)

    def send_mail(self, from_, to, message):
        return self.connection.sendmail(from_, to, message)

    def close(self):
        self.connection.close()


if __name__ == '__main__':
    host = raw_input('Digite o servidor de e-mails (exemplo: smtp.gmail.com): ')
    port = raw_input('Digite a porta (exemplo: 587): ')
    username = raw_input('Digite seu login (geralmente o email) no servidor: ')
    password = getpass.getpass('Digite a senha do e-mail: ')
    email_connection = EmailConnection(host, port, username, password)
    email_connection.connect()
    i = 0

    emails = [
              {'gentilico': 'cariocas e fluminenses',
               'email': 'pythonrio@yahoogrupos.com.br'},
              {'gentilico': 'catarinenses',
               'email': 'pug-sc@yahoogrupos.com.br'},
              {'gentilico': 'alagoanos e alagoanas',
               'email': 'pug-al@googlegroups.com'},
              {'gentilico': 'alagoanos e alagoanas',
               'email': 'grupy-al@googlegroups.com'},
              {'gentilico': 'amazonenses',
               'email': 'grupy-am@googlegroups.com'},
              {'gentilico': 'baianos e baianas',
               'email': 'grupy-ba@googlegroups.com'},
              {'gentilico': 'brasilienses',
               'email': 'grupy-df@googlegroups.com'},
              {'gentilico': 'capixabas',
               'email': 'grupy_es@googlegroups.com'},
              {'gentilico': 'paraibanos e paraibanas',
               'email': 'grupy-pb@googlegroups.com'},
              {'gentilico': 'paranaenses',
               'email': 'grupy-pr@googlegroups.com'},
              {'gentilico': 'potiguares',
               'email': 'grupy-rn@googlegroups.com'},
              {'gentilico': 'gaúchos e gaúchas',
               'email': 'pytche@googlegroups.com'},
              {'gentilico': 'gaúchos e gaúchas',
               'email': 'grupy-rs@googlegroups.com'},
              {'gentilico': 'paulistas',
               'email': 'grupy-sp@googlegroups.com'},
              {'gentilico': 'mineiros e mineiras',
               'email': 'python-mg@googlegroups.com'},
              {'gentilico': 'cearenses',
               'email': 'pug-ce@googlegroups.com'},
              {'gentilico': 'pernambucanos e pernambucanas',
               'email': 'pug-pe@googlegroups.com'},
              {'gentilico': 'goianos e goianas',
               'email': 'grupy-go@googlegroups.com'},
              {'gentilico': 'rondonianos e rondonianas',
               'email': 'grupy-ro@googlegroups.com'},
              {'gentilico': 'ribeirão-pretanos e ribeirão-pretanas',
               'email': 'grupy-rp@googlegroups.com'},
              {'gentilico': 'maranhenses',
               'email': 'pug-ma@googlegroups.com'},
              {'gentilico': 'brasileiros e brasileiras',
               'email': 'python-brasil@googlegroups.com'},
              {'gentilico': 'associados e associadas da APyB',
               'email': 'apyb-associados@googlegroups.com'},
              {'gentilico': 'científicos',
               'email': 'pyscience-brasil@googlegroups.com'},
              {'gentilico': 'usuários e usuárias de web2py',
               'email': 'web2py-users-brazil@googlegroups.com'},
              {'gentilico': 'da APyB-ConDir',
               'email': 'apyb-condir@googlegroups.com'},
              {'gentilico': 'piauienses',
               'email': 'python-pi@googlegroups.com'},
    ]

    for row in emails:
        mensagem = msg
        for key, value in row.iteritems():
            mensagem = mensagem.replace('{%s}' % key, value)

        i += 1
        sys.stdout.write('Enviando email %02d para <%s> ... ' % \
                         (i, row['email']))
        response = email_connection.send_mail(remetente, email, mensagem)
        print('OK' if response == {} else response)
        time.sleep(0.1) # alguns servidores de e-mail fecham a conexão quando a
                        # taxa de e-mails enviados é grande

    email_connection.close()
