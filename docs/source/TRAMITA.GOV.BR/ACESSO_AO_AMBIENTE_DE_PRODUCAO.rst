Acesso ao Ambiente de Produção
==============================

Após a conclusão dos procedimentos em ambiente de homologação, o órgão ou a entidade será autorizado a replicar as configurações de que tratam os capítulos `Configuração da Estrutura <https://manuais.processoeletronico.gov.br/pt_BR/latest/TRAMITA.GOV.BR/CONFIGURACAO_DA_ESTRUTURA.html#configuracoes-da-estrutura>`_ , `Implantação do Módulo de Conexão <https://manuais.processoeletronico.gov.br/pt_BR/latest/TRAMITA.GOV.BR/IMPLANTACAO_DO_MODULO_DE_CONEXAO.html#implantacao-do-modulo-de-conexao>`_ e `Acesso ao Ambiente de Produção <https://manuais.processoeletronico.gov.br/pt_BR/latest/TRAMITA.GOV.BR/ACESSO_AO_AMBIENTE_DE_PRODUCAO.html#acesso-ao-ambiente-de-producao>`_ em ambiente de produção, de modo a minimizar a possibilidade de erros que possam vir a impactar os trâmites na plataforma. Como é no ambiente de Produção que os trâmites reais são realizados, os requisitos estabelecidos em ambiente de homologação são realmente necessários para que a experiência de utilização do Tramita.GOV.BR seja positiva.

O acesso ao Portal de Administração do Tramita.GOV.BR é feito pelo endereço http://gestaopen.processoeletronico.gov.br.

.. admonition:: Notas
   
   Deve-se observar que o presente Manual Técnico versa, em maiores detalhes, sobre as configurações do portal e sobre os procedimentos de teste para validação da integração. As configurações referentes ao módulo de integração ao SEI e às demais soluções de integração devem ser consultadas na documentação específica dos referidos projetos.

   Vide o item `Definição dos Status <https://manuais.processoeletronico.gov.br/pt_BR/latest/TRAMITA.GOV.BR/ACESSO_AO_AMBIENTE_DE_PRODUCAO.html#id3>`_ deste manual para referência completa sobre os diferentes status de tramitação.

**Somente após o cumprimento dos requisitos mínimos descritos nos capítulos anteriores** e validação dos mesmos pela equipe técnica do PEN, será autorizado o acesso ao **ambiente de Produção**, sendo que nesse ambiente, após a realização das configurações no portal do Tramita.GOV.BR, **devem ser realizados novamente TODOS  os  requisitos mínimos**.

**Em produção**, os processos de testes de que trata o Capítulo `Acesso ao Ambiente de Produção <https://manuais.processoeletronico.gov.br/pt_BR/latest/TRAMITA.GOV.BR/ACESSO_AO_AMBIENTE_DE_PRODUCAO.html#acesso-ao-ambiente-de-producao>`_ devem ser enviados para a unidade “Divisão de Gestão de Sistemas de Documentação e Informação – DISIS”, do Ministério da Gestão e da Inovação em Serviços Públicos.

.. admonition:: Nota

   Ao enviar o processo acima citado, é necessário incluir a descrição que se trata de um teste (por exemplo: TESTE – órgão X). Os testes em ambiente de produção são acompanhados por técnicos do PEN. Após o envio do processo de teste, deve-se comunicar, por meio de e-mail institucional processo.eletronico@economia.gov.br, que os testes foram iniciados.

Funcionamento dos Trâmites de Processos ou Documentos
+++++++++++++++++++++++++++++++++++++++++++++++++++++

O trâmite é o envio de um documento avulso, em meio eletrônico, ou de um processo administrativo eletrônico do remetente até o destinatário. O trâmite pode ser concluído de três formas: cancelado, recusado ou com sucesso. Em qualquer situação de conclusão, o trâmite percorre por vários status até a sua conclusão. A compreensão desses status é importante para que os Gestores de Protocolo saibam identificar eventuais problemas no andamento de trâmite no qual o seu órgão/ entidade está envolvido. Os vários status possíveis de um trâmite são explicados nos próximos tópicos.
 
Fluxo de Status
+++++++++++++++

.. figure:: _static/images/Tramite_concluido_com_sucesso.jpg

.. figure:: _static/images/Tramite_Concluido_com_Recusa.jpg

.. figure:: _static/images/Tramite_Concluido_com_Cancelamento.jpg


Definição dos Status
++++++++++++++++++++

O trâmite de um processo administrativo eletrônico e/ou documento avulso, em meio eletrônico, pode passar pelos seguintes “status”:


.. list-table::
   :header-rows: 1

   - * Status
     * Descrição
     * O que significa o status?
     * Onde está o processo?
     * O processo ficou parado nesse status, o que posso fazer?
   - * 1
     * Aguardando o envio dos arquivos digitais
     * As informações gerais (número, descrição, interessado, relação de documentos etc.) foram recebidas pelo Barramento, que está aguardando o envio dos arquivos do processo/documento
     * Sistema de processo administrativo eletrônico remetente
     * O trâmite do processo pode ser cancelado manualmente por usuário do sistema remetente
   - * 2
     * Arquivos digitais recebidos pelo Barramento
     * Os arquivos digitais do processo foram recebidos pelo Barramento e validados quanto à integridade. O Barramento aguarda o Sistema de processo eletrônico destinatário buscar as informações do processo.
     * Tramita.GOV.BR
     * O trâmite do processo pode ser cancelado pelo usuário do sistema remetente. Caso o processo/documento tenha ficado parado no status 2, provavelmente o sistema destinatário está com problema no recebimento. Ente em contato com um dos gestores de protocolo do órgão/entidade destinatário.
   - * 3
     * Metadados recebidos pelo sistema de processo eletrônico destinatário
     * As informações gerais (número, descrição, interessado, relação de documentos etc.) foram recebidas pelo sistema de processo eletrônico destinatário. Aguardando a transferência dos arquivos digitais para o sistema destinatário
     * Tramita.GOV.BR
     * Caso o processo/documento tenha ficado parado no status 3 será necessário verificar se o sistema destinatário está com problema no recebimento. Entre em contato com um dos gestores de protocolo do órgão/entidade destinatário.
   - * 4
     * Arquivos digitais recebidos pelo destinatário
     * Os arquivos digitais foram recebidos pelo sistema de processo eletrônico destinatário. O Barramento aguarda o Sistema destinatário enviar o recibo de conclusão do trâmite.
     * Sistema de processo administrativo eletrônico destinatário
     * Caso o processo/documento tenha ficado parado no status 4 será necessário verificar se o sistema destinatário está com problema no recebimento. Entre em contato com um dos gestores de protocolo do órgão/entidade destinatário.
   - * 5
     * Recibo de conclusão recebido pelo Barramento
     * O sistema de processo eletrônico destinatário validou a integridade do processo e enviou o recibo de conclusão do trâmite para o Barramento.
     * Sistema de processo administrativo eletrônico destinatário
     * Caso o processo esteja parado no status 5 será necessário verificar se o sistema de remetente está indisponível. Entre em contato com um dos gestores de protocolo do órgão/entidade remetente.
   - * 6
     * Recibo de conclusão recebido pelo remetente
     * O recibo de conclusão do trâmite foi recebido pelo sistema de processo eletrônico remetente.
     * Sistema de processo administrativo eletrônico destinatário
     * --
   - * 7
     * Trâmite cancelado
     * O trâmite foi cancelado manualmente por usuário no sistema de processo eletrônico remetente ou por falha na transferência dos dados do processo. Por exemplo: usuário do sistema remetente identifica que o trâmite foi realizado para o destinatário errado e cancela o envio.
     * Sistema de processo administrativo eletrônico remetente
     * --
   - * 8
     * Trâmite recusado. Aguardando ciência do remetente
     * O trâmite foi recusado pelo sistema de processo eletrônico destinatário por alguma falha na validação dos dados recebidos e aguarda ciência do sistema remetente, para desbloqueio do processo. Por exemplo: o formato de arquivo não é aceio pelo sistema destinatário
     * Tramita.GOV.BR
     * Caso o trâmite tenha ficado parado no status 8 será necessário verificar se o sistema remetente está com problema de comunicação com o Barramento.
   - * 9
     * Ciência da recusa recebido pelo remetente
     * O trâmite é cancelado automaticamente pelo barramento após o prazo estabelecido pelos Administradores do Barramento. Apenas os trâmites com status 1,2 e 3 podem ser cancelados automaticamente.
     * Sistema de processo administrativo eletrônico remetente
     * --
   - * 10
     * Trâmite cancelado automaticamente
     * O trâmite é cancelado automaticamente pelo barramento após o prazo estabelecido pelos Administradores do Barramento. Apenas os trâmites com status 1,2 e 3 podem ser cancelados automaticamente.
     * Sistema de processo administrativo eletrônico remetente
     * --