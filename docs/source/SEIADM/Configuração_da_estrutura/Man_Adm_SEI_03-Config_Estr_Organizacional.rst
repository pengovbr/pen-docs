Configuração da Estrutura Organizacional
========================================

Cadastro das Unidades no SEI
----------------------------

Para iniciar a configuração no SEI é preciso cadastrar suas unidades. Essa etapa é importante pois todas as unidades que fazem parte da estrutura do órgão devem ser cadastradas na ferramenta SEI para que a tramitação dos processos ocorra corretamente. Para isso deve-se seguir o passo a passo a seguir: 

1. **Acessar o Menu Unidades**

O acesso ao menu "Unidades" é feito por meio do menu Administração e clicar na opção Unidades como mostrado na figura abaixo: 

.. image:: images/foto_01.png
   :alt: Foto número 01

No menu "Unidades" é possível visualizar todas as unidades cadastradas para aquele órgão conforme o exemplo a seguir: 

.. image:: images/foto_02.png
   :alt: Foto número 02

2. **Ação Novo**

Ao clicar no ícone “Novo” você terá acesso a uma nova tela com o formulário de cadastramento das unidades. Esse formulário é dividido em seções que serão apresentadas a seguir.

- **Sigla**: trata-se da sigla da unidade. 
- **Nome**: trata-se do nome completo da unidade. 
- **Estrutura Hierárquica**: trata-se da posição que a unidade ocupa na estrutura hierárquica do órgão. Esta seção é dividida em três campos: 

- **Hierarquia**: deve ser selecionada a opção hierárquica do órgão em que a unidade será cadastrada. 
- **Subordinada a**: deve ser selecionada a unidade à qual a nova unidade estará subordinada. 
- **Ordem**: deve ser preenchido o campo da ordem de subordinação.

- **Formato da Numeração**

Campo destinado à configuração do formato do número do processo da unidade. Deve seguir o mesmo padrão numérico adotado pelo órgão por exemplo Número Único de Protocolo (NUP). A configuração do formato do número deve utilizar as variáveis oferecidas pelo SEI. Ao clicar no ícone “Ajuda” ao lado direito do campo será exibida uma lista com todas as variáveis possíveis para composição do número conforme exemplo a seguir: 

.. image:: images/foto_03.png
   :alt: Foto número 03

Note que no SEI as variáveis se caracterizam por estarem entre @. Para montar a estrutura do NUP serão utilizadas variáveis específicas para cada parte do número: 

- **Código da UP**: ``@cod_unidade_sei_05d@`` 

Observe que no código UP supracitado existe a informação “05d” que indica a quantidade de dígitos no campo nesse caso corresponde à 5 dígitos.

- **Sequencial numérico**: ``@seq_anual_cod_unidade_sei_06d@`` 
- **Ano do documento**: ``@ano_4d@`` 
- **Dígito verificador**: ``@dv_mod11_executivo_federal_2d@``

 A máscara do número (sinais como “/” “.” “-“) devem ser inseridas manualmente no momento de compor a numeração. Ao final o campo ficará preenchido da seguinte forma:

   ``@cod_unidade_sei_05d@.@seq_anual_cod_unidade_sei_06d@/@ano_4d@-@dv_mod11_executivo_federal_2d@``

- **Checkboxes**
   
- **Esta unidade pode receber processos**: ao selecionar esta opção a unidade estará disponível para receber processos. Desmarcar esta opção se aplica aos casos em que não é interessante que a unidade receba processo por exemplo no caso da extinção da unidade. 
   - **Esta unidade pode publicar documentos**: ao selecionar esta opção a unidade poderá publicar os documentos selecionados nos veículos de publicação disponíveis no SEI.

- **CORRETOR ORTOGRÁFICO**

Nesta seção é possível selecionar um dos tipos de corretor ortográfico que será utilizado no editor de textos do SEI conforme as opções a seguir: 

- **Nenhum**: nenhum corretor ortográfico será utilizado no editor de textos do SEI. 
- **Nativo do Navegador**: o editor de textos do SEI utilizará o próprio corretor ortográfico do navegador. Sendo assim haverá variação dependendo do navegador utilizado por exemplo Mozilla Firefox Google Chrome Internet Explorer. 
   - **Licenciado**: opção indicada para as instituições que optarem por adquirir uma solução de corretor ortográfico exclusiva. Ao selecionar esta opção será exibido um campo para informar o endereço do servidor do corretor ortográfico adquirido pelo órgão.

- **Timbre**

Esta opção permite realizar a seleção da imagem que servirá como timbre da unidade. O timbre será exibido no topo dos documentos criados na instituição. A imagem pode representar a logo da unidade ou algum outro símbolo sempre respeitando os padrões estabelecidos de redação oficial. Importante! Ressalta-se que o formato de arquivo recomendado para a imagem é o “.png”. Como exemplo utilizaremos o Brasão da República. 

Lembre-se de salvar a operação clicando no botão “Salvar” localizado na parte superior direita da tela!

Montagem/Gestão de Hierarquias
------------------------------

Montagem de Hierarquia no SIP
+++++++++++++++++++++++++++++

Após a criação de todas as unidades no SIP a ferramenta permite realizar a montagem da hierarquia que estrutura a organização. Essa funcionalidade é importante para refletir a subordinação entre as unidades cadastradas além de permitir a utilização de relatórios gerenciais que reflitam a estrutura da organização. A montagem da hierarquia é realizada no SIP conforme os seguintes passos:

1. **Acessar o SIP com perfil de Administrador;**

2. **Acessar a opção “Hierarquias”;**

A imagem a seguir apresenta o menu "Hierarquias": 

.. image:: images/foto_04.png
   :alt: Foto número 04

3. **Criar uma nova hierarquia**:

Ao acessar o menu "Hierarquias" será exibida a lista das hierarquias cadastradas. Para criar uma nova hierarquia clique no ícone "Novo" conforme a imagem a seguir:

.. image:: images/foto_05.png
   :alt: Foto número 05

Ao selecionar a opção “Novo” será aberta uma nova tela para preencher os dados da nova hierarquia que são: 

- **Nome da Hierarquia**: Nome da estrutura hierárquica que está sendo criada. 
- **Sigla**: Sigla da estrutura hierárquica que está sendo criada. 
- **Data de Início**: Data de início de vigência da estrutura hierárquica. 
- **Data de Fim**: Data de fim de vigência da estrutura hierárquica. 
- **Ativa**: Situação atual da hierarquia.

Após o preenchimento desses dados clique no botão “Salvar” localizado na parte superior direita da tela.

Explorando a Funcionalidade "Montar Hierarquias"
++++++++++++++++++++++++++++++++++++++++++++++++

A ferramenta permite realizar a montagem da hierarquia de uma forma dinâmica onde as unidades são arrastadas para suas posições na estrutura organizacional. Veja o exemplo a seguir onde as unidades foram criadas no SIP para compor a estrutura do Ministério fictício XPTO com suas secretarias e departamentos conforme figura abaixo: 

.. image:: images/foto_06.png
   :alt: Foto número 06

Na tela inicial do menu "Montar Hierarquias" selecione a hierarquia que deseja editar. A tela seguinte permitirá arrastar as unidades criadas para suas respectivas posições na estrutura hierárquica conforme figura abaixo: 

.. image:: images/foto_07.png
   :alt: Foto número 07

Os ícones ao lado das unidades permitem a execução de três ações: 

- **Subir Unidade**: permite subir a unidade para o nível hierárquico superior. 
- **Descer Unidade**: permite descer a unidade para o nível hierárquico inferior. 
- **Remover Unidade**: permite remover a unidade da estrutura hierárquica.

Introdução à Configuração dos Dados na Funcionalidade "Gestão de Hierarquia"
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Explorando a Ação "Alterar Unidade" no SEI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A ação "Alterar Unidade" no SEI é utilizada para modificar as informações da unidade já cadastrada. Essa funcionalidade é importante para manter os dados da unidade sempre atualizados. Para alterar os dados de uma unidade siga os passos a seguir:

1. **Acessar o SEI com perfil de Administrador;**

2. **Acessar o menu “Unidades” na opção Administração;**

3. **Selecionar a unidade que deseja alterar;**

4. **Clicar no ícone “Alterar Unidade” conforme a figura abaixo:**

.. image:: images/foto_08.png
   :alt: Foto número 08

A tela seguinte apresentará o formulário para alteração dos dados da unidade que são:

- **Sigla**: trata-se da sigla da unidade.
- **Nome**: trata-se do nome completo da unidade. 
- **Estrutura Hierárquica**: trata-se da posição que a unidade ocupa na estrutura hierárquica do órgão. Esta seção é dividida em três campos:

- **Hierarquia**: deve ser selecionada a