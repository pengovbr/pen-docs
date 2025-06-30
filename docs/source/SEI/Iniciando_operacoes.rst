Iniciando Operações
====================

Acesso ao Sistema
+++++++++++++++++

Para acessar o SEI, o usuário deve utilizar um navegador de internet para acessar a URL fornecida pelo órgão ao qual está vinculado, informar seu login, senha e – no caso de instalações multiórgão – o órgão ao qual está vinculado.


.. figure:: _static/images/1-IO-Tela_inicial.gif


Autenticação em dois fatores
+++++++++++++++++++++++++++++

Para habilitar a Autenticação em dois fatores, é necessário acessar a tela de login do SEI, preencher o campo **Usuário**, inserir a **Senha** e clicar sobre a opção **Autenticação em dois fatores**. 

.. admonition:: Nota
    
   O usuário poderá, se desejar, habilitar a Autenticação em dois fatores para efetuar o login no sistema. A disponibilização desse recurso é um dos itens que evidenciam a preocupação com a segurança do sistema e das informações registradas.
   Com essa possibilidade, o usuário poderá adicionar uma camada extra de segurança aos seus dados de acesso, uma vez que essa sistemática associa um dado que o usuário conhece (a sua senha) a um recurso que possui em mãos (o seu smartphone). 

.. figure:: _static/images/tela_A2F.gif

Na tela seguinte, será exibido um link com todas as informações para a habilitação do recurso. O usuário deverá ler as instruções e, em seguida, clicar no botão **Prosseguir**.

Para continuar, é necessário ter, em seu dispositivo móvel, um aplicativo destinado a autenticação em duas etapas. O ***Google Authenticator*** e o ***Microsoft Authenticator*** são exemplos de apps que podem ser utilizados para esta finalidade. 

Após esse procedimento, abra o aplicativo e acesse a opção para leitura de **QR Code**.  

.. admonition:: Nota

   Recomenda-se informar um e-mail pessoal, que não esteja associado à sua Instituição. É imprescindível que a senha de acesso a esse e-mail seja diferente da senha de acesso ao SEI.

Faça a leitura da imagem, insira seu e-mail pessoal e clique em **Enviar**.

.. figure:: _static/images/tela_A2F_envio_email.gif
  

Ao clicar sobre o botão **ACESSAR**, o sistema emitirá uma mensagem informando o envio de um e-mail para habilitação do recurso, com validade de até 60 minutos para a conclusão da solicitação.  

Para ativar a Autenticação em dois fatores, o usuário deve acessar o e-mail e clicar sobre o *link* (ou copiar o endereço eletrônico da mensagem e colar no navegador). 

Para acessar o sistema, insira o usuário e a senha na tela inicial. Depois, clique em **ACESSAR**. 

A tela seguinte exigirá o código de acesso gerado pelo aplicativo. Portanto, consulte o código exibido no app e digite-o no campo apropriado do sistema. Em seguida, clique em **Validar**.  

Para dispositivos utilizados com frequência, o SEI disponibiliza a opção “Não usar o 2FA neste dispositivo e navegador”. Se essa opção for marcada, o código de acesso não será solicitado novamente no mesmo dispositivo e navegador. Porém, se for realizada a limpeza de cookies do navegador, o código de acesso voltará a ser solicitado. 

.. figure:: _static/images/1-IO_tela_inicial_2fa_flag_nao_usar_2fa.png
   :align: center


A desativação da Autenticação em dois fatores também poderá ser feita por meio dessa tela. Ao clicar sobre o botão **Desativar 2FA**, o sistema enviará um link para o e-mail cadastrado, para confirmar a operação. Acessando o e-mail e clicando no link, o recurso será desabilitado e o usuário voltará a efetuar o acesso somente com usuário e senha. 

.. admonition:: Saiba Mais
   
   Caso o usuário tenha utilizado a Autenticação em dois fatores e, por qualquer motivo, tenha efetuado a desabilitação do recurso ou perdido o prazo para sua ativação, será necessário, para efetuar uma nova tentativa, verificar se essa conta permanece registrada no aplicativo. Em caso afirmativo, será preciso excluí-la    antes de efetuar a leitura do novo QR Code.


Barra de Ferramentas
++++++++++++++++++++

No topo da página está localizada a barra de ferramentas do sistema.

.. figure:: _static/images/1-IO_barra_de_ferramentas.png


As funcionalidades disponíveis são:


.. list-table::
   :widths: 20 35
   :header-rows: 1

   - * Ícones Disponíveis
     * Descrição
   - * .. figure:: _static/images/1-IO_icone_exibir_ocultar.png
          :align: center 
     * **Exibir/ocultar:** permite ocultar e exibir o menu principal.
   - * .. figure:: _static/images/1-IO_icone_pesquisa.png
          :align: center     
     * **Pesquisa:** possibilita uma busca rápida a processos ou documentos.
   - * .. figure:: _static/images/1-IO_icone_caixa_selecao_unidade.png
          :align: center 
     * **Caixa de seleção de unidade:** informa ao usuário qual unidade ele está acessando e possibilita navegar pelas unidades nas quais tenha permissão.
   - * .. figure:: _static/images/1-IO_icone_controle_de_processos.png
          :align: center
     * **Controle de processos:** permite ao usuário voltar à tela principal do sistema.
   - * .. figure:: _static/images/icone_em_numeros.png
          :align: center
     * **Painel de Controle:** possibilita ao usuário ter uma visão mais resumida e personalizada dos processos da unidade. Tal funcionalidade foi disponibilizada na barra de ferramentas do SEI a partir da **versão 4.1**. 
   - * .. figure:: _static/images/icone_acessibilidade.png
          :align: center
     * **Acessibilidade:** são mecanismos que permitem ao usuário acessar rapidamente funções ou visões do SEI, por meio de combinações de teclas de atalho. Tal funcionalidade foi incorporada ao SEI a partir da **versão 4.1**.
   - * .. figure:: _static/images/1-IO_icone_usuario.png
          :align: center
     * **Usuário:** identifica o usuário que está acessando o sistema.
   - * .. figure:: _static/images/1-IO_icone_configuracoes_do_sistema.png
          :align: center 
     * **Configurações do sistema:** permite que o usuário altere o esquema de cores do sistema.
   - * .. figure:: _static/images/1-IO_icone_sair_do_sistema.png
          :align: center
     * **Sair do sistema:** permite ao usuário sair com segurança do sistema.

Lista de Acessibilidades
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :widths: 20 35
   :header-rows: 1

   - * "Atalho"
     * Descrição
   - * ALT + F1
     * Exibe esta tela.
   - * ALT + F2
     * Exibe a tela de Controle de Processos.
   - * ALT + F3 
     * Exibe a tela de Painel de Controle.
   - * ALT + F9
     * Exibe ou oculta o menu lateral.
   - * ALT + F10
     * Acessa a Pesquisa Rápida.
   - * ALT + F11
     * Troca de unidade.
   - * ALT + F12
     * Posiciona no link sair do sistema.
   - * ALT + M
     * Pesquisa no menu.
   - * ALT + T
     * Posiciona no título da tela.
   - * ALT + B
     * Posiciona no primeiro botão da barra de comandos.
   - * TAB
     * Permite a navegação entre componentes da tela.
   - * SHIFT + TAB
     * Permite a navegação inversa entre componentes da tela.
   - * ALT + Seta acima
     * Posiciona no componente de seleção da linha anterior (se o foco está em um componente em tabela).
   - * ALT + Seta abaixo
     * Posiciona no componente de seleção da próxima linha (se o foco está em um componente em tabela).
   - * ESC
     * Fecha janelas de seleção abertas internamente.
   - * ALT + R
     * Posiciona na tabela de processos recebidos.
   - * ALT + G
     * Posiciona na tabela de processos gerados.
   - * CTRL + ALT + R
     * Posiciona no item raiz da árvore que representa o número do processo.
   - * CTRL + ALT + S
     * Posiciona no item de protocolo selecionado atualmente na árvore. 
   - * CTRL + ALT + F
     * Posiciona na barra de funcionalidades associadas com o protocolo selecionado (usar TAB para navegar entre as funcionalidades disponíveis).
   - * CTRL + ALT + V
     * Posiciona na área de visualização de conteúdo associada com protocolo selecionado ou funcionalidade escolhida.
   - * CTRL + ALT + U
     * Posiciona no último item de protocolo da árvore.
   - * CTRL + ALT + S
     * Salva o documento em edição.
   - * CTRL + SHIFT + A
     * Assina um documento em edição.
   - * CTRL + SHIFT + L 
     * Insere um link para processo ou documento do SEI. 
   - * CTRL + SHIFT + X 
     * Insere o conteúdo de um texto padrão (AutoTexto).
   - * CTRL + B 
     * Torna o texto selecionado em Negrito.
   - * CTRL + I
     * Torna o texto selecionado em Itálico.
   - * CTRL + U 
     * Torna o texto selecionado em Sublinhado.
   - * CTRL + X 
     * Recorta o conteúdo selecionado em um documento.
   - * CTRL + C
     * Copia o conteúdo selecionado em um documento.
   - * CTRL + V 
     * Insere ("cola") o conteúdo existente na área de transferência para um documento em edição.
   - * CTRL + SHIFT + V
     * Insere ("cola") o conteúdo existente na área de transferência para um documento em edição, como texto sem formatação. 
   - * CTRL + Z
     * Desfaz a última operação em um documento em edição.
   - * CTRL + Y
     * Refaz a última operação em um documento em edição.
   - * ALT + 0
     * Exibe instruções de acessibilidade do editor de textos.


Menu Principal
+++++++++++++++

É a coluna localizada na lateral esquerda da tela. Disponibiliza um conjunto de funcionalidades de acordo com o perfil do usuário ou do tipo de unidade.

As funcionalidades estão apresentadas em ordem alfabética e contêm símbolos para facilitar a sua identificação e correspondência com os ícones existentes na tela de controle de processos e tela do processo.

.. figure:: _static/images/1-IO_tela_menu_principal.png

O perfil básico apresenta as seguintes opções:

* **Acompanhamento Especial**: permite visualizar a relação dos processos da unidade que estão em acompanhamento especial e outras informações sobre cada acompanhamento, como o usuário responsável, a data de inclusão, o grupo em que ele está incluído e um campo para observação.

* **Base de Conhecimento**: permite descrever as etapas de um processo e anexar documentos de referência relacionados ao Tipo de Processo vinculado àquela base de conhecimento.

* **Blocos de Assinatura**: Permite gerenciar os blocos de assinatura criados pela unidade ou disponibilizados a ela. Possibilita que mais de um usuário, de qualquer unidade, possa assinar documentos produzidos no sistema.

* **Blocos de Reunião**: Permite gerenciar os blocos de reunião criados pela unidade ou disponibilizados a ela. Possibilita que uma unidade disponibilize processos para conhecimento de outras unidades, sem que estas tenham uma atuação formal sobre eles, para serem discutidos em reuniões ou decisão colegiada. Essa funcionalidade permite a visualização do conteúdo dos documentos mesmo que não estejam assinados.

* **Blocos Internos**: Permite visualizar os blocos internos criados pela unidade. Possibilita a organização de conjuntos de processos que possuam alguma ligação entre si. Esta forma de organização é visível apenas pela unidade que a criou.

.. admonition:: Saiba Mais

   Além disso, diferentemente do Acompanhamento Especial – que pode ser utilizado para assinalar qualquer processo, independentemente de onde este esteja aberto – a    inclusão em bloco interno só pode ser feita em processos abertos na unidade.

* **Contatos**: permite o cadastro e consulta dos contatos que serão exibidos como opções para o preenchimento dos campos Interessados, Remetente e Destinatários, na tela de cadastro do processo ou do documento, por exemplo.

* **Controle de Prazos**: ferramenta utilizada para administração de prazos dentro da unidade. É uma funcionalidade de organização interna – ou seja, outras unidades não terão acesso ao Controle de Prazos da unidade.

* **Controle de Processos**: Direciona o usuário para a tela principal do SEI, onde são visualizados todos os processos que estão em sua unidade.

* **Estatísticas**: Permite visualizar as estatísticas da unidade e o desempenho de processos.

* **Favoritos**: permite visualizar e gerenciar a relação de processos salvos como favoritos na unidade, possibilitando acesso rápido a eles.

* **Grupos de Contato**: possibilita a criação de uma lista a partir da seleção de contatos cadastrados no sistema.

* **Grupos de E-mail**: permite criar e gerenciar grupos de e-mail para o envio de mensagens eletrônicas dentro do sistema.

* **Grupos de Envio**: permite criar e gerenciar grupos de unidades para o envio de processos dentro do sistema.

* **Iniciar Processo**: permite iniciar um novo processo no SEI.

* **Marcadores**: permite que a unidade crie e gerencie marcadores para os processos sob sua gestão. Utilizado para organização interna da equipe de trabalho.

* **Painel de Controle**: Funcionalidade que possibilita ao usuário ter uma visão resumida e personalizada dos processos da unidade.

* **Pesquisa**: Possibilita a pesquisa avançada de informações, documentos ou processos.

* **Pontos de Controle**: Recurso que permite atribuir Pontos de Controle (fases ou categorias) para acompanhamento de processos.

* **Processos Sobrestados**: permite visualizar a relação de processos da unidade que se encontram suspensos temporariamente e as informações relativas ao sobrestamento.

* **Retorno Programado**: Permite verificar a relação de retornos programados da unidade – aqueles processos aos quais foram atribuídos prazos para resposta.

* **Textos Padrão**: Permite incluir textos que sejam recorrentes na unidade para utilização em documentos e e-mails produzidos no sistema. 


Tela de Controle de Processos
+++++++++++++++++++++++++++++

Ao acessar o sistema, o usuário será direcionado para a tela Controle de Processos. Essa tela apresenta os processos abertos na unidade (recebidos e gerados) e disponibiliza diversas funcionalidades por meio da Barra de Ferramentas, do Menu Principal (ambos abordados em capítulos anteriores), e da Barra de Ícones. 

Além disso, a tela de controle de processos apresenta filtros que permitem diferentes formas de visualização dos processos da Unidade.

.. figure:: _static/images/1-IO_tela_controle_de_processos.png

Nessa tela é possível realizar operações com processos em lote. Para isso, é necessário clicar na caixa de seleção ao lado do número de cada processo e selecionar o ícone da operação desejada, conforme a necessidade.

Abaixo, estão descritas as diversas funcionalidades da barra de ícones. O passo a passo para o uso de cada uma dessas funcionalidades será apresentado mais à frente. 


.. list-table::
   :header-rows: 1
   :widths: 5 35

   - * Ícones
     * Descrição
   - * |enviar_processo|
     * **Enviar processo:** permite tramitar processo(s) para outra unidade. Conclui o processo na unidade remetente, a menos que, no momento do envio, o usuário assinale a opção “Manter o processo aberto na unidade atual”. Se concluído, o processo desaparecerá da tela “Controle de Processos”, mas poderá ser recuperado na Pesquisa ou Acompanhamento Especial (quando assinalado).
   - * |atualizar_andamento| 
     * **Atualizar andamento:** permite incluir uma informação ou despacho de andamento ao(s) processo(s) selecionado(s).
   - * |Atribuição_de_processos|
     * **Atribuição de processos:** permite distribuir processos entre os usuários da unidade, atribuindo-lhes responsabilidade. Essa informação não fica disponível para outras unidades que, eventualmente, consultarem o processo.
   - * |Incluir_em_bloco|
     * **Incluir em bloco:** utilizado para organizar os processos dentro do sistema, incluindo-os em Bloco Interno ou Bloco de Reunião.
   - * |Sobrestar_processo|
     * **Sobrestar processo:** utilizado quando o processo precisa aguardar alguma providência antes de ter prosseguimento, mantendo-se suspenso temporariamente na unidade.
   - * |Concluir_processo_nesta_unidade|
     * **Concluir processo nesta unidade:** permite finalizar o processo na unidade em que o usuário que está acessando o sistema. O processo desaparecerá da tela “Controle de Processos”, mas poderá ser recuperado na Pesquisa ou Acompanhamento Especial quando tiver sido previamente incluído em acompanhamento).
   - * |Anotações|
     * **Anotações:** permite inserir informações adicionais que não devem constar dos autos do processo. Utilizado geralmente para orientações internas de trabalho da equipe. Essas informações não ficam disponíveis para outras unidades que, eventualmente, consultarem o processo.
   - * |Acompanhamento_especial|
     * **Acompanhamento especial:** possibilita ao usuário acompanhar o andamento do processo, mesmo que ele esteja tramitando em outra unidade, sem a necessidade de mantê-lo aberto em sua unidade.
   - * |Incluir_documento|
     * **Incluir documento:** permite incluir novo documento no(s) processo(s) selecionado(s).
   - * |Gerenciar_marcador|
     * **Gerenciar marcador:** permite que a unidade crie e gerencie marcadores para os processos sob sua gestão. Utilizado para organização interna da equipe de trabalho. Essas informações não ficam disponíveis para unidades que, eventualmente, consultarem o processo.
   - * |Controle_de_Prazos|
     * **Controle de Prazos:** ferramenta utilizada para administração de prazos dentro da unidade. É uma funcionalidade de organização interna, dessa forma, outras unidades não terão acesso ao Controle de Prazos da unidade.

.. |enviar_processo| image:: _static/images/1-IO_icone_Enviar_Processo.png
   :align: middle
   :width: 50
   
.. |atualizar_andamento| image:: _static/images/1-IO_icone_Atualizar_Andamento.png
   :align: middle
   :width: 50

.. |Atribuição_de_processos| image:: _static/images/1-IO_icone_Atribuicao_processo.png
   :align: middle
   :width: 50

.. |Incluir_em_bloco| image:: _static/images/1-IO_icone_incluir_bloco.png
   :align: middle
   :width: 50

.. |Sobrestar_processo| image:: _static/images/1-IO_icone_sobrestar_processo.png
   :align: middle
   :width: 50

.. |Concluir_processo_nesta_unidade| image:: _static/images/1-IO_icone_concluir_processo.png
   :align: middle
   :width: 50

.. |Anotações| image:: _static/images/1-IO_icone_Anotacoes.png
   :align: middle
   :width: 50

.. |Acompanhamento_especial| image:: _static/images/1-IO_icone_Acompanhamento_especial.png
   :align: middle
   :width: 50

.. |Incluir_documento| image:: _static/images/1-IO_icone_incluir_documento.png
   :align: middle
   :width: 50

.. |Gerenciar_marcador| image:: _static/images/1-IO_icone_Gerenciar_Marcador.png
   :align: middle
   :width: 50

.. |Controle_de_Prazos| image:: _static/images/1-IO_icone__cotrole_de_prazos.png
   :align: middle
   :width: 50


Os Filtros disponíveis na tela Controle de Processos, que ficam logo abaixo da Barra de Ícones, permitem diversas visualizações dos processos. Veja a explicação de cada opção a seguir:

.. list-table::
   :header-rows: 1
   :widths: 15 35

   - * Ícones
     * Descrição
   - * *Visualização detalhada*
     * Possibilita uma visualização mais detalhada dos processos na tela. O usuário poderá configurar essa opção clicando no link “Visualização detalhada” e, em seguida, no link “Configurar nível de detalhe”.
   - * *Configurar nível de detalhe*
     * Esse link surge quando o usuário clica em “Visualização detalhada”. Ele permite a configuração do nível de detalhe a ser exibido em tela. O usuário poderá selecionar uma das seguintes opções a serem apresentadas na tela: Atribuição, Anotação, Tipo de processo, Especificação, Interessados, Observação, Controle de Prazo, Para Devolver, Aguardando Retorno, Última Movimentação na Unidade e Marcadores.
   - * *Ver processos atribuídos a mim*
     * Aplica filtro para que sejam mostrados, na tela Controle de Processos, apenas os processos atribuídos ao usuário que está acessando o sistema.
   - * *Ver por marcadores*
     * Exibe os Marcadores utilizados na unidade e a quantidade de processos em cada Marcador. Para acessar os processos, basta clicar no número correspondente à quantidade de cada Marcador, na coluna Processos.
   - * *Ver por tipo de processo*
     * Exibe os tipos de processos abertos na unidade e a quantidade de processos de cada tipo. Para acessar os processos, basta clicar no número correspondente à quantidade de cada tipo, na coluna Processos.


Os símbolos e orientações visuais apresentados na tela Controle de Processos auxiliam na identificação da situação dos processos. Veja a descrição de cada um deles a seguir:

.. list-table::
   :header-rows: 1
   :widths: 10 35

   - * Ícones/Simbologias
     * Descrição
   - * |Login_entre_parenteses|
     * **Login entre parênteses**: indica o usuário a quem o processo foi atribuído na unidade.
   - * |Processo_numero_preto|
     * **Processo com número em preto**: indica que já foi acessado por algum usuário da unidade.
   - * |Processo_núumero_vermelho|
     * **Processo com número em vermelho**: indica que ainda não foi acessado.
   - * |Processo_fundo_preto| 
     * **Processo com fundo preto**: Indica processo sigiloso já acessado por alguém da unidade. Só pode ser visto por usuários com credencial de acesso ao processo sigiloso.
   - * |Processo_fundo_vermelho|
     * **Processo com fundo vermelho**: indica processo sigiloso que ainda não foi acessado.
   - * |Processo_fundo_azul|
     * **Processo com fundo azul**: indica que o processo sigiloso foi acessado e/ou que sofreu alguma ação realizada pelo usuário no login/sessão atual.
   - * |retorno_laranja|
     * Indica que o processo recebido pela unidade tem prazo de Retorno Programado a vencer.
   - * |retorno_vermelho|
     * Indica que o processo recebido pela unidade está com prazo de Retorno Programado expirado (atrasado).
   - * |retorno_azul|
     * Indica que o processo recebido pela unidade com prazo de Retorno Programado teve a devolução cumprida.
   - * |ampulheta_laranja| 
     * Indica que o processo enviado pela unidade com Retorno Programado está aguardando retorno de outra unidade.
   - * |ampulheta_azul| 
     * Indica que o processo enviado pela unidade com Retorno Programado teve o retorno cumprido.
   - * |ampulheta_vermelha|
     * Indica que o processo enviado pela unidade com Retorno Programado está com o prazo de devolução expirado (atrasado).
   - * |alerta|
     * Indica que um documento foi incluído ou assinado no processo.
   - * |anotacoes| 
     * Indica a existência de uma Anotação simples.
   - * |anotocoes_vermelho|
     * Indica a existência de uma Anotação com prioridade.
   - * |marcador|
     * Indica que o processo possui um marcador.
   - * |ponto_controle|
     * Indica que o processo possui um Ponto de Controle.
   - * |controle_prazo_laranja|
     * Indica que o processo possui um Controle de Prazo a vencer.
   - * |controle_prazo_azul| 
     * Indica que o processo possui um Controle de Prazo concluído.
   - * |controle_prazo_vermelho|
     * Indica que o processo possui um Controle de Prazo vencido (atrasado).

.. |Login_entre_parenteses| image:: _static/images/1-IO_icone_Login_entre_parenteses.png
   :align: middle
   :width: 150

.. |Processo_numero_preto| image:: _static/images/1-IO_icone_numero_preto.png
   :align: middle
   :width: 100

.. |Processo_núumero_vermelho| image::  _static/images/1-IO_icone_numero_em_vermelho.png
   :align: middle
   :width: 100

.. |Processo_fundo_preto| image:: _static/images/1-IO_icone_processo_fundo_preto.png
   :align: middle
   :width: 100

.. |Processo_fundo_vermelho| image:: _static/images/1-IO_icone_fundo_vermelho.png
   :align: middle
   :width: 100

.. |Processo_fundo_azul| image:: _static/images/1-IO_icone_fundo_azul.png
   :align: middle
   :width: 100

.. |retorno_laranja| image:: _static/images/1-IO_icone_RP_a_vencer.png
   :align: middle
   :width: 40

.. |retorno_vermelho| image:: _static/images/1-IO_icone_RP_atrasado.png
   :align: middle
   :width: 40

.. |retorno_azul| image:: _static/images/1-IO_icone_RP_concluido.png
   :align: middle
   :width: 40

.. |ampulheta_laranja| image:: _static/images/1-IO_icone_RP_aguardando_retorno.png
   :align: middle
   :width: 40

.. |ampulheta_azul| image:: _static/images/1-IO_icone_retorno_cumprido.png
   :align: middle
   :width: 35

.. |ampulheta_vermelha| image:: _static/images/1-IO_icone_RP_devolucao_atrasada.png
   :align: middle
   :width: 40

.. |alerta| image:: _static/images/1-IO_icone_doc_inluido_ou_assinado.png
   :align: middle
   :width: 40

.. |anotacoes| image:: _static/images/1-IO_icone_Anotacoes.png
   :align: middle
   :width: 40

.. |anotocoes_vermelho| image:: _static/images/1-IO_icone_Anotacoes_com_prioridade.png
   :align: middle
   :width: 40

.. |marcador| image:: _static/images/1-IO_icone_Gerenciar_Marcador.png
   :align: middle
   :width: 40

.. |ponto_controle| image:: _static/images/1-IO_icone__possui_ponto_de_controle.png
   :align: middle
   :width: 40

.. |controle_prazo_laranja| image::  _static/images/1-IO_icone__controle_prazo_a_vencer.png
   :align: middle
   :width: 40

.. |controle_prazo_azul| image:: _static/images/1-IO_icone__controle_prazo_concluido.png
   :align: middle
   :width: 35

.. |controle_prazo_vermelho| image:: _static/images/1-IO_icone__controle_prazo_atrasado.png
   :align: middle
   :width: 40

Tela do Processo
++++++++++++++++

Ao clicar sobre um número de processo, na tela Controle de Processos, o usuário será direcionado a uma nova tela, onde poderá visualizar seu conteúdo.

.. figure:: _static/images/1-IO_tela_do_processo.png

O lado esquerdo da tela mostra o número do processo e a relação de documentos organizados por ordem de produção – é a chamada **“Árvore do Processo”**. Logo abaixo, é apresentada a funcionalidade **“Consultar Andamento”** e, em seguida, são mostrados os **Processos Relacionados**, quando houver. 

À direita da tela são exibidos os ícones de operações possíveis para o processo e, logo abaixo, as unidades nas quais o processo está aberto.

Alguns desses ícones são os mesmos apresentados na tela Controle de Processos, já detalhados no tópico anterior. As demais funcionalidades são as seguintes: 


.. list-table::
   :header-rows: 1
   :widths: 5 35


   - * Ícone
     * Descrição
   - * |Iniciar_processo_relacionado| 
     * **Iniciar processo relacionado:** permite iniciar um novo processo relacionado ao processo em que o usuário está trabalhando no momento. 
   - * |Consultar_Alterar_processo|
     * **Consultar/Alterar processo:** permite consultar ou alterar os dados de cadastro do processo (descrição, interessados, destinatário, nível de acesso), com exceção da data de autuação e do NUP.
   - * |Ciencia|
     * **Ciência:** permite que as unidades registrem ciência do processo, dispensando a necessidade de se produzir um novo documento para esse fim. 
   - * |Favoritos|
     * **Favoritos:** Permite salvar o processo selecionado como “favorito”, podendo-se incluí-lo em grupos de favoritos, a critério da unidade. Os processos favoritos podem ser acessados a partir da opção “Favoritos” no menu Principal.
   - * |Duplicar_processo|
     * **Duplicar processo:** permite duplicar os documentos integrantes de um processo, gerando um novo processo.
   - * |Enviar_correspondência_eletronica|
     * **Enviar correspondência eletrônica:** permite enviar e-mail relacionado ao processo, com ou sem anexos.
   - * |Relacionamentos_do_processo|
     * **Relacionamentos do processo:** permite vincular virtualmente um processo a outro, mantendo os andamentos de forma independente. 
   - * |Ordenar_arvore_do_processo|
     * **Ordenar árvore do processo:** permite que o usuário altere a ordem dos documentos de um processo conforme a necessidade.
   - * |Gerenciar_disponibilizacoes_de_acesso_externo|
     * **Gerenciar disponibilizações de acesso externo**: utilizado para liberar acesso ao conteúdo do processo para um usuário externo. Envia e-mail com link que dará acesso aos documentos do processo. 
   - * |Anexar_processo| 
     * **Anexar processo:** permite anexar um processo a outro. Essa ação não pode ser desfeita. 
   - * |Gerar_arquivo_PDF_do_processo|
     * **Gerar arquivo PDF do processo:** permite gerar um arquivo do processo no formato PDF. O usuário pode escolher quais documentos deseja incluir no arquivo. 
   - * |Gerar_arquivo_ZIP_do_processo|
     * **Gerar arquivo ZIP do processo:** permite gerar um arquivo do processo no formato ZIP. O usuário pode escolher quais documentos deseja incluir no arquivo. 
   - * |Comentarios| 
     * **Comentários:** permite a inclusão de comentários em processos e/ou documentos.
   - * |Controle_de_Processos|
     * **Controle de Processos:** permite que o usuário acesse a tela de controle de processos.
   - * |Pesquisar_no_Processo|
     * **Pesquisar no Processo:** Permite que o usuário realize pesquisas avançadas sobre processos e documentos.


.. |Iniciar_processo_relacionado| image:: _static/images/1-IO_icone__iniciar_processo_relacionado.png
   :align: middle
   :width: 50

.. |Consultar_Alterar_processo| image:: _static/images/1-IO_icone__consultar_alterar_processo.png
   :align: middle
   :width: 50

.. |Ciencia| image::  _static/images/1-IO_icone__ciência.png
   :align: middle
   :width: 50

.. |Favoritos| image:: _static/images/1-IO_icone__favoritos.png
   :align: middle
   :width: 50

.. |Duplicar_processo| image:: _static/images/1-IO_icone__duplicar_processo.png
   :align: middle
   :width: 50

.. |Enviar_correspondência_eletronica| image:: _static/images/1-IO_icone__enviar_correspondencia_eletronica.png
   :align: middle
   :width: 50

.. |Relacionamentos_do_processo| image:: _static/images/1-IO_icone__relacionamentos_processo.png
   :align: middle
   :width: 50

.. |Ordenar_arvore_do_processo| image:: _static/images/1-IO_icone__ordenar_arvore.png
   :align: middle
   :width: 50

.. |Gerenciar_disponibilizacoes_de_acesso_externo| image:: _static/images/1-IO_icone__gerenciar_dispon_acesso_externo.png
   :align: middle
   :width: 50

.. |Anexar_processo| image:: _static/images/1-IO_icone__anexar_processo.png
   :align: middle
   :width: 50

.. |Gerar_arquivo_PDF_do_processo| image:: _static/images/1-IO_icone__gerar_pdf.png
   :align: middle
   :width: 50

.. |Gerar_arquivo_ZIP_do_processo| image:: _static/images/1-IO_icone__gerar_ZIP.png
   :align: middle
   :width: 50

.. |Comentarios| image:: _static/images/1-IO_icone__comentarios.png
   :align: middle
   :width: 50

.. |Controle_de_Processos| image:: _static/images/1-IO_icone_controle_de_processo_tela_processos.png
   :align: middle
   :width: 50

.. |Pesquisar_no_Processo| image:: _static/images/1-IO_icone__pesquisar_processo.png
   :align: middle
   :width: 50


Árvore de Processos
-------------------

Todos os documentos do processo são organizados por ordem de inclusão, na vertical, em um modo de visualização denominado **“Árvore de Documentos do Processo”**.

.. figure:: _static/images/1-IO_tela_arvore_de_processos.png

Processos que, por sua natureza, comportem grande volume de documentos apresentam seus conteúdos aglutinados em pastas, de modo que sempre fiquem visíveis os últimos documentos inseridos. Essa aglutinação não pode ser confundida com “Volume de Processo”, que é típico de processos em suporte físico, não existente em processo eletrônico.

O SEI traz facilidades para cópia do Número Único de Protocolo (NUP). Para isso, deve-se clicar no ícone ao lado do número do processo.

Será possível copiar o número do processo, o número do processo acompanhado do seu assunto ou o seu link de acesso.

.. figure:: _static/images/1-IO_tela_arvore_de_processos_NUP.png



Tela do Documento
+++++++++++++++++

Ao clicar sobre um documento na árvore do processo, ele recebe uma marcação em azul enfatizando o item selecionado.

.. figure:: _static/images/1-IO_tela_do_documento.png

À direita, são mostrados todos os ícones de operações possíveis para documentos e, logo abaixo, é apresentado o corpo do documento.

Alguns desses ícones são os mesmos apresentados na tela do processo, já detalhados no tópico anterior. As demais funcionalidades disponíveis são as seguintes:


.. list-table::
   :widths: 5 50
   :header-rows: 1
  

   - * Ícone
     * Descrição
   - * |Consultar_Alterar_documento|
     * **Consultar/Alterar documento:** permite consultar ou alterar os dados de cadastro do documento (descrição, interessados, destinatário, nível de acesso), com exceção da data de produção e do número do documento.
   - * |Adicionar_aos_favoritos| 
     * **Adicionar aos favoritos:** permite que o usuário defina o documento como modelo, aproveitando seu formato e conteúdo na produção de novos documentos. 
   - * |Imprimir_web| 
     * **Imprimir web**: permite imprimir um documento. Essa funcionalidade está disponível apenas para documentos produzidos no editor de texto do sistema.
   - * |Consultar_assinaturas| 
     * **Consultar assinaturas:** permite consultar as assinaturas de autenticação efetuadas no documento externo digitalizado e inserido no SEI.

.. |Consultar_Alterar_documento| image:: _static/images/1-IO_icone__consultar_alterar_documento.png
   :align: middle
   :width: 50

.. |Adicionar_aos_favoritos| image:: _static/images/1-IO_icone__adionar_aos_favoritos.png
   :align: middle
   :width: 50

.. |Imprimir_web| image:: _static/images/1-IO_icone__imprimir_web.png
   :align: middle
   :width: 50

.. |Consultar_assinaturas| image:: _static/images/1-IO_icone_consultar_assinaturas.png
   :align: middle
   :width: 50


Da mesma forma que ocorre com o número do processo, o SEI tem funcionalidade que permite a geração de cópia do número do documento, para acessá-la clique no ícone ao lado do documento.

Será possível copiar o número do documento, o número do documento acompanhado do seu título ou o seu link de acesso.


.. figure:: _static/images/1-IO_tela_do_documento_numero_doc.png

