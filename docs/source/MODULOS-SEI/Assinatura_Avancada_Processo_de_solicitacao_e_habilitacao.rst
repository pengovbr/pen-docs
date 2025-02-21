Solicitação de credenciais para uso do módulo Assinatura Avançada
=================================================================

Introdução
----------

A solicitação de credenciais é uma das etapas necessárias para utilização do módulo **Assinatura Avançada do SEI**. A solicitação é feita junto à Secretaria de Governo Digital do Ministério da Gestão e da Inovação em Serviços Públicos (SGD/MGI) por meio do `Serviço de Integração aos Produtos de Identidade Digital GOV.BR <https://www.gov.br/governodigital/pt-br/estrategias-e-governanca-digital/transformacao-digital/servico-de-integracao-aos-produtos-de-identidade-digital-gov.br>`_.

Neste tutorial, abordaremos os passos necessários para solicitar as credenciais para os ambientes de homologação e produção para a Assinatura Avançada.

1ª ETAPA – Solicitação
----------------------

01. Acessar a página do `Serviço de Integração aos Produtos de Identidade Digital GOV.BR <https://www.gov.br/governodigital/pt-br/estrategias-e-governanca-digital/transformacao-digital/servico-de-integracao-aos-produtos-de-identidade-digital-gov.br>`_.

02. Clicar no botão “Iniciar”

.. figure:: _static/images/AssinAvan_01-Solicitacao_Iniciar.png

03. Fazer login com a conta GOV.BR do agente público (preferencialmente um servidor público efetivo ou comissionado)

.. figure:: _static/images/AssinAvan_01-Solicitacao_Login_GOVBR.png
 
04. Preencher os dados do solicitante e do órgão/entidade

.. figure:: _static/images/AssinAvan_01-Solicitacao_Dados-Org-Solicit.png

05. Preencher os dados do Responsável Negocial e do Responsável Técnico 
 
.. figure:: _static/images/AssinAvan_01-Solicitacao_Dados-Funcionais.png
 
06. Preencher o Questionário, conforme abaixo
 
.. figure:: _static/images/AssinAvan_01-Solicitacao_Questionario.png
 


.. admonition:: Justifique o benefício

   O uso do login gov.br permitirá a assinatura de documentos no SEI com emprego de assinatura avançada, garantindo um maior grau de confiabilidade.

7. Clicar em “Avançar”

8. Preencher os campos sobre o produto a ser integrado

.. figure:: _static/images/AssinAvan_01-Solicitacao_Prod_Interesse_Homologacao_1.png
   

.. admonition:: Nome do Sistema (Homologação)

   "SEI Assinatura Avançada - <Adicionar o Nome do Órgão>"

.. admonition:: Descrição/Objetivo do Sistema

   "O módulo de Assinatura Avançada permite a assinatura de documentos no SEI com emprego de assinatura avançada."

09. Preencher os dados sobre o serviço a ser integrado e em seguida clique em “ADICIONAR DADOS NA TABELA +”
 
.. figure:: _static/images/AssinAvan_01-Solicitacao_Servico.png
 
.. admonition:: Nome do Serviço

   "SEI Assinatura Avançada - <Adicionar o Nome do Órgão>"

.. admonition:: Descreva os benefícios ofertados ao cidadão

   "Possibilitar a assinatura de documentos no SEI com emprego de assinatura avançada."

10. Preencher os campos abaixo conforme indicação:
   
.. figure:: _static/images/AssinAvan_01-Solicitacao_Servico2.png

.. admonition:: Atenção

   No campo “Lista de IPs dos servidores” digite o IP público da instalação do SEI. Em caso de dúvida, consulte a área de TI do seu órgão ou entidade.

.. admonition:: Quais níveis, categorias e selos de confiabilidade

   Para o módulo Assinatura Avançada selecionar:
   Acesso restrito: Prata e Ouro

.. admonition:: Justificativa de acesso ilimitado, restrito ou informação sigilosa

   Os usuários do SEI poderão assinar documentos que contenham dados pessoais/sensíveis.


11. Preencher os campos abaixo conforme indicação:


.. figure:: _static/images/AssinAvan_01-Solicitacao_Chaves_URLs.png

.. admonition:: Atenção

   Orientações sobre como criar um par de chaves PGP podem ser obtidas no `Roteiro de Integração do Login Único <https://acesso.gov.br/roteiro-tecnico/chavepgp.html>`_.

.. admonition:: URL(s) do retorno (Homologação)

   Sugestão de texto para o módulo Assinatura Avançada:
   "https://ENDEREÇO SEI/sei"

.. admonition:: URL única para página inicial do sistema (Homologação) (Máx. 1):

   "http://ENDEREÇO SEI"  ou
   "https://ENDEREÇO SEI"

.. admonition:: Atenção

   Os três campos de datas presentes no final do formulário podem ser preenchidos conforme o exemplo: **Início do desenvolvimento:** data do preenchimento do formulário / **Homologação:** 10 dias após o preenchimento do formulário / **Disponibilização para a sociedadeo órgão:** 20 dias após o preenchimento do formulário.

12. Clicar em "Confirmar dados"

13. Aceitar os termos e clicar em “Enviar solicitação”, aguardando o prazo de até 10 dias úteis para retorno deste primeiro formulário, onde o processo ficará com o status 3 “Análise/Aprovação”

.. figure:: _static/images/AssinAvan_01-Solicitacao_CienciaTermos_EnvioSolicitacao.png

.. figure:: _static/images/AssinAvan_01-Solicitacao_Lista-Status.png


2ª ETAPA - Finalização
----------------------
 
14. Fazer login com a mesma conta GOV.BR que o processo foi iniciado e clicar em “Acompanhamento”.

15. Se houver ocorrido a alteração do status 3 “Análise/Aprovação” para outro, conforme imagem abaixo, clicar em “Responder” para dar andamento no processo. Caso o status não tenha sido alterado, favor aguardar e continuar verificando dentro dos próximos 10 dias úteis.

.. figure:: _static/images/AssinAvan_02-Finalizacao_Lista-Status.png
 
16. Localizar a sessão “Análise do Produto Homologação”

17. Em “Considerações”, copiar os valores “client_id” e “secret”.
 
.. figure:: _static/images/AssinAvan_02-Finalizacao_Analise_Prod_Homol-Consideracoes.png

18. Acessar o arquivo de configuração “ConfiguracaoModAssinaturaAvancada.exemplo.php” e alterar o os campos "Client ID" e "Secret" com as informações obtidas no passo anterior, conforme linhas 43 e 46 da imagem abaixo.

.. figure:: _static/images/AssinAvan_02-cod_ClientID-Secret.png

19. Salvar o arquivo de configuração e gravar um vídeo testando a assinatura de documento utilizando o gov.br, conforme manual de utilização do módulo, disponível no endereço `<https://github.com/pengovbr/mod-sei-assinatura-avancada/blob/master/docs/USAGE.md.>`_

20. Voltar à página do formulário do `Serviço de Integração aos Produtos de Identidade Digital GOV.BR <https://www.gov.br/governodigital/pt-br/estrategias-e-governanca-digital/transformacao-digital/servico-de-integracao-aos-produtos-de-identidade-digital-gov.br>`_ e procurar pelos seguintes campos: 

.. figure:: _static/images/AssinAvan_02-Finalizacao_Chaves_URLs.png

.. admonition:: URL(s) do retorno (Produção)

   "https://ENDEREÇO SEI/sei"

.. admonition:: URL única para página inicial do sistema (Produção)
 
   "http://ENDEREÇO SEI"  ou
   "https://ENDEREÇO SEI"



.. admonition:: Atenção 

   Caso necessário, altere as datas previstas para Início do desenvolvimento, Homologação e Disponibilização para a sociedade.

21. Procurar a seção “Produto(s) de Identidade Digital de interesse” e digitar “SEI Assinatura Avançada - <Adicionar o Nome do Órgão>” em “Nome do Sistema”, conforme imagem abaixo:

.. figure:: _static/images/AssinAvan_02-Finalização_Prod_Interesse_Producao.png

.. admonition:: Descrição/Objetivo do Sistema

   O módulo de Login Externo gov.br permite que cidadãos acessem o ambiente do SEI destinado a usuários externos.

22. Rolar até o fim do formulário e na seção “Enviar dados/Dúvidas” selecionar a opção “Enviar dados de produção”.
 
.. figure:: _static/images//AssinAvan_02-Finalizacao_EnviarDadosProd.png

23. Clicar no botão “Enviar dados de produção”
 
.. figure:: _static/images/AssinAvan_01-Finalizacao_EnviarDadosProd_bot.png

.. figure:: _static/images/AssinAvan_02-Finalizacao_EnvioSolicitacao.png
 
24. Executar novamente os passos 14 a 17 Passos , para localizar o “client_id” e o “secret” de produção, e executar novamente o passo 18, mas desta vez incluindo no arquivo de configuração as credenciais de produção recebidas. Após salvar o arquivo a integração estará concluída.

Orientações gerais: 

• Caso algum dado de produção informado esteja errado, o solicitante receberá um retorno nos e-mails cadastrados no formulário, para correção do problema;
• Caso o processo de solicitação de credenciais esteja parado por mais de 10 dias úteis na mesma etapa, favor enviar um e-mail para o endereço integracaoid@gestao.gov.br, informando o número da solicitação e explicando o ocorrido;
• Em caso de dúvidas técnicas sobre o preenchimento do formulário, favor enviar um e-mail para o endereço: integracao-acesso-govbr@economia.gov.br; 
• Para mais informações, entre em contato pelo telefone 0800 978-9005 ou pela Central de Serviços do PEN, endereço https://portaldeservicos.gestao.gov.br.