Módulo de Login Externo GOV.BR
===================================================

O módulo **Login Externo GOV.BR** trará ao usuário externo a facilidade e segurança de acessar o SEI via plataforma de autenticação do Governo Federal, chamada no âmbito desta documentação de **Conta gov.br**

Usuário externo é a pessoa física autorizada a acessar ou atuar em determinado(s) processo(s) no SEI, independente de vinculação a determinada pessoa jurídica, para fins de peticionamento ou assinatura de documentos relativos a um Órgão da Administração.

A utilização deste módulo adicionará novas funcionalidades ao SEI, permitindo, entre outros:

 - Autenticar usuários externos utilizando a **Conta gov.br**
 
Para informações sobre como aderir à Conta Gov.Br, acesse: https://sso.acesso.gov.br/


Manual de Utilização
--------------------

Esta seção tem por objetivo demonstrar as funcionalidades que são disponibilizadas pelo módulo de integração e também as configurações que devem ser realizadas no próprio SEI para o seu correto funcionamento.

A instalação do módulo de **Login Externo GOV.BR** irá adicionar uma nova opção de autenticação para os usuários externos, permitindo que seja utilizada a conta única provida pelo **gov.br** para realização do acesso externo ao SEI.

Para acesso ao ambiente externo do SEI da entidade, o usuário deverá acessar a página de acesso externo específica de sua entidade e clicar no botão **[acessar com gov.br]**;

.. figure:: _static/images/tela_acesso_externo_login_unico.png
    :alt: Tela de acesso externo

Será apresentada a tela de login da **Conta gov.br**. O usuário deverá colocar o seu CPF e clicar em continuar. Em seguida, inserir a senha e clicar em Entrar;

Primeiro Acesso ao SEI via Conta gov.br
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Caso seja o primeiro acesso externo do usuário ao SEI, esse será direcionado à tela de complementação de dados cadastrais. Os dados obtidos da Conta gov.br são automaticamente preenchidos e não podem ser modificadados, sendo necessário apenas a complementação de informações, como: endereço, telefones, RG.

Entre as informações cadastrais estão: Nome do Representante, CPF, RG, Telefones de Contato e Endereço.

.. figure:: _static/images/tela_cadastro_externo_super.png
    :alt: Cadastro de usuário externo

.. admonition:: Nota
 
   Também é solicitado uma senha secundária para que o usuário utilize caso ocorra alguma indisponibilidade do serviço de autenticação da **Conta gov.br**.

.. figure:: _static/images/tela_cadastro_externo_senha_alteranativa2.png
    :alt: Cadastro de senha alternativa

Após o preenchimento do formulário, o usuário deverá preencher o código indicado na imagem em tela e clicar em enviar. Em seguida a tela do SEI acesso externo será aberta.

.. admonition:: Nota
 
    O acesso direto ao ambiente externo do SEI somente será concedido caso o usuário possua uma **Conta gov.br** classificada como "Ouro" ou "Prata", o que garante um nível de confiabilidade e de autenticidade em níveis adequados, não necessitando validação manual da documentação para liberação de acesso. Entende-se que a confirmação das informações do usuário foram prestadas devidamente no momento em que o mesmo adiquiriu o respectivo selo de confiabilidade.


Para maiores informações sobre os níveis de confiabilidade da **Conta gov.br**, acesse `O que é Selo de Confiabilidade (Ouro e Prata)? Como posso obter esses selos? <https://www.gov.br/servidor/pt-br/acesso-a-informacao/faq/acesso-gov.br/5-o-que-e-selo-de-confiabilidade-ouro-e-prata-como-posso-obter-esses-selos>`_


Usuário com Cadastro Simples na Conta gov.br (Selo de Confiabilidade Bronze)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Caso o usuário somente tenha realizado o auto-cadastro simplificado na Conta gov.br, ou seja, não tenha aumentado o nível de segurança (Ex: Certificado Digital, Justiça Eleitoral, SIGEPE), o SEI irá seguir o fluxo padrão do sistema, que consiste no encaminhamento de mensagem com as instruções para a complementação das informações necessárias ao acesso externo do usuário.

Para conseguir as credenciais Outro ou Prata, acesse o seu cadastro na `Conta gov.br <https://sso.acesso.gov.br/>`_ siga as orientações presentes no link **[Segurança da Conta] > [Aumentar nível da conta]**.

.. figure:: _static/images/login_unico_mensagem_usuario_bronze.gif
    :alt: Mensagem usuário bronze

.. figure:: _static/images/mensagem_usuario_bronze.png
    :alt: Mensagem usuário bronze

Após apresentar a documentação indicada na mensagem, o usuário será autorizado a utilizar o SEI com acesso externo. A partir deste momento, o seu ingresso no SEI utilizando a conta gov.br será de forma direta, bastando clicar no botão **[acessar com gov.br]** e incluir suas credenciais.

Unificação de usuários externos com conta gov.br
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Caso o usuário já possua um usuário externo, ao acessar o sistema via conta gov.br será aberta tela indicando que foi identificado um usuário externo SEI com o mesmo endereço de email da conta gov.br e possibilitará a associação das destas contas. Tal ação possibilitará que os próximos acessos do usuário ocorram de forma direta.


.. figure:: _static/images/vinculacao_de_contas.png
    :alt: Vinculação de contas

O usuário deverá inserir a senha de usuário externo do SEI, preencher o captcha e clicar em **[Vincular Conta]**. 

Após a vinculação, o usuário será direcionado ao ambiente externo SEI.
