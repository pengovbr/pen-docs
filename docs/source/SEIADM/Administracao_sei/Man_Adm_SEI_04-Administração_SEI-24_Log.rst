Logs
====

Introdução aos Logs
-------------------

Nos logs são exibidas informações mais técnicas avaliadas pela equipe de TI do órgão ou entidade com o objetivo de identificar problemas de funcionamento ou de configuração no SEI ou em algum dos seus módulos, por exemplo. 

Essa funcionalidade pode ser acessada por meio do menu principal, selecionando a opção “Infra” e clicando em “Log”.

.. admonition:: Nota

   Fique atento! Apenas usuários com a permissão “Informática” têm acesso ao menu “Infra”. Portanto, o usuário que possui apenas o perfil “Administrador” não consegue acessar essa funcionalidade.

Tipos de Logs
-------------

.. figure:: _static/images/04-24_Tipos-de-Logs_Lista_Tipos-de-Log.png

Então vamos nos aprofundar em cada tipo de log:

- **Tipo "Erro"** 

O tipo “Erro”, como o nome já diz, lista os logs relacionados a erros. 

Mas o que seria um erro no SEI?
		
Um erro é um comportamento inadequado do sistema. Nesse caso, os logs viabilizam avaliar a causa desse comportamento.

Destacamos a seguir alguns exemplos de erros identificados por meio da avaliação dos logs: 

1) A recusa do recebimento de um processo por meio do barramento pois a espécie documental não está mapeada no destino. 
2) Processo 00000.000000/0000-00 não possui andamento aberto na unidade MP. 
3) Erro na requisição do serviço de monitoramento de pendências.

A tela do tipo “Erro” é apresentada da seguinte forma:

.. figure:: _static/images/04-24_Tipos-de-Logs_Tela_Tipo-Erro-no-Log.png
	
- **Tipo "Aviso"** 

Os avisos são alertas de algum problema não crítico no sistema, ou seja, correspondem a problemas que não impedem o funcionamento do sistema.

A imagem a seguir demonstra um exemplo de aviso: “Unidade CGSOL não possui endereço cadastrado”.

.. figure:: _static/images/04-24_Tipos-de-Logs_Tela_Tipo-Aviso-no-Log.png

- **Tipo “Informação”** 

Este tipo, como o nome diz, são logs relacionados a mensagens informativas. Essas mensagens não estão relacionadas a erro ou problema de configuração, apenas possuem o objetivo de informar algum comportamento do sistema. 
	
A imagem a seguir demonstra um exemplo.

.. figure:: _static/images/04-24_Tipos-de-Logs_Tela_Tipo-Informação-no-Log.png

- **Tipo “Debug”**

As mensagens de debug são resultado da análise de um depurador, o qual analisa o código de um programa para testar bugs ou erros no código fonte. A equipe de TI do órgão ou da entidade pode configurar que essas mensagens sejam exibidas na interface do SEI. Caso essa configuração não seja realizada, as mensagens de debug não serão exibidas.

.. admonition:: Nota

   Portanto, lembre-se que os logs do SEI não são compostos apenas de erros.
 
 Pesquisando Logs 
----------------

Para acessar essa funcionalidade, é necessário no menu principal selecionar o item “Infra” e clicar em “Log”, que abrirá uma nova tela denominada “Logs”. Essa tela contém campos para pesquisa e uma lista de todos os logs. Os campos são: 

- **Tipo**: Refere-se ao tipo de log que se deseja pesquisar. Como ensinado anteriormente, os tipos podem ser classificados em quatro categorias a saber: erro, aviso, informação e debug. Ressalta-se que este filtro é obrigatório, ou seja, deve ser escolhido um tipo para realização de pesquisa. 

- **Período**: É composto por dois campos do tipo Data/Hora. O preenchimento é facilitado pela seleção da data e da hora desejada por meio do ícone de calendário. 

- **Texto**: Este filtro é de livre preenchimento, sendo que a qualidade da pesquisa está diretamente relacionada à quantidade de informação dada pelo usuário, restringindo o resultado. 

- **IP**: É utilizado para filtrar os logs por meio do endereço IP de quem acessou o sistema. 

Por fim, ao marcar a checkbox “Atualizar automaticamente a cada minuto” localizada após o campo “IP”, a tela é atualizada sem a necessidade de o usuário pressionar a tecla F5. 


Vamos reforçar nosso aprendizado sobre a funcionalidade ensinada com o vídeo a seguir:


Clique [aqui](https://cdn.evg.gov.br/cursos/304_EVG/videos/modulo07video01.mp4) para ver o vídeo.