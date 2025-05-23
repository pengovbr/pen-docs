Sequências
==========

Introdução à Funcionalidade "Sequência"
---------------------------------------

Cada unidade do órgão ou entidade tem sua própria sequência de processos e são diferentes para cada ano. 

A alteração da sequência de um processo é bastante útil em situações de migração da utilização de processo analógico para digital no decorrer do ano no qual já existem processos criados e ainda em andamento. 

Assim essa funcionalidade permite que os processos criados tenham um Número Único de Protocolo (NUP) diferente daqueles processos criados anteriormente em formato não digital. 

Por exemplo, a unidade “XPTO” tem o último processo criado na unidade com o final X. Contudo, esse não é o último criado na unidade, pois antes da utilização do sistema, processos em papel foram criados. Então a sequência foi atualizada para o valor X + 15 com o objetivo de contemplar os processos criados em formato analógico.

Para acessar essa funcionalidade no sistema, o usuário com perfil “Informática” deve acompanhar o caminho descrito a seguir:

1. Acesse o SEI e entre no menu principal;
2. Selecione a opção “Infra”;
3. Clique no item “Sequências”.

.. figure:: _static/images/04-26_Introducao-a-Funcionalidade-Sequencia_TelaSEI_Acessar-Sequencias.png

.. admonition:: Nota

   Apenas usuários com o perfil “Informática” têm acesso ao menu “Infra”. Portanto, o usuário com apenas perfil “Administrador” não tem acesso a essa funcionalidade.

Entre as sequências presentes no sistema estão a de numeração de processos de cada unidade, a de quantidade de usuários externos e a de quantidade de usuários internos. 

Por exemplo, a unidade de código “82667” (Teste_MP) tem duas sequências: “seq_2018_uni_sei_82667” e “seq_2019_uni_sei_82667”. 

O número apresentado na coluna “Valor Atual” representa a quantidade de processos abertos na unidade com o começo do NUP 82667, sendo a primeira em 2018 e a segunda em 2019. 

No primeiro caso, o NUP do processo é 82667.000009/2018-89 e o do segundo caso é 82667.000004/2019-37.


.. admonition:: Importante
 
   Caso o código do SEI da unidade protocolizadora sofra alguma alteração durante o ano, o valor da sequência não representa a quantidade de processos gerados pela unidade, e sim a quantidade de processos com aquele código.

As informações da quantidade de processos podem ser ratificadas por meio da funcionalidade “Estatísticas da Unidade”. 

A tela dessa funcionalidade é apresentada da seguinte maneira:

.. figure:: _static/images/04-26_Introducao-a-Funcionalidade-Sequencia_Tela_Estatisticas-da-Unidade.png

Outro exemplo é o ID do último sistema cadastrado no SEI, o qual é mantido pela sequência “usuario_sistema”, sendo que seu valor conforme apresentado na imagem a seguir é 2. Essa informação é ratificada por meio do seguinte caminho: no menu principal, acesse “Administração”, em seguida selecione “Sistemas” e por fim clique em “Listar”. 

A tela dessa funcionalidade é apresentada da seguinte maneira:

.. figure:: _static/images/04-26_Introducao-a-Funcionalidade-Sequencia_Tela_Sistemas.png

Manutenção
----------

O usuário com perfil “Informática” pode realizar algumas ações de manutenção na funcionalidade “Sequências”. São elas: inclusão, alteração, exclusão e consulta de sequência. As opções alteração, exclusão e consulta de sequência estão disponíveis na coluna “Ações” localizada do lado direito da tabela, enquanto que a opção inclusão está disponível por meio do botão “Nova” localizado no canto superior direito da tela. 

A tela dessa funcionalidade é apresentada da seguinte maneira:

.. figure:: _static/images/04-26_Manutencao_Tela_Manutencao-Sequencias.png

Inclusão de Sequência
---------------------

A tela de inclusão de uma sequência é composta pelos seguintes campos, todos de preenchimento obrigatório:

**Campos a serem preenchidos:**

- **Nome**: campo destinado à descrição da sequência.
- **Incremento**: nesse campo deve conter informações de como o valor da sequência é incrementado a cada ação, por exemplo: +1, +2.
- **Valor Atual**: esse campo refere-se ao valor atual da sequência.
- **Valor Máximo**: esse campo refere-se ao valor máximo a ser alcançado pela sequência.

_**Lembre-se de salvar a operação!**_ 

A imagem a seguir demonstra a disposição dos campos descritos:

.. figure:: _static/images/04-26_Inclusao-de-Sequencia_Tela_Nova-Sequencia.png

Alteração
---------

A ação “Alterar Sequência” permite ao usuário modificar as informações dos campos. Para alterar um critério já cadastrado, é necessário selecionar a sequência que se deseja alterar e clicar no ícone “Alterar Sequência” disponível na coluna “Ações”. Em seguida abrirá uma nova tela com os campos “Nome”, “Incremento”, “Valor Atual” e “Valor Máximo”, todos habilitados para alteração.

.. figure:: _static/images/04-26_Alteracao_Tela_Alterar-Sequencias.png

Exclusão
--------

A ação “Excluir Sequência” pode ser realizada de duas maneiras:

1. A primeira maneira é localizar a sequência que se deseja excluir e clicar em “Excluir Sequência” localizado na coluna “Ações” à direita da tabela.
2. A segunda maneira é selecionar as checkboxes das sequências que serão excluídas e em seguida clicar no botão “Excluir” localizado no menu superior à direita da tela. 

Depois disso, aparece uma mensagem de confirmação da exclusão conforme imagem a seguir:

.. figure:: _static/images/04-26_Exclusao_Tela_Excluir-Sequencias.png

Consulta de Sequência
---------------------

Para consultar as informações das sequências, o usuário com perfil “Informática” deve selecionar a sequência que se deseja consultar e clicar no ícone “Consultar Sequência” disponível na coluna “Ações”. Em seguida abrirá uma nova tela com os campos “Nome”, “Incremento”, “Valor Atual” e “Valor Máximo”, porém não é possível editá-los, somente visualizá-los.

.. figure:: _static/images/04-26_Consulta-de-Sequência_Tela_Consultar-Sequencias.png

Vamos reforçar nosso aprendizado sobre a funcionalidade ensinada com o vídeo a seguir:


Clique `[aqui] <https://cdn.evg.gov.br/cursos/304_EVG/videos/modulo07video05.mp4>`_ para ver o vídeo.