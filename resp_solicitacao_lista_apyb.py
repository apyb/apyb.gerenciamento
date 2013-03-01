#!/usr/bin/env python
# -*- coding=utf-8 -*-

solicitante = 'FULANO'
email = 'fulano@rede.net'
respondente = 'Voluntário da Comunidade Python Brasil'

resposta = """
Prezado(a), Sr(a). {0}.


A lista de associados Python Brasil é exclusiva para membros da
Associação Python Brasil e utilizada para tratar assuntos de 
interesse dos associados.

Infelizmente seu e-mail ({1}) não consta nos
registros de pagamento da associação,mas se houve um equívoco da
nossa parte, peço que por gentileza nos envie o comprovante de
pagamento ou informe a data em que foi paga a anuidade.

Se trocou de e-mail recentemente, podemos conferir e ajustar
seus dados, bastando informar o e-mail anterior e o atual.

Caso queira se associar, acesse a página:
http://associacao.python.org.br/associe-se

Caso tenha outros interesses relacionados à tecnologia Python,
pode optar por se inscrever nas listas da comunidade:
http://www.python.org.br/wiki/ListasDeDiscussao

Certo de sua compreensão, me coloco à disposição para maiores
esclarecimentos.

Atenciosamente, {2}.
""".format(solicitante, email, respondente)

print(resposta)
