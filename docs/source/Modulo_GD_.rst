Módulo de Gestão Documental
===========================

O módulo de Gestão documental do SUPER.GOV.BR traz consigo uma série de funcionalidades que visam contribuir para a gestão arquivística dos processos possibilitando o arquivamento, o desarquivamento, o controle dos prazos de guarda, a avaliação, a devolução para correção de metadados e a geração de listagens de eliminação e recolhimento.

## Manual de Utilização

Essa seção tem por objetivo demonstrar as funcionalidades que serão disponibilizadas pelo módulo de Gestão Documental e também as configurações necessárias para o seu correto funcionamento.

## Configurações do Módulo

Para a adequada utilização do módulo, será necessário configurá-lo conforme as orientações descritas nessa seção.
Abaixo, segue os itens de configuração do módulo.

* [Perfis](#perfis)
* [Unidades de Arquivamento](#configuração-das-unidades-de-arquivamento)
* [Justificativas de Arquivamento e Desarquivamento](#justificativas-de-arquivamento-e-desarquivamento)
* [Modelos de documentos](#modelos-de-documentos)
* [Configurações](#configurações)

___

### Perfis

As funcionalidades do módulo de Gestão Documental estão separadas em dois perfis que possuem recursos específicos e são criados no script de instalação. 
Abaixo são listados os recursos do módulo de Gestão Documental de acordo com cada perfil.

>Atenção: a concessão dos perfis deve ser a primeira etapa de configuração para uso do módulo. As configurações específicas da gestão documental só podem ser realizadas quando da atribuição do perfil “GD Avaliação”.


#### Perfil GD Arquivamento

Possibilita o arquivamento e o desarquivamento de processos na unidade. Além disso possibilita listar as unidades de arquivamento e as justificativas de arquivamento e desarquivamento.

>Atenção: no arquivamento e desarquivamento de processos é gerado um termo na árvore do processo que é automaticamente assinado mediante inserção da senha. Desse modo é necessário que o usuário possua também o perfil básico ou outro que permita a assinatura de documentos.

Recursos

- gd_arquivamento_edicao_concluir
- gd_arquivamento_editar
- gd_arquivamento_historico_listar
- gd_arquivamento_listar
- gd_justificativa_listar
- gd_pendencia_arquivamento_anotar
- gd_pendencia_arquivamento_listar
- gd_procedimento_arquivar
- gd_procedimento_desarquivar
- gd_procedimento_reabrir
- gd_unidade_arquivamento_listar

Menus

- Arquivo da Unidade
- Administração / Gestão Documental / Justificativas de Arquivamento e Desarquivamento / Listar
- Pendências de Arquivamento
- Gestão Documental / Relatórios
- Administração / Gestão Documental / Unidades de Arquivamento / Listar


#### Perfil GD Avaliação

Permite a avaliação dos processos que já cumpriram o prazo de guarda corrente possibilitando também a devolução para correção pela unidade responsável pelo arquivamento. Além disso possibilita a geração de listagens de eliminação e de recolhimento.

Recursos

- gd_arquivamento_avaliar
- gd_arquivamento_devolver
- gd_arquivamento_edicao_concluir
- gd_arquivamento_editar
- gd_arquivamento_eliminacao_enviar
- gd_arquivamento_historico_listar
- gd_arquivamento_recolhimento_enviar
- gd_justificativa_alterar
- gd_justificativa_cadastrar
- gd_justificativa_excluir
- gd_justificativa_listar
- gd_justificativa_visualizar
- gd_listar_eliminacao_anotar
- gd_listar_recolhimento_anotar
- gd_lista_eliminacao_documentos_fisicos_eliminar
- gd_lista_eliminacao_documentos_fisicos_listar
- gd_lista_eliminacao_edicao_concluir
- gd_lista_eliminacao_editar
- gd_lista_eliminacao_eliminar
- gd_lista_eliminacao_listar
- gd_lista_eliminacao_pdf_gerar
- gd_lista_eliminacao_preparacao_excluir
- gd_lista_eliminacao_preparacao_gerar
- gd_lista_eliminacao_preparacao_listar
- gd_lista_eliminacao_preparacao_observar
- gd_lista_eliminacao_procedimento_adicionar
- gd_lista_eliminacao_procedimento_remover
- gd_lista_eliminacao_visualizar
- gd_lista_recolhimento_documentos_fisicos_listar
- gd_lista_recolhimento_documentos_fisicos_recolher
- gd_lista_recolhimento_edicao_concluir
- gd_lista_recolhimento_editar
- gd_lista_recolhimento_listar
- gd_lista_recolhimento_pdf_gerar
- gd_lista_recolhimento_preparacao_excluir
- gd_lista_recolhimento_preparacao_gerar
- gd_lista_recolhimento_preparacao_listar
- gd_lista_recolhimento_preparacao_observar
- gd_lista_recolhimento_procedimento_adicionar
- gd_lista_recolhimento_procedimento_remover
- gd_lista_recolhimento_recolher
- gd_lista_recolhimento_visualizar
- gd_modelo_documento_alterar
- gd_parametro_alterar
- gd_relatorio
- gd_unidade_arquivamento_alterar
- gd_unidade_arquivamento_cadastrar
- gd_unidade_arquivamento_excluir
- gd_unidade_arquivamento_listar
- gd_unidade_arquivamento_visualizar

Menus

- Gestão Documental / Avaliação de Processos
- Administração / Gestão Documental / Justificativas de Arquivamento e Desarquivamento / Novo
- Administração / Gestão Documental / Justificativas de Arquivamento e Desarquivamento / Listar
- Gestão Documental / Listagens de Eliminação / Gestão das Listagens
- Gestão Documental / Listagens de Eliminação / Preparação da Listagem
- Gestão Documental / Listagens de Recolhimento / Gestão das Listagens
- Gestão Documental / Listagens de Recolhimento / Preparação da Listagem
- Administração / Gestão Documental / Modelos de Documento
- Administração / Gestão Documental / Configurações
- Gestão Documental / Relatórios
- Administração / Gestão Documental / Unidades de Arquivamento / Novo
- Administração / Gestão Documental / Unidades de Arquivamento / Listar


### Unidades de Arquivamento 

As unidades do SUPER.GOV.BR configuradas como Unidades de Arquivamento podem arquivar processos. Para cada Unidade de Arquivamento deve ser associada uma Unidade de Avaliação, que ficará responsável por realizar as etapas seguintes da gestão documental, como a revisão da classificação e a geração de listagens de eliminação e de recolhimento.

>Atenção: Como boa prática recomenda-se que todas as unidades do sistema sejam configuradas como Unidade de Arquivamento e que a unidade administrativa responsável pela gestão documental seja configurada como Unidade de Avaliação.

Tal configuração será feita via SUPER.GOV.BR, pelo caminho: Administração > Gestão Documental > Unidades de Arquivamento

#### Opção Novo

Para configurar uma nova unidade de arquivamento, o usuário deverá primeiramente selecionar o nome da unidade que será responsável pela avaliação no campo “Unidade de Avaliação” e, em seguida, inserir uma ou mais unidades de arquivamento, que serão responsáveis pelo arquivamento dos processos.

>Nota: O campo “Unidade de Arquivamento” permite que o usuário inclua tantas unidades quantas as existentes no Órgão.

![](imagens/nova_unidade_de_arquivamento_gif_lançamento_individual1.gif)

Caso o usuário não saiba a grafia da unidade poderá pesquisar as opções disponíveis clicando em “Selecionar Unidades” (ícone Lupa) e selecionar a unidade que deseja.

![](imagens/unidade_arquivamento_pesquisa_unidade.gif)

>Dica: Para vincular mais de uma unidade de arquivamento à unidade de avaliação, basta utilizar a visão “Selecionar Unidades” para marcar as opções desejadas, via checkbox, e clicar em Transportar. Caso o usuário deseje selecionar todas as unidades basta clicar no checkbox existente na lateral esquerda superior da tabela.

Após as seleções, o usuário deverá salvar o registro.

![](imagens/tela_unidade_arquivamento_listar_campos.png)

#### Opção Listar

A opção listar possibilita:

1.	**Criar uma nova unidade de Arquivamento**

Para configurar uma nova unidade de Arquivamento, o usuário deverá clicar no botão Novo e seguir os passos indicados na opção Novo, descritos acima.

2.	**Consultar Unidade de Arquivamento**

A opção consultar unidade de arquivamento permite ao usuário visualizar os metadados relativos ao registro selecionado.

3.	**Alterar Unidade de Arquivamento**

Essa opção permite que o usuário edite o registro da unidade de arquivamento selecionada. Para realizar a edição, o usuário deverá clicar no botão Alterar Unidade de Arquivamento.

Após a edição, clicar em Salvar.

4.	**Excluir Unidade de Arquivamento**

Para excluir uma unidade de arquivamento o usuário deverá clicar em “Excluir Unidade de Arquivamento”, na linha do registro que deseja remover.

Caso o usuário deseje excluir mais de uma Unidade de Arquivamento, deverá selecionar todos os registros desejados, via marcação de checkbox, e em seguida clicar no botão "Excluir", existente na parte superior direita da tela.


### Justificativas de Arquivamento e Desarquivamento

Algumas Justificativas de Arquivamento e Desarquivamento já são cadastradas por meio do script de instalação.

Justificativas de Arquivamento nativas:

			Descrição 						Base legal 
	Inobservância de prazo pelo interessado			Artigo 40, Lei nº 9784/99
	Deferimento do pleito  					Item 2.16 A, Portaria Interministerial nº 1677/2015
	Indeferimento do pleito 				Item 2.16 A, Portaria Interministerial nº 1677/2015
	Desistência ou renúncia do interessado 			Artigo 51, Lei nº 9784/99
	Decisão motivada de autoridade competente 		Item 2.16 C, Portaria Interministerial nº 1677/2015 

Justificativas de Desarquivamento nativas:

			Descrição						Base legal
	Necessidade de continuidade da ação administrativa	Item 2.17, Portaria Interministerial nº 1677/2015 

Para cadastrar uma nova justificativa de arquivamento ou de desarquivamento, o usuário com perfil de Avaliação deverá acessar o SUPER.GOV.BR e seguir o caminho: menu Administração > Gestão Documental > Justificativas de Arquivamento e Desarquivamento.


#### Opção Listar

Por meio da opção Listar o usuário terá acesso à todas as Justificativas cadastradas, podendo realizar as seguintes ações:

 ![](imagens/tela_justificativa_listar_campos_disponiveis.png)

1. **Criar Nova Justificativa**

Para criar uma nova justificativa, o usuário deverá clicar no botão Novo e seguir os passos indicados na opção Novo, descritos abaixo.
 
2. **Consultar Justificativa**

O ícone “Consultar Justificativa” permite ao usuário visualizar os metadados relativos à justificativa de arquivamento ou desarquivamento selecionada.

3. **Alterar Justificativa**

O ícone “alterar Justificativa” dará a possibilidade de o usuário alterar o cadastro de uma justificativa. Ao clicar neste botão, o sistema abrirá uma tela contendo os campos para edição.

 4. **Excluir justificativa**

Para excluir uma Justificativa, o usuário deverá clicar em “Excluir Justificativa”, na linha do registro que deseja remover.

Caso o usuário deseje excluir mais de uma justificativa, deverá selecionar todos os registros desejados, via marcação de checkbox, e em seguida clicar no botão Excluir, existente na parte superior direita da tela.


#### Opção Novo
 
 ![](imagens/justificativas_arquivamento_novo_campos_preenchimento.png)
 
 
1)	**Nome**: Campo obrigatório. Preencher com o nome da justificativa de arquivamento ou desarquivamento. 
2)	**Tipo**: Campo obrigatório. Indicar se a justificativa é de arquivamento ou de desarquivamento.
3)	**Base Legal**: Campo obrigatório. Descrever e/ou citar a base legal que sustenta a justificativa de arquivamento ou desarquivamento.

Após os preenchimentos, o usuário deverá salvar o registro.
 
### Modelos de documentos

Os modelos de documentos utilizados estarão presentes no módulo de forma nativa sendo possível a sua edição, conforme as particularidades do Órgão.

Os modelos de documentos disponíveis no módulo são os seguintes:

- Documento de Arquivamento
- Documento de Desarquivamento
- Listagem de Eliminação
- Documento de Eliminação
- Listagem de Recolhimento
- Documento de Recolhimento

Para editar o conteúdo do modelo de documento, o usuário com perfil de Avaliação deverá acessar, por meio do SUPER.GOV.BR, o submenu “Modelos de Documentos” pelo caminho: menu Administração > Gestão Documental > “Modelos de Documentos”.

Selecionar o tipo de documento, editar o conteúdo e clicar em Salvar.

![](imagens/tela_modelo_documemento_selecao_modelo.png) 
	
### Configurações

O submenu Configurações possibilita que o usuário selecione os tipos de processos e os tipos de documentos que serão utilizados nas ações realizadas pelo módulo.

Para acessar esse submenu, o usuário deverá seguir o caminho: menu Administração > Gestão Documental > Configurações.

>Atenção: Os tipos de processos e tipos de documentos associados na etapa acima devem ser previamente criados por meio do menu “Administração > Tipos de processo” e “Administração > Tipos de documento”, respectivamente.

![](imagens/tela_configuracoes_gestao_documental.gif)

As configurações necessárias são as seguintes:

**Tipo de Documento de Arquivamento**
Documento que será gerado no processo para registrar o seu arquivamento. Recomenda-se a criação do tipo de documento "Termo de Arquivamento".

**Tipo de Documento de Desarquivamento**
Documento que será gerado no processo para registrar o seu desarquivamento. Recomenda-se a criação do tipo de documento “Termo de Desarquivamento”.

**Tipo de Processo de Eliminação**
Processo que será gerado no SUPER.GOV.BR para registrar a Listagem de Eliminação de Documentos. Recomenda-se a criação do tipo de processo “Gestão da Informação: Listagem de Eliminação”.

**Tipo de Documento da Listagem de Eliminação**
Documento que será gerado para listar os processos para eliminação. Recomenda-se a criação do tipo de documento “Listagem de Eliminação de Documentos”.

**Tipo de Documento de Eliminação**
Documento que será gerado para registrar a eliminação. Recomenda-se a criação do tipo de documento “Termo de Eliminação de Documentos”.

**Tipo de Processo de Recolhimento**
Processo que será gerado no SUPER.GOV.BR para registrar a Listagem de Recolhimento de Documentos. Recomenda-se a criação do tipo de processo “Gestão da Informação: Listagem de Recolhimento”.

**Tipo de Documento da Listagem de Recolhimento**
Documento que será gerado para listar os processos para recolhimento. Recomenda-se a criação do tipo de documento “Listagem de Recolhimento de Documentos”.

**Tipo de Documento de Recolhimento**
Documento que será gerado para registrar o recolhimento. Recomenda-se a criação do tipo de documento “Termo de Recolhimento de Documentos”.

Após realizar as configurações, clicar em Salvar.


## Utilização do Módulo

O módulo de Gestão Documental traz incrementos ao Sistema SUPER.GOV.BR que podem ser acessados via entidades:

* Botão Arquivar Processo – Possibilita o arquivamento de processos.
* Botão Desarquivar Processo – possibilita que um processo arquivado seja desarquivado e retorne para a tela de controle de processos.
* Menu Arquivo da Unidade – concentra todos os processos da unidade que foram arquivados e se encontram em fase corrente.
* Menu Pendências de Arquivamento – concentra todos os processos cuja unidade foi a última a concluir e ainda não os arquivou.
* Menu Gestão Documental – possibilita a avaliação dos processos, a devolução para correção e a geração de listagens de eliminação e de recolhimento, conforme a destinação final associada a cada processo.


Para facilitar a navegação nesse documento, abaixo fica disponível tabela contendo links para as entidades supramencionadas, bem como para suas funcionalidades.

* **[Arquivar Processo](#arquivar-processo)**
  * [Tela de Controle de processos](#tela-de-controle-de-processos)
  * [Tela de Visualização do Processo](#tela-de-visualização-do-processo)
  * [Preenchimento do Formulário de Arquivamento de Processo](#preenchimento-do-formulário-de-arquivamento-de-processo)
* **[Desarquivar Processo](#desarquivar-processo)**
  * [Desarquivar via Visão do Processo](#desarquivar-via-visão-do-processo)
  * [Desarquivar via Menu Arquivo da Unidade](#desarquivar-via-menu-arquivo-da-unidade)
  * [Preenchimento do Formulário de Desarquivamento de Processo](#preenchimento-do-formulário-de-desarquivamento-de-processo)
* **[Arquivo da Unidade](#menu-arquivo-da-unidade)**
  * [Pesquisar processos arquivados](#pesquisar-processos-arquivados)
  * [Imprimir uma relação de processos](#imprimir-relação-de-processos)
  * [Desarquivar um ou mais processos](#desarquivar-um-ou-mais-processos)
* **[Pendências de Arquivamento](#menu-pendências-de-arquivamento)**
  * [Pesquisar Processos Concluídos](#pesquisar-processos-concluídos)
  * [Reabrir um processo](#reabrir-processo)
  * [Arquivar um processo](#arquivar-processo)
* **[Gestão Documental](#gestão-documental)**
  * [Avaliação de Processos](#avaliação-de-processos)
    * [Pesquisar Processos para Avaliação](#pesquisar-processos-para-avaliação)
    * [Preparação da Listagem de Eliminação](#preparação-da-listagem-de-eliminação)
    * [Preparação da Listagem de Recolhimento](#preparação-da-listagem-de-recolhimento)
    * [Imprimir](#imprimir)
    * [Devolver para Correção](#devolver-para-correção)
  * [Listagem de Eliminação](#listagem-de-eliminação)
    * [Preparar Listagem de Eliminação](#preparar-listagem-de-eliminação)
      * [Pesquisar Processos para Eliminação](#pesquisar-processos-para-eliminação)
      * [Adicionar observação e/ou justificativa a um processo](#adicionar-observação-eou-justificativa)
      * [Excluir da preparação para Eliminação](#excluir-da-preparação-para-eliminação)
      * [Gerar Listagem de Eliminação](#gerar-listagem-de-eliminação)
      * [Imprimir](#imprimir-1)
    * [Gestão das Listagens de Eliminação](#gestão-das-listagens-de-eliminação)
      * [Visualizar Listagem de Eliminação](#visualizar-listagem-de-eliminação)
      * [Editar a Listagem de Eliminação](#editar-a-listagem-de-eliminação)
      * [Remover Processos da Listagem de Eliminação](#remover-processos-da-listagem-de-eliminação)
      * [Acessar o Processo](#acessar-o-processo)
      * [Pesquisar](#pesquisar)
      * [Imprimir](#imprimir-2)
   * [Listagem de Recolhimento](#listagem-de-recolhimento)
     * [Preparar Listagem de Recolhimento](#preparar-listagem-de-recolhimento)
       * [Pesquisar](#pesquisar-1)
       * [Adicionar observação e/ou justificativa a um processo](#adicionar-observação-eou-justificativa-1)
       * [Excluir da preparação para Recolhimento](#excluir-da-preparação-para-recolhimento)
       * [Gerar Listagem de Recolhimento](#gerar-listagem-de-recolhimento)
       * [Imprimir](#imprimir-3)
     * [Gestão das Listagens de Recolhimento](#gestão-das-listagens-de-recolhimento)
       * [Visualizar Listagem de Recolhimento](#visualizar-listagem-de-recolhimento)
       * [Editar Listagem de Recolhimento](#editar-listagem-de-recolhimento)
       * [Remover Processos da Listagem de Recolhimento](#remover-processos-da-listagem-de-recolhimento)
       * [Acessar o Processo](#acessar-o-processo-1)
       * [Pesquisar](#pesquisar-2)
       * [Imprimir](#imprimir-4)
   * [Relatórios](#relatórios)
     * [Pesquisar](#pesquisar-3)
     * [Imprimir](#imprimir-5)

Abaixo são detalhadas cada uma dessas funcionalidades.

### Arquivar Processo

O botão “Arquivar Processo” será utilizado para indicar que o último ato processual foi realizado, ou seja, tal processo não terá mais movimentações e estará pronto para iniciar a contagem dos prazos de guarda.

Após o clique nesse botão indicado, será necessário preencher o formulário de arquivamento, incluindo a justificativa de arquivamento e inserindo a senha para autenticação da ação.

O botão “Arquivar Processo” está disponível na tela de Controle de Processos e na tela de Visualização de Processos, como pode ser visto abaixo:

#### Tela de Controle de processos
 
![](imagens/conculsao_arquivament_tela_de_controle_processos.png)

Para arquivamento de processos, o usuário deverá selecionar o processo, via marcação de checkbox, e clicar no botão “Arquivar Processo”.

>Nota: Será possível a seleção de mais de um processo para a realização do procedimento de arquivamento, contudo, todos os processos deverão ter a mesma justificativa de arquivamento.

#### Tela de Visualização do Processo

![](imagens/conculsao_arquivament_tela_de_visualizacao_processos.png)

Após todas as tratativas do processo, o usuário poderá direcioná-lo para arquivamento por meio de click no botão “Arquivar Processo”.

#### Preenchimento do Formulário de Arquivamento de Processo

![](imagens/conculsao_arquivament_fomulario_de_preenchimento.png)

O formulário deverá ser preenchido conforme os campos indicados abaixo:

1. **Processo(s)**: campo preenchido automaticamente. Utilizado para indicar um ou mais processos que serão arquivados;
2. **Justificativa**: campo obrigatório. Utilizado para indicar a justificativa do arquivamento. Poderá ser selecionada apenas uma justificativa para arquivamento.
3. **Arquivamento Legado?**: Campo opcional. Funcionalidade utilizada para indicar uma data retroativa de arquivamento do processo. Tal funcionalidade pode ser utilizada para arquivamento de processos concluídos antes da implantação do módulo.

>Nota: no arquivamento legado não é possível selecionar uma data de arquivamento anterior à data do último andamento do processo.

4. **Órgão do Assinante**: Campo obrigatório. Utilizado para indicação do órgão ao qual o usuário responsável pela ação está vinculado.
5. **Assinante**: Campo obrigatório. Utilizado para o registro do nome do usuário responsável pelo arquivamento.
6. **Cargo/Função**: Campo obrigatório. Utilizado para o registro do cargo/função do assinante.
7. **Senha**: Campo obrigatório. Utilizado para a inclusão da senha de autenticação da ação.

Ao clicar em Assinar, o processo receberá uma sinalização indicando que está Arquivado. Além disso, o sistema irá gerar automaticamente um documento de arquivamento assinado eletronicamente pelo responsável pela ação e o incorporará ao processo.

![](imagens/conculsao_arquivamento_tela_apos_procedimento_arquivamento.png) 

A realização do arquivamento impede que novos documentos ou andamentos sejam associados ao processo, sendo possível apenas as seguintes ações:

- Iniciar Processo Relacionado
- Consultar Processo
- Acompanhamento Especial
- Adicionar aos Favoritos
- Anotações
- Gerar Arquivo PDF do Processo
- Gerar Arquivo ZIP do Processo
- Comentários
- Controle de Prazos
- Controle de Processos
- Pesquisar no Processo
- Consultar Histórico de Arquivamento do Processo
- Desarquivar Processo

Após o procedimento de arquivamento, o processo ficará disponível no menu “Arquivo da Unidade” até o cumprimento do prazo corrente. Depois passará a ser apresentado na tela de Avaliação de Processos da Unidade de Avaliação associada.

### Desarquivar Processo

O botão “Desarquivar Processo” será utilizado para o desarquivamento, retornando o processo para a tela de controle de processos.

Após o clique no botão indicado, será necessário preencher o formulário de desarquivamento do processo, incluindo a justificativa de desarquivamento e inserindo a senha para autenticação da ação.

Caso seja necessário, o desarquivamento de um processo poderá ser realizado por meio da tela de visualização do processo ou pelo menu “Arquivo da Unidade”.

#### Desarquivar via Visão do Processo

![](imagens/desarquivamento_visao_processo.png)

#### Desarquivar via Menu Arquivo da Unidade

![](imagens/desarquivamento_visao_menu_arquivo_unidade_individual.png)

Será possível a seleção de mais de um processo para desarquivamento, para tanto, o usuário deverá selecionar todos os processos desejados, via marcação de checkbox, e em seguida clicar no botão Desarquivar, existente na parte superior direita da tela. Poderá ser selecionada apenas uma justificativa para desarquivamento.

>Nota: Para o desarquivamento em lote, todos os processos a serem desarquivados deverão ter a mesma justificativa de desarquivamento.

![](imagens/desarquivamento_visao_menu_arquivo_unidade_lote.png)

#### Preenchimento do Formulário de Desarquivamento de Processo

![](imagens/desarquivamento_formulario_preenchimento.png)

O formulário deverá ser preenchido conforme os campos indicados abaixo:

1)	**Processo(s)**: campo preenchido automaticamente. Utilizado para indicar um ou mais processos que serão desarquivados.
2)	**Justificativa**: campo obrigatório. Utilizado para indicar a justificativa do desarquivamento. Poderá ser selecionada apenas uma justificativa para desarquivamento.
3)	**Órgão do Assinante**: Campo obrigatório. Utilizado para indicação do órgão ao qual o usuário responsável pela ação está vinculado.
4)	**Assinante**: Campo obrigatório. Utilizado para o registro do nome do usuário responsável pelo desarquivamento.
5)	**Cargo/Função**: Campo obrigatório. Utilizado para o registro do cargo/função do responsável pelo desarquivamento.
6)	**Senha**: Campo obrigatório. Utilizado para a inclusão da senha de autenticação da ação.

Ao clicar em Assinar, o sistema irá gerar automaticamente um documento de desarquivamento assinado eletronicamente pelo responsável pela ação e o incorporará ao processo.

### Menu Arquivo da Unidade

Tal menu concentra a lista de todos os processos que foram arquivados pela unidade e se encontram em fase corrente.

#### Pesquisar Processos Arquivados

A pesquisa de processos poderá ser realizada por meio do preenchimento dos campos de filtragem disponíveis em tela e, em seguida, clique no botão Pesquisar.


#### Imprimir Relação de Processos

Será possível imprimir uma relação de processos conforme os filtros de pesquisa aplicados. 

Para realizar a Impressão (seja física ou em PDF), o usuário deverá selecionar os processos, via marcação de checkbox, e clicar em Imprimir.
 
#### Desarquivar um ou mais processos

Os passos para o desarquivamento de processos poderão ser acessados por meio da seção Desarquivar de Processo, existente nesse documento.

### Menu Pendências de Arquivamento

No menu pendências de arquivamento ficam concentrados todos os processos cuja unidade foi a última a concluir e ainda não os arquivou.

#### Pesquisar Processos Concluídos

A pesquisa de processos poderá ser realizada por meio do preenchimento dos campos de filtragem disponíveis em tela e, em seguida, clique no botão Pesquisar.

#### Reabrir Processo

A reabertura consiste em retornar um processo ao status de aberto. Nesta visão, o usuário terá a possibilidade de reabrir um ou mais processos.

>Atenção: Só é possível reabrir processos que estejam apenas concluídos. Processos arquivados precisam ser desarquivados para voltarem a tramitar.

Para reabrir um único processo, o usuário deverá clicar no botão Reabrir Processo, presente na grid do processo que deseja reabrir.

![](imagens/pendencias_arquivamento_reabir_um_processo.png)

Após o clique no botão, o sistema apresentará uma mensagem de confirmação da reabertura. Para concluir a ação, o usuário deverá clicar em “Ok”.
 
Para reabrir mais de um processo, o usuário deverá selecionar todos os processos desejados, via marcação de checkbox, e em seguida clicar no botão Reabrir, existente na parte superior direita da tela.

![](imagens/pendencias_arquivamento_reabir_varios_processos.png)

Após o clique no botão, o sistema apresentará uma mensagem de confirmação da reabertura. Para concluir a ação, o usuário deverá clicar em “Ok”.


#### Arquivar Processo

Nesta visão, o usuário terá a possibilidade de arquivar um ou mais processos.

Para arquivar um único processo, o usuário deverá clicar no botão "Arquivar Processo", presente na grid do processo que deseja arquivar.

![](imagens/arquivo_unidade_arquivar_um_documento.png)

Após o clique no botão, o sistema abrirá o formulário de arquivamento para preenchimento e autenticação. Os passos para o preenchimento deste formulário poderão ser acessados na seção [Preenchimento do Formulário de Desarquivamento de Processo](#preenchimento-do-formulário-de-desarquivamento-de-processo).

Para arquivar mais de um processo, o usuário deverá selecionar todos os processos desejados, via marcação de checkbox, e em seguida clicar no botão "Arquivar", existente na parte superior direita da tela.

>Nota: para o arquivamento em lote, todos os processos a serem arquivados deverão ter a mesma justificativa de arquivamento.

![](imagens/arquivo_unidade_arquivar_lote_documento.png)


### Gestão Documental

O menu Gestão documental poderá ser utilizado pelo usuário lotado na Unidade configurada como de Avaliação que possua o perfil equivalente.

Nesse menu ficarão disponíveis as seguintes opções:

* Avaliação de Processos
* Listagens de Eliminação
* Listagens de Recolhimento
* Relatórios
 
#### Avaliação de Processos

Na opção Avaliação de Processos ficam concentrados todos os processos arquivados pelas respectivas unidades de arquivamento e que cumpriram o prazo de guarda corrente. Nesta visão, o usuário poderá avaliar se as informações relativas aos processos estão adequadas, poderá devolver para a unidade responsável pelo arquivamento realizar correções e poderá enviar para a etapa de preparação da listagem. 

##### Pesquisar Processos para Avaliação

A pesquisa de processos poderá ser realizada por meio do preenchimento dos campos de filtragem disponíveis em tela e, em seguida, clique no botão Pesquisar.
 
##### Preparação da Listagem de Eliminação

Para indicar que um único processo deve ser enviado para preparação da listagem de eliminação, o usuário deverá clicar no botão Preparar Listagem de Eliminação, presente na grid do processo.

![](imagens/avaliacao_de_processos_enviar_destinacao_um_registro.png)

Após o clique no botão, o sistema apresentará uma mensagem de confirmação. Para concluir a ação, o usuário deverá clicar em “Ok”.

Para indicar que mais de um processo deve ser enviado para preparação da listagem de eliminação, o usuário deverá selecionar todos os processos desejados, via marcação de checkbox, e em seguida clicar no botão “Preparar Listagem de Eliminação” existente na parte superior direita da tela.

>Nota: Caso tenha sido selecionado algum processo cuja destinação final não seja Eliminação o módulo irá desconsiderá-lo.

![](imagens/avaliacao_de_processos_enviar_destinacao_lote_registros.png)

Após o clique no botão, o sistema apresentará uma mensagem de confirmação. Para concluir a ação, o usuário deverá clicar em “Ok”.

Os processos enviados para preparação da listagem de eliminação passarão a ser listados no menu “Gestão Documental > Listagens de Eliminação > Preparação da Listagem”.

##### Preparação da Listagem de Recolhimento

Para indicar que um único processo deve ser enviado para preparação da listagem de recolhimento, o usuário deverá clicar no botão Preparar Listagem de Recolhimento, presente na grid do processo.

![](imagens/avaliacao_de_processos_enviar_destinacao_um_registro.png)

Após o clique no botão, o sistema apresentará uma mensagem de confirmação. Para concluir a ação, o usuário deverá clicar em “Ok”.

Para indicar que mais de um processo deve ser enviado para preparação da listagem de recolhimento, o usuário deverá selecionar todos os processos desejados, via marcação de checkbox, e em seguida clicar no botão “Preparar Listagem de Recolhimento” existente na parte superior direita da tela.

>Nota: Caso tenha sido selecionado algum processo cuja destinação final não seja Recolhimento o módulo irá desconsiderá-lo.

![](imagens/avaliacao_de_processos_enviar_destinacao_lote_registros.png)

Após o clique no botão, o sistema apresentará uma mensagem de confirmação. Para concluir a ação, o usuário deverá clicar em “Ok”.

Os processos enviados para preparação da listagem de recolhimento passarão a ser listados no menu “Gestão Documental > Listagens de Recolhimento > Preparação da Listagem”.

##### Imprimir

Nessa visão será possível imprimir uma relação de processos conforme os filtros de pesquisa aplicados. 

Para realizar a Impressão (seja física ou em PDF), o usuário deverá selecionar os processos, via marcação de checkbox, e clicar em Imprimir.

##### Devolver para Correção

Caso o usuário identifique que alguma informação necessita ser corrigida, deverá clicar no botão Devolver para Correção, presente na grid do processo.

![](imagens/avaliacao_de_processos_enviar_correcao_um_registro.png) 

Ao clicar nesse botão, será aberta uma janela para inserção da mensagem de devolução do processo. Após o término do texto, clicar em Devolver.

![](imagens/avaliacao_de_processos_enviar_correcao_justificativa.png)
 
O processo devolvido para correção ficará disponível no Arquivo da Unidade que realizou o arquivamento. Tal processo terá a indicação de que foi devolvido para correção, acompanhado do motivo.

![](imagens/Tela_arquivo_da_unidade_ícone_indicativo_de_correcao.png)

![](imagens/icone_motivo_correção_detalhado.png)

Para realizar a correção o usuário deverá clicar no ícone Consultar/Alterar Processo (1), disponível na grid do processo. Após a correção, o usuário deverá clicar no ícone Concluir Edição (2), disponível na grid do processo.

![](imagens/avaliacao_de_processos_icone_correcao.png) 

>Nota: Ao confirmar a conclusão da Edição os prazos de guarda serão recalculados. Caso ainda esteja pendente o cumprimento de prazo corrente, o processo continuará no Arquivo da Unidade. Caso o processo já tenha cumprido o prazo de guarda corrente, será retornado para a tela de Avaliação de Processos da unidade responsável pela avaliação.

#### Listagem de Eliminação

Nesta opção, o usuário irá criar as listagens de processos elegíveis para eliminação para posterior submissão à CPAD (Comissão Permanente de Avalição de Documentos)

>Nota: A submissão à CPAD não é um procedimento controlado pelo Módulo.

##### Preparar Listagem de Eliminação

###### Pesquisar Processos para Eliminação

A pesquisa poderá ser realizada por meio do preenchimento dos campos de filtragem disponíveis em tela e, em seguida, clique no botão Pesquisar.

###### Gerar Listagem de Eliminação

Para gerar uma listagem de eliminação, o usuário deverá selecionar os processos que deseja que componham a listagem e clicar em Gerar Listagem de Eliminação.

![](imagens/listagem_eliminacao_gerar_listagem.png)

Ao gerar uma listagem, o sistema criará um processo na tela de controle de processos para guardar a listagem criada, que ficará disponível na visão “Gestão das Listagens”, ligada à Listagens de Eliminação, existente no menu Gestão Documental.

###### Excluir da Preparação para Eliminação

Nessa visão, o usuário terá a possibilidade de excluir um ou mais processos da preparação da Listagem de Eliminação.

Para excluir um único processo, o usuário deverá clicar no botão Excluir, presente na grid do processo.

![](imagens/listagem_eliminacao_exclusao_uma_lista.png)

Para excluir mais de um processo, o usuário deverá selecionar todos os processos desejados, via marcação de checkbox, e em seguida clicar no botão Excluir, existente na parte superior direita da tela.

![](imagens/listagem_eliminacao_exclusao_varias_listas.png)

Após a confirmação da exclusão, os processos ficarão disponíveis na tela de Avaliação de Processos, do menu Gestão Documental.

###### Imprimir

Nesta visão será possível imprimir uma relação de processos conforme os filtros de pesquisa aplicados. 

Para realizar a Impressão (seja física ou em PDF), o usuário deverá selecionar os processos, via marcação de checkbox, e clicar em Imprimir.

###### Adicionar observação e/ou justificativa

Para registrar uma observação e/ou justificativa, o usuário deverá clicar no botão "Adicionar observação e/ou justificativa", presente na grid do processo que deseja.

![](imagens/listagem_eliminacao_observacao_justificativa.png)
 
Preencher o campo com a informação desejada e clicar em Salvar.

![](imagens/listagem_eliminacao_inclusao_observacao_justificativa.png)
 
Após esta ação, a informação salva ficará disponível em tela no campo Observações e/ou Justificativas da Grid do processo.


##### Gestão das Listagens de Eliminação

A visão de Gestão das Listagens concentra a relação dos processos de  eliminação, criados na fase “Preparação de Listagem”.

###### Pesquisar

A pesquisa de processos poderá ser realizada por meio do preenchimento dos campos de filtragem disponíveis em tela e, em seguida, clique no botão Pesquisar.
 
###### Imprimir

Nesta visão será possível imprimir uma relação de processos conforme os filtros de pesquisa aplicados. Para realizar a Impressão (seja física ou em PDF), o usuário deverá selecionar os processos, via marcação de checkbox, e clicar em Imprimir.

###### Visualizar Listagem de Eliminação

Para visualizar a listagem de eliminação o usuário deverá clicar no botão "Visualizar Listagem de Eliminação" disponível na grid do processo que deseja.

>Nota: o documento Listagem de Eliminação conforme modelo definido pelo Conarq é criado no processo de eliminação gerado na tela de controle de processos da unidade responsável pela Avaliação.

![](imagens/gestao_das_listagens_visualizao_listagem.png)

Ao acessar a listagem de eliminação, o usuário poderá imprimi-la, via clique no botão imprimir; poderá gerar um PDF, via clique no botão Gerar PDF; ou retornar à tela de gestão de listagens, via clique no botão Cancelar.

![](imagens/gestao_das_listagens_visualizao_listagem_opcoes.png)

###### Editar a Listagem de Eliminação

Conforme a necessidade e/ou deliberações internas, o usuário poderá editar a listagem de eliminação clicando no botão Editar Listagem de Eliminação.

![](imagens/gestao_das_listagens_editar_listagem.png)

Ao realizar esta ação, o sistema irá apresentar na grid do processo botões para adicionar ou remover processos.

![](imagens/gestao_das_listagens_editar_listagem_inclusao_exclusao.png)

###### Adicionar Processos à Listagem de Eliminação

Ao clicar em adicionar, o sistema disponibiliza a lista de todos os processos presentes na tela de Preparação da Listagem de Eliminação. 

Para incluir um ou mais processos, o usuário deverá selecionar, via marcação de checkbox, os processos que deseja incluir na listagem e clicar no botão Adicionar na Listagem de Eliminação.

![](imagens/gestao_das_listagens_editar_listagem_opcao_inclusao.png)

###### Remover Processos da Listagem de Eliminação

Ao clicar em remover, o sistema disponibiliza a lista de todos os processos presentes na listagem de eliminação.

Para excluir um ou mais processos, o usuário deverá selecionar, via marcação de checkbox, os processos que deseja excluir da listagem e clicar no botão Excluir da Listagem de Eliminação.

![](imagens/gestao_das_listagens_editar_listagem_opcao_exclusao.png)

Após realizar as inclusões e/ou exclusões de processos na listagem desejada, o usuário deverá clicar no botão Concluir Edição da Listagem para atualizar a lista com as edições efetuadas. Nesse momento será criada uma nova Listagem de Eliminação no processo de eliminação gerado na tela de controle de processos da unidade de avaliação.

![](imagens/gestao_das_listagens_editar_listagem_inclusao_exclusao_atualizar.png)

###### Acessar o Processo

Para acessar o processo contendo a listagem de eliminação, o usuário deverá clicar sobre o número do processo em questão.

![](imagens/gestao_das_listagens_acessar_listagem.png)


#### Listagem de Recolhimento

Nesta opção, o usuário irá criar as listagens de processos elegíveis para recolhimento.

##### Preparar Listagem de Recolhimento

###### Pesquisar

A pesquisa poderá ser realizada por meio do preenchimento dos campos de filtragem disponíveis em tela e, em seguida, clique no botão Pesquisar.

###### Gerar Listagem de Recolhimento

Para gerar uma listagem de recolhimento, o usuário deverá selecionar os processos que deseja que componham a listagem e clicar em Gerar Listagem de Recolhimento.

![](imagens/listagem_recolhimento_gerar_listagem.png) 

Ao gerar uma listagem, o sistema criará um número de processo para guardar a listagem criada, que ficará disponível na visão “Gestão das Listagens”, ligada à Listagens de Recolhimento, existente no menu Gestão Documental.

###### Excluir da Preparação para Recolhimento

Nesta visão, o usuário terá a possibilidade de excluir um ou mais processos da preparação da Listagem de Recolhimento.

Para excluir um único processo, o usuário deverá clicar no botão Excluir da Preparação para Recolhimento, presente na grid do processo.

![](imagens/listagem_recolhimento_exclusao_uma_lista.png)
 
Para excluir mais de um processo, o usuário deverá selecionar todos os processos desejados, via marcação de checkbox, e em seguida clicar no botão Excluir, existente na parte superior direita da tela.

![](imagens/listagem_recolhimento_exclusao_varias_listas.png)

Após a confirmação da exclusão, os processos ficarão disponíveis na visão de Avaliação de Processos, do menu Gestão Documental

###### Imprimir

Nesta visão será possível imprimir uma relação de processos conforme os filtros de pesquisa aplicados. 

Para realizar a Impressão (seja física ou em PDF), o usuário deverá selecionar os processos, via marcação de checkbox, e clicar em Imprimir.


###### Adicionar observação e/ou justificativa

Para registrar uma observação e/ou justificativa, o usuário deverá clicar no botão Adicionar observação e/ou justificativa, presente na grid do processo que deseja.

![](imagens/listagem_recolhimento_observacao_justificativa.png)

Preencher o campo com a informação desejada e clicar em Salvar.

![](imagens/listagem_recolhimento_inclusao_observacao_justificativa.png)
 
Após esta ação, a informação salva ficará disponível em tela no campo Observações e/ou Justificativas da Grid do processo.


##### Gestão das Listagens de Recolhimento

A visão de Gestão das Listagens concentra a relação dos processos de Recolhimento, criados na fase “Preparação de Listagem”.

###### Pesquisar

A pesquisa de processos poderá ser realizada por meio do preenchimento dos campos de filtragem disponíveis em tela e, em seguida, clique no botão Pesquisar.

###### Imprimir

Nesta visão será possível imprimir uma relação de processos conforme os filtros de pesquisa aplicados. 

Para realizar a Impressão (seja física ou em PDF), o usuário deverá selecionar os processos, via marcação de checkbox, e clicar em Imprimir.

###### Visualizar Listagem de Recolhimento

Para visualizar a listagem de recolhimento o usuário deverá clicar no botão "Visualizar Listagem", disponível na grid do processo que deseja.

![](imagens/recolhimento_gestao_das_listagens_visualizao_listagem.png)
 
Ao acessar a listagem de recolhimento, o usuário poderá imprimi-la, via clique no botão imprimir; poderá gerar um PDF, via clique no botão Gerar PDF; ou retornar a tela de gestão de listagens, via clique no botão Cancelar.

![](imagens/recolhimento_gestao_das_listagens_visualizacao_listagem_opcoes.png)


###### Editar Listagem de Recolhimento

Conforme a necessidade e/ou deliberações internas, o usuário poderá editar a listagem de recolhimento clicando no botão Editar Listagem de Recolhimento.
 
![](imagens/recolhimento_gestao_das_listagens_editar_listagem.png)

Ao realizar esta ação, o sistema irá deixar disponível na grid do processo um botão para adicionar processos e outro para remover processos.

![](imagens/recolhimento_gestao_das_listagens_editar_listagem_inclusao_exclusao.png)

###### Adicionar Processos à Listagem de Recolhimento

Ao clicar em adicionar, o sistema disponibiliza a lista de todos os processos presentes na tela de Preparação da Listagem de Recolhimento.

Para incluir um ou mais processos, o usuário deverá selecionar, via marcação de *checkbox*, os processos que deseja incluir na listagem e clicar no botão Adicionar na Listagem de Recolhimento.

![](imagens/recolhimento_gestao_das_listagens_editar_listagem_opcao_inclusao.png)
 
###### Remover Processos da Listagem de Recolhimento

Ao clicar em remover, o sistema disponibiliza a lista de todos os processos presentes na listagem de recolhimento.

Para excluir um ou mais processos, o usuário deverá selecionar, via marcação de *checkbox*, os processos que deseja excluir da listagem e clicar no botão Excluir da Listagem de Recolhimento.
 
![](imagens/recolhimento_gestao_das_listagens_editar_listagem_opcao_exclusao.png)

Após realizar as inclusões e/ou exclusões de processos na listagem desejada, o usuário deverá clicar no botão Concluir Edição da Listagem para atualizar a lista com as edições efetuadas. Nesse momento será criada uma nova Listagem de Recolhimento no processo de recolhimento gerado na tela de controle de processos da unidade de avaliação.

![](imagens/recolhimento_gestao_das_listagens_editar_listagem_inclusao_exclusao_atualizar.png)

###### Acessar o Processo

Para acessar o processo contendo a listagem de recolhimento, o usuário deverá clicar sobre o número do processo em questão.

![](imagens/recolhimento_gestao_das_listagens_acessar_listagem.png)


#### Relatórios

Nessa visão o usuário terá um panorama geral dos processos arquivados pelo Módulo.

Na parte inferior da tela existem contadores que auxiliam o usuário.

![](imagens/relatorios_contadores.png)


##### Pesquisar

A pesquisa de processos poderá ser realizada por meio do preenchimento dos campos de filtragem disponíveis em tela e, em seguida, clique no botão Pesquisar.
 

##### Imprimir

Nessa visão será possível imprimir uma relação de processos conforme os filtros de pesquisa aplicados.

Para realizar a Impressão (seja física ou em PDF), o usuário deverá selecionar os processos, via marcação de checkbox, e clicar em Imprimir.


 
