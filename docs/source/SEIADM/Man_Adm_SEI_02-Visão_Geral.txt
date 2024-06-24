```rst
Visão Geral do SEI e do SIP
============================

O SEI é um sistema que trabalha em conjunto com outro sistema o SIP (Sistema de Permissões) que promove o cadastramento inicial de dados do SEI. Visto o seu nome além de realizar o cadastro inicial de dados (Usuários Unidades Hierarquia de Unidades) ele possibilita a concessão e retirada de permissões.

.. image:: Foto1.png
   :alt: Foto número 1

Apesar de o SIP atender a um único sistema (o SEI) vale ressaltar que os dois são sistemas diferentes portanto possuem login próprio em que o usuário e senha de um não necessariamente acessará o outro.

Conhecendo o SIP
=================

O SIP é o Sistema de Permissões que permite o cadastramento inicial de usuários unidades hierarquia das unidades e permissões. Ele foi concebido de forma generalista para atender quaisquer sistemas que necessitem desses dados.
Dessa forma dados específicos que são utilizados no âmbito de cada sistema devem ser complementados em cada um desses sistemas.
O SIP atende a um único sistema que é o SEI. Porém por ter sido criado para atender vários sistemas dados básicos dos usuários e unidades devem ser cadastrados inicialmente no SIP e depois nos casos específicos complementados no SEI.
Para entender as relações entre as respectivas funções do SEI e do SIP segue uma comparação entre os dois sistemas.

.. image:: Foto2.png
   :alt: Foto número 2

SIP     | SEI
--------|---------
Criação de órgãos | Cadastramento de dados dos órgãos
Criação de unidades | Cadastramento de dados das unidades
Criação de hierarquia entre unidades | Indicação dos perfis das unidades
Criação dos perfis de usuários | Gestão dos contatos
Cadastramento de usuários | Configuração de processos e documentos
Gestão da autenticação de usuários | Instrução processual
Gestão de permissões |

Acesso ao SIP e ao SEI
=======================

Ambos os sistemas possuem login próprio em que o usuário e senha de um não necessariamente acessará o outro.
Para acessar o SIP basta adicionar “/SIP” após o endereço de acesso ao SEI da instituição. Para exemplificar vamos acessar o SEI e em seguida o SIP.

- Para acessar o SEI do órgão vamos digitar no navegador de internet o endereço:
 www.sei.[o nome ou sigla do órgão que deseja acessar].gov.br

- Para acessar o SIP do órgão vamos digitar no navegador de internet o endereço:
 www.sei.[o nome ou sigla do órgão que deseja acessar].gov.br/SIP

.. image:: Foto3.png
   :alt: Foto número 3

.. image:: Foto4.png
   :alt: Foto número 4
```

Certifique-se de salvar as imagens com os nomes `Foto1.png`, `Foto2.png`, etc., para que sejam referenciadas corretamente no arquivo `.rst`.