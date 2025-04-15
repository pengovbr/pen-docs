Manual de Fluxo do Trâmite
==========================

Introdução
-----------

Este documento visa servir de apoio para a integração de sistemas de processo eletrônico ao canal de comunicação eletrônico do PEN (Processo Eletrônico Nacional).

O canal de comunicação, acima citado, trata-se de um software intermediário que faz o papel de terceiro confiável no trâmite de processos e documentos eletrônicos entre órgãos integrantes. 

Para se integrar à solução, o órgão interessado deve:

1. Inscrever seu sistema de processo eletrônico junto à equipe gestora do sistema;
2. Obter o acesso ao ambiente de homologação;
3. Desenvolver a integração com o catálogo de serviços de interoperabilidade no ambiente de homologação;
4. Obter o acesso ao ambiente de produção.

Este manual é focado no item 3, ou seja, ele considera que o órgão interessado já possui acesso ao ambiente de homologação e deseja iniciar as evoluções em seu sistema.


Cenários de Utilização
----------------------

Nesta seção são descritos os cenários de utilização principais da Solução de interoperabilidade. A explicação é composta do fluxo de chamadas e texto complementar. Os cenários são: 

• Iniciar o envio de Status 0 para Status 1 - "Aguardando o envio dos arquivos digitais";
• Iniciar o envio de um documento avulso; Status 2 - Arquivos digitais recebidos pelo Tramita GOV.BR.
• Enviar os componentes digitais do trâmite;
• Enviar o recibo de conclusão do envio dos componentes digitais;
• Receber metadados e componentes digitais; Status 3 - Metadados recebidos pelo sistema de processo eletrônico destinatário e Status 4 - Arquivos digitais recebidos pelo destinatário

• Assinar e enviar o recibo de conclusão do trâmite; e, Status 5 Recibo de conclusão recebido pelo Tramita GOV.BR
• Receber o recibo de conclusão do trâmite. Status 6 - Recibo de conclusão recebido pelo remetente

1,2,3 ou 4 para o 7 - Trâmite cancelado
3 ou 4 para o 8 - Trâmite recusado. Aguardando ciência do remetente
8 para 9 - Ciência da recusa recebido pelo remetente
1,2,3 ou 4 para o 10 - Trâmite cancelado automaticamente



Iniciar o envio de um processo administrativo 
---------------------------------------------

Quando uma unidade administrativa deseja tramitar um processo administrativo, o SPE remetente se encontra neste cenário. Pré-requisitos: 

• Metadados do processo administrativo a ser tramitado; 

• Identificação da unidade administrativa de destino, bem como seu repositório de estruturas organizacionais. 

A Figura abaixo descreve os serviços que devem ser chamados para execução deste cenário, a partir do endpoin enviarprocesso (/interoperabilidade/rest/v3/tramites/processo). 

.. figure:: _static/images/Fluxo_tramite_Cenario_01-envio_proc_adm.png


Iniciar o envio de um documento avulso
--------------------------------------

Quando uma unidade administrativa deseja tramitar um documento avulso, o SPE remetente encontra-se neste cenário. Pré-requisitos: 

• Metadados do documento avulso a ser tramitado; 

• Identificação das estruturas organizacionais que receberão o artefato. 

A Figura abaixo descreve o fluxo de chamadas para este cenário.

.. figure:: _static/images/Fluxo_tramite_Cenario_02-envio_DocAv.png


Enviar os componentes digitais do trâmite
-----------------------------------------

Após o início do trâmite, o SPE remetente deve enviar para a Solução os componentes digitais do processo ou documento tramitado. Pré-requisitos: 

• Ticket de envio de componentes digitais: número de identificação das pendências de envio, retornado na chamada do serviço que iniciou o trâmite; 

• Conteúdo binário dos componentes: deve ser exatamente o mesmo conteúdo que gerou o hash (espalhamento) que foi informado nos metadados na abertura do trâmite. 

• Número de Registro Eletrônico: número de identificação do trâmite a qual está enviando o componente digital. 

A Figura abaixo descreve o fluxo para envio dos componentes digitais de um trâmite. Note que o mesmo fluxo atende os trâmites de processo administrativo 

.. figure:: _static/images/Fluxo_tramite_Cenario_03-envio_CompDig.png

Enviar o recibo de conclusão do envio dos componentes digitais
--------------------------------------------------------------

Após o remetente enviar todos os componentes digitais referentes ao trâmite para a Solução, a Solução gera o recibo de conclusão do envio dos componentes digitais do processo ou documento tramitado para uma possível consulta pelo remetente. Pré-requisitos: 

• IDT: identificador do trâmite. 

• Ter concluído o envio para a Solução de todos os componentes digitais solicitados. 

A Figura abaixo demonstra o fluxo desse cenário:

.. figure:: _static/images/Fluxo_tramite_Cenario_04-Recibo_conclusao.png

Receber metadados e componentes digitais
----------------------------------------

O SPE, ao consumir o serviço de pendências (vide seção de cenários auxiliares), pode identificar um trâmite novo cujo destinatário está sob seu tratamento. Neste caso, ele deve seguir o descrito neste cenário. Pré-requisitos: 

• IDT: identificador do trâmite que está aguardando solicitação dos metadados por parte do SPE de destino. 

A Figura abaixo demonstra os serviços que devem ser chamados para conclusão deste cenário.

.. figure:: _static/images/Fluxo_tramite_Cenario_05-Receb_Metadados_CompDig.png

Deve ser considerado que, a critério de cada SPE, o momento da solicitação dos metadados e o momento do recebimento dos componentes digitais podem divergir, a fim de permitir a melhor utilização dos recursos de tráfego de rede. Como exemplo, o SPE pode receber os metadados assim que a pendência surge para ele, mas agendar o recebimento dos componentes digitais para período de baixa utilização de rede. 

Assinar e enviar o recibo de conclusão do trâmite 
-------------------------------------------------

Após a conclusão do recebimento dos componentes digitais, o SPE precisa assinar um recibo de conclusão do trâmite. Essa assinatura é feita através do certificado digital que o SPE usa para se comunicar com a Solução de interoperabilidade. Pré-requisitos: 

• IDT do trâmite que está aguardando o recibo de conclusão; 

• Assinatura digital efetuada sobre os dados do recibo (o texto exato a ser assinado pode ser conferido na seção Textos assinados nos recibos). 

A Figura abaixo demonstra o fluxo de chamadas para o envio do recibo de trâmite.

.. figure:: _static/images/Fluxo_tramite_Cenario_06-AssEnv_RecConc.png


Receber o recibo de conclusão do trâmite
----------------------------------------

Após o envio do recibo à Solução, assinado pelo SPE destinatário, o SPE remetente é notificado com uma pendência para receber este recibo. Este é o último passo antes que o trâmite seja dado como concluído dentro da Solução de interoperabilidade. Pré-requisitos: 

• IDT do trâmite na situação correspondente. 

A Figura abaixo demonstra o fluxo de chamadas para o recebimento do recibo de conclusão de trâmite.

.. figure:: _static/images/Fluxo_tramite_Cenario_07-Receber_RecConc.png


Cenários de utilização auxiliares
---------------------------------

Nesta seção serão descritos os cenários de utilização auxiliares, ou seja, que não são essenciais para a efetivação de um trâmite completo, mas que atuam no auxílio para a busca de informações ou na execução de rotinas alternativas. Esses cenários são: 

• Listar pendências; 

• Consultar trâmites; 

• Consultar repositórios e estruturas organizacionais; 

• Cancelar envio de trâmite; 

• Recusar trâmite; 

• Informar ciência da recusa de trâmite; e 

• Retransmitir processo ou documento avulso. 


Listar pendências
-----------------

Todos os SPEs integrantes da Solução precisam ser notificados das suas pendências. Isso se dá através do consumo de um serviço, que retorna todos os trâmites que estão aguardando alguma ação do SPE solicitante, bem como a situação atual deste trâmite, que permite que o SPE identifique o que ele deve fazer em cada pendência. O único pré-requisito para a execução deste fluxo é ser um SPE integrante da Solução. 

A Figura abaixo demonstra a utilização deste serviço. Note que o objetivo é que o SPE chame repetidamente este fluxo.

.. figure:: _static/images/Fluxo_tramite_CenAux_01-ListPend.png


Consultar trâmites
------------------

Os SPEs integrantes, por variados motivos, podem necessitar obter diversas informações (como a situação atual, histórico de mudança de situações, motivo e justificativa de recusa, IDT, NRE, etc.) de trâmites, sejam eles trâmites em execução ou já concluídos. O catálogo fornece um serviço específico para esta finalidade. A única restrição é que, um sistema consumidor deste serviço, só enxerga trâmites em que ele faz o papel de remetente ou destinatário. 

A Figura abaixo demonstra a utilização deste serviço. 

.. figure:: _static/images/Fluxo_tramite_CenAux_02-ConsultTram.png


Consultar repositórios e estruturas organizacionais
---------------------------------------------------

Em vários serviços da Solução, com destaque para os serviços de início de trâmite, os SPEs precisam obter a identificação de uma ou mais estruturas organizacionais. O catálogo de serviços possui 3 itens cuja finalidade é permitir que os sistemas forneçam a seguinte usabilidade para seus usuários:

• Caixa de seleção (combobox) de repositório de estruturas; 

• Com um repositório selecionado, apresentar uma árvore de estruturas organizacionais; 

• Com uma estrutura organizacional selecionada na árvore, permitir que o usuário filtre as estruturas filhas desta, através de parâmetros como nome, sigla e sigla completa. 

A Figura abaixo representa a proposta de usabilidade delineada acima.

.. figure:: _static/images/Fluxo_tramite_CenAux_03-ConsultRepEstrOrg.png


Cancelar envio de trâmite 
-------------------------

Após iniciar um trâmite de documento digital (avulso ou processo), o remetente pode desistir da operação, seja por motivos técnicos (algum hash que não foi calculado corretamente, por exemplo) ou por motivos negociais (a área identificou que o trâmite não deve mais ocorrer). Nesses casos, o SPE remetente deve cancelar o trâmite, e, para isto, os pré-requisitos são:

• possuir o IDT; e 

• o destinatário ainda não ter enviado o recibo assinado para a Solução. 

A Figura abaixo demonstra o fluxo para cancelamento de um trâmite.

.. figure:: _static/images/Fluxo_tramite_CenAux_04-CancTram.png


Recusar trâmite 
---------------

O SPE de destino de um trâmite pode, em determinadas circunstâncias, recusar um trâmite. 
Para isso ele precisa dos seguintes itens: 

• IDT do trâmite que já se encontra sob sua responsabilidade e ainda não foi concluído; 

• Motivo da recusa (uma das opções da enumeração definida pela própria Solução); 

• Justificativa da recusa (texto complementar ao motivo). 

A Figura abaixo demonstra o fluxo para recusa de trâmite.

.. figure:: _static/images/Fluxo_tramite_CenAux_05-RecusTram.png


Informar ciência da Recusa de Trâmite
-------------------------------------

Caso o SPE de destino recuse um trâmite, tal trâmite ficará na situação/status “Aguardando Ciência da Recusa” para o SPE remetente. Desse modo o SPE remetente deve acionar o serviço “cienciaRecusa” para informar sua ciência do trâmite recusado. Para isso ele precisa do seguinte item: 

• IDT do trâmite que está aguardando a recusa (Status “Aguardando Ciência da Recusa”); 

A Figura abaixo demonstra o fluxo do Remetente informando a ciência da recusa de um trâmite recusado pelo Destinatário. 

.. figure:: _static/images/Fluxo_tramite_CenAux_06-Inf_Cien_RecTram.png

A partir do momento em que o trâmite for recusado pelo Destinatário, apenas o Remetente visualizará os dados do trâmite, bem como suas situações/status. O resultado da execução do serviço “cienciaRecusa” é o trâmite com o status de “Recusado pelo Destinatário”.


Retransmitir processo ou documento avulso
-----------------------------------------


Neste cenário de utilização, o remetente deseja retransmitir um documento digital, avulso ou processo, para um determinado destinatário. Pré-requisitos: 

• NRE (Número de Registro Eletrônico) do artefato a tramitar; 

• Identificação da estrutura organizacional de destino. 

A Figura abaixo contém o fluxo para retransmitir o último trâmite. 

.. figure:: _static/images/Fluxo_tramite_CenAux_07-Retransm_ProcDocAv.png


Máquina de estado das situações de trâmite
------------------------------------------

Todos os trâmites da Solução passam por uma máquina definida de estados. Os estados podem ser obtidos através de chamadas ao serviço de consulta de trâmites. A Figura abaixo destaca essa transição. 


.. figure:: _static/images/Fluxo_tramite_MaqEst_01-MaqEstad.png


Textos assinados nos recibos
----------------------------

Esta seção descreve os textos que são assinados nos recibos que trafegam pela Solução. Os textos são especificados também no esquema XSD recibo.xsd, parte integrante da documentação do catálogo de serviços. É importante frisar que a cadeia de bytes assinada deve ser a representação textual do XML sem nenhum espaço em branco extra ou caracteres de quebra de linha. 

• Recibo de conclusão do envio dos componentes digitais: 
   Quem assina? A Solução; 
   Quem pode solicitar? O remetente; 
   Elemento do XSD que especifica o formato: reciboDeEnvio; 
   Exemplo (com quebras de linha):

  <conteudoDoReciboDeEnvio> 
  <reciboDeEnvio> 
  <IDT>1</IDT> 
  <NRE>0000000001342016</NRE> 
  <dataDeRecebimentoDoUltimoComponenteDigital>2016-11-14T17:27:38.159-02:00
  </dataDeRecebimentoDoUltimoComponenteDigital>         
  <hashDoComponenteDigital>U3vAEFQSLIYYzR2ukdrA7GO...</hashDoComponenteDigital> 
  </reciboDeEnvio> 
  <cadeiaDoCertificado>MIIBnzCCAQigAwIBA...</cadeiaDoCertificado> 
  <hashDaAssinatura>eOvUtoaxhTG8RsfGMaUx...</hashDaAssinatura> 
  </conteudoDoReciboDeEnvio> 


* Recibo de conclusão do trâmite:
   Quem assina? O destinatário; 
   Quem recebe? A Solução (e disponibiliza para o remetente); 
   Elemento do XSD que especifica o formato: recibo; 
   Exemplo (com quebras de linha):

  <conteudoDoReciboDeTramite> 
  <recibo> 
  <IDT>1</IDT> 
  <NRE>0000000001342016</NRE> 
  <dataDeRecebimento>2016-11-14T17:27:59-02:00</dataDeRecebimento>            
  <hashDoComponenteDigital>U3vAEFQSLIYYzR2ukdrA7GO...</hashDoComponenteDigital> 
  </recibo> 
  <cadeiaDoCertificado>MIIBnzCCAQigAwIBA...</cadeiaDoCertificado> 
  <hashDaAssinatura>fRwSaPB953...</hashDaAssinatura> 
  </conteudoDoReciboDeTramite>



.. admonition:: Observações

   Alguns valores foram comprimidos para facilitar a leitura, mas devem ser concatenados por completo. O código de exemplo, parte integrante da documentação entregue como pacote de integração, exemplifica essa especificação.
   Quando existirem múltiplos hashes, a ordenação dos mesmos deve ser a alfabética (obtida considerando a codificação UTF-8) das representações em base 64. 


