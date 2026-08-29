Manual de Configuração do Módulo de Integração do Tramita.gov.br
==============================================================

O objetivo deste documento é descrever os procedimento para realizar a
configuração do Módulo de Integração com o Tramita.GOV.BR
(**`mod-sei-pen <https://github.com/pengovbr/mod-sei-pen/>`**) no Sistema Eletrônico de Informações (SEI).

O módulo **PEN** é o responsável por integrar o Sistema Eletrônico de
Informações - SEI à plataforma de interoperabilidade do Tramita GOV.BR. Este projeto tem como objetivo interligar
todos os sistema de processo eletrônico do Poder Executivo Federal a fim
de proporcionar a troca de documentos oficiais de forma rápida,
simplificada e segura.

A utilização deste módulo adicionará novas funcionalidades ao SEI,
permitindo, entre outros: - Enviar e receber processos administrativos
de outras instituições - Acompanhar a relação de processos em trâmite
externo

Para maiores informações sobre o Tramita.GOV.BR e o PEN, acesse
https://www.gov.br/pen.

Este documento está estruturado nas seguintes seções:

1. `Instalação <https://github.com/pengovbr/mod-sei-pen/blob/master/docs/INSTALL.md>`__: Procedimentos destinados à Equipe
   Técnica responsáveis pela instalação do módulo nos servidores web e
   atualização do banco de dados.

2. `Configuração <#CONFIGURAÇÕES>`__: Procedimentos destinados ao
   Administradores do SEI responsáveis pela configuração do módulo
   através da funcionalidades de administração do sistema.


CONFIGURAÇÕES
-------------

Esta seção descreve os passos de configuração do módulo de Integração do
SEI com o Tramita.GOV.BR. Todos os itens descritos nesta seção são
destinados aos Administradores do sistema SEI da instituição,
responsáveis pela alteração de configurações gerais do sistema através
do menu de administração do SEI (**SEI >> Administração >> Processo
Eletrônico Nacional**)

.. _configurar-os-parâmetros-do-módulo-de-integração-pen-1:

2.1. Configurar os parâmetros do Módulo de Integração PEN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Acesse a funcionalidade **[SEI > Administração > Processo Eletrônico
Nacional > Parâmetros de Configuração]** para configurar os parâmetros
de funcionamento do módulo:

Repositório de Estruturas:
^^^^^^^^^^^^^^^^^^^^^^^^^^

| *Identificador do repositório de origem do órgão na estrutura
  organizacional. Este identificador é informado para a instituição pela
  equipe do Processo Eletrônico Nacional no envio do pacote de
  integração.*
| Exemplo: Poder Executivo Federal - *Valor 1 (Código de identificação
  da estrutura organizacional do Poder Executivo Federal)*

Tipo de Processo Externo:
^^^^^^^^^^^^^^^^^^^^^^^^^

*Identificação do Tipo de Processo que será aplicado à todos os
processos e documentos recebidos de outras instituições pelo
Tramita.GOV.BR.*

Como o recebimento é realizado de forma automática, o sistema precisa
atribuir um Tipo de Processo padrão para o novo processo recebido. Com
isto, sugerimos a criação de um tipo de processo específico para estes
processos, permitindo a fácil identificação e reclassificação, caso
necessário. Segue abaixo um exemplo de Tipo de Processo que pode ser
criado para esta situação:

::

   Nome: Processo Recebido Externamente (a classificar) 
   Descrição: Processos recebidos de outras instituições 
   // O assunto deve ser definido juntamente com a área de documentação
   Sugestão de Assuntos: a classificar
   Níveis de Acesso Permitidos: Restrito e Público 
   Nível de Acesso Sugerido: Público 
   Processo único no órgão por usuário interessado: Não
   Interno do Sistema: Sim       

Unidade SEI para Representação de Órgãos Externos
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Identificação da unidade administrativa que representará órgãos e
unidades externas nos históricos de andamento do processo. Esta
configuração também é necessária para que o sistema possa aplicar
corretamente as regras de restrição de modificação de dados cadastrais
de processos e documentos criados por outras instituições.*

A unidade a ser definida neste parâmetro será utilizada internamente
pelo módulo e não deverá ter acesso de nenhum usuário do sistema. Por
isto, não deve ser utilizada uma unidade pré-existente da própria
instituição, sendo recomendado a criação de uma nova unidade
administrativa “virtual” no SIP para esta configuração.

Essa unidade **não deve ser mapeada no item de [Administração > Processo
Eletrônico Nacional > Mapeamento de Unidades]**.

A opção “Disponível para recebimento de processos” deverá estar
habilitada para o cadastro da unidade selecionada neste campo.

Sugerimos que a criação uma nova unidade no SEI denominada: [sigla =
**Tramita.GOV.BR**, nome: **Processo recebido via Tramita.GOV.BR**] para
atribuição à este parâmetro do sistema. Lembrando que novas unidades
devem ser criadas inicialmente no SIP (SIP > Unidades) e depois
atribuídas à hierarquia de unidades do SEI (SIP > Hierarquias > Montar).

Envia E-mail de Notificação de Recebimento
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*Indicação se o sistema irá enviar um e-mail de notificação alertando o
recebimento de um novo processo para a unidade. Necessário que a unidade
tenha um e-mail configurado em seu cadastro de contato.*

2.2. Mapeamento de unidades que poderão realizar o envio e recebimento de trâmites externos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Acesse a funcionalidade **[SEI > Administração > Processo Eletrônico
Nacional > Mapeamento de Unidades]** para configurar as unidades
administrativas do SEI com as respectivas unidades habilitadas no Portal
do Processo Eletrônico Nacional para envio e recebimento de processos.

As unidades administrativas que estão habilitadas para envio e
recebimento de processos são gerenciadas pela própria instituição no
Portal do Processo Eletrônico Nacional. Veja seção `Pré-condições para
utilização <#pré-condições>`__

Primeiro selecione a unidade administrativa do SEI no campo de seleção e
depois digite o nome da unidade habilitada no Barramento e aperte ENTER
para que seja realizada uma consulta às do cadastro da unidade
habilitada no Tramita.GOV.BR.

--------------

2.3. Mapeamento de Tipos de Documentos do SEI com as Espécies Documentais do PEN
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A partir da versão **mod-sei-pen** 2.0.0, os mapeamentos dos Tipos de
Documentos do SEI são realizados de forma automática durante a
instalação do módulo ou automaticamente através do agendamento de
tarefas **PENAgendamentoRN::atualizarInformacoesPEN**.

Caso seja necessário modificar o mapeamento pré-definido pelo sistema, a
alteração pode ser realizada através da funcionalidade **Mapeamento de
Tipos de Documentos** localizado em [SEI >> Administração >> Processo
Eletrônico Nacional >> Mapeamento de Tipos de Documentos]

**Observação**: Os tipos de documentos a serem mapeados deverão estar
configurados no SEI como Externo ou Interno/Externo

Este mapeamento precisa ser feito tanto para o envio de processos como
para o recebimento, sendo necessário realizar a configuração através das
duas funcionalidades apresentadas abaixo:

-  SEI > Administração > Processo Eletrônico Nacional > Mapeamento de
   Tipos de Documentos > **Envio**
-  SEI > Administração > Processo Eletrônico Nacional > Mapeamento de
   Tipos de Documentos > **Recebimento**

2.3.1. Atribuição de Espécie Documental Padrão para Envio
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

A configuração de Espécie Documental Padrão para Envio define qual será
o comportamento do sistema ao enviar processos que contenham Tipos de
Documentos não mapeados previamente pelo Administrador. Neste caso, a
espécie documental configurada será aplicada automaticamente, evitando
que o trâmite seja cancelado pela falta desta configuração.

O mapeamento de Espécie Documental Padrão para Envio deve ser feito
através da funcionalidade:

::

   [SEI > Administração > Processo Eletrônico Nacional > Mapeamento de Tipos de Documentos > **Envio > Botão "Atribuir Espécie Padrão"**]

2.3.2. Atribuição de Tipo de Documento Padrão para Recebimento
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

A configuração de Tipo de Documento Padrão para Recebimento define qual
será o comportamento do sistema ao receber processos que contenham
Espécies Documentais não mapeadas previamente pelo Administrador. Neste
caso, o tipo de documento configurado será aplicado automaticamente,
evitando que o trâmite seja cancelado pela falta de mapeamento.

O mapeamento de Tipo de Documento Padrão para Recebimento deve ser feito
através da funcionalidade:

::

   [SEI > Administração > Processo Eletrônico Nacional > Mapeamento de Tipos de Documentos > **Recebimento > Botão "Atribuir Tipo de Documento Padrão"**]

PS: Somente Tipos de Documento com aplicabilidade ‘Externa’ ou ‘Interna
e Externa’ podem ser selecionados para esta configuração.

--------------

2.4. Mapeamento de hipóteses legais do SEI com o Tramita.GOV.BR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Acesse a funcionalidade **[SEI > Administração > Processo Eletrônico
Nacional > Mapeamento de Hipóteses Legais]** para configurar as
hipóteses legais do SEI com a relação de hipóteses pré-definidas pelo
Tramita.GOV.BR.

Esta vinculação é necessária para que o módulo de integração possa
traduzir corretamente as hipóteses legais definidas no SEI para o
subconjunto de hipóteses aceitas pelos Tramita.GOV.BR no momento do
envio ou recebimento de processos.

Este mapeamento precisa ser feito tanto para o envio de processos como
para o recebimento, sendo necessário realizar a configuração através das
duas funcionalidades apresentadas abaixo:

-  SEI > Administração > Processo Eletrônico Nacional > Mapeamento de
   Hipóteses Legais > **Envio**
-  SEI > Administração > Processo Eletrônico Nacional > Mapeamento de
   Hipóteses Legais > **Recebimento**

2.4.1 Hipótese de Restrição Padrão
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A configuração de Hipótese de Restrição Padrão define qual será o
comportamento do sistema ao enviar ou receber processos/documentos que
contenham restrição de acesso com hipóteses legais não mapeadas
previamente pelo Administrador. Neste caso, a hipótese legal padrão
configurado será aplicado automaticamente, evitando que o trâmite seja
cancelado pela falta de mapeamento.

SUPORTE
-------

Em caso de dúvidas ou problemas durante o procedimento de atualização,
favor entrar em conta pelos canais de atendimento disponibilizados na
Central de Atendimento do Processo Eletrônico Nacional, que conta com
uma equipe para avaliar e responder esta questão de forma mais rápida
possível.

Para mais informações, contate a equipe responsável por meio dos
seguintes canais: - `Portal de Atendimento (PEN): Canal de
Atendimento <https://portaldeservicos.economia.gov.br>`__ - Módulo do
Barramento - Telefone: 0800 978 9005
