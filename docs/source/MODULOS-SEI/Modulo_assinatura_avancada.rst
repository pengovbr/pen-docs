Módulo de Assinatura Avançada (Assinatura Eletrônica do gov.br)
================================================================

O módulo de **Assinatura Avançada** adiciona ao SEI a possibilidade de assinatura e autenticação de documentos utilizando a Assinatura Eletrônica do gov.br, ampliando a validade dos documentos neste sistema.

Manual de Utilização
--------------------

Esta seção tem por objetivo demonstrar as funcionalidades que serão disponibilizadas pelo módulo de Assinatura Avançada do SEI.

Requisitos para Utilização do Módulo
++++++++++++++++++++++++++++++++++++

* Módulo de Login Único instalado;
* Possuir um usuário interno SEI;
* Usuários com CPF cadastrado no menu de usuário SEI (Administração > Usuário > Contatos).
* Usuários com conta gov.br com selo de confiabilidade prata ou ouro.
* Aplicativo **gov.br** instalado no celular. ( `Link para download <https://acesso.gov.br/faq/_perguntasdafaq/oqueemeugovbrmobile.html>`_ )

Utilização do Módulo
++++++++++++++++++++

O módulo de **Assinatura Avançada** introduz a possibilidade de o usuário assinar documentos via **Assinatura Eletrônica do gov.br**, por meio das suas credenciais da Conta **gov.br**, ampliando a validade do documento assinado.

Para realizar a **Assinatura Eletrônica do gov.br**, o usuário deverá acessar o documento e clicar no botão “Assinar Documento”.

.. figure:: _static/images/assinatura_sei.png

Em seguida será aberta a janela **Assinatura de Documentos**. Nessa, o usuário poderá assinar via SEI, com o Certificado Digital ou com **Assinatura Eletrônica do gov.br**.

Para assinatura com **gov.br**, o usuário deverá clicar no botão **"Assinatura GovBr"**.

Preencher os campos indicados em tela e clicar em assinar com **gov.br**:

.. figure:: _static/images/botao_assinar_com_gov.br.png

1) **Órgão Assinante:** selecionar o órgão do assinante;
2) **Assinante:** Indicar o nome do assinante;
3) **Cargo/função:** selecionar o cargo do assinante.

Ao clicar em assinar com **gov.br**, o sistema abrirá uma nova janela solicitando dados de autenticação da Conta gov.br. Após a autenticação, o sistema encaminhará uma mensagem para o **aplicativo gov.br** (que deverá estar instalado no celular do usuário) com um código de autenticação.

Incluir o código de autorização encaminhado ao **aplicativo gov.br** no campo **"Código"** e clicar em **"Autorizar"**.

.. figure:: _static/images/tela_de_inclusao_de_codigo_de_autorizacao.png

Após esta ação, o documento assinado via **gov.br** será atualização com a respsctiva assinatura eletrônica.

.. admonition:: Nota

   Caso o usuário não deseje assinar com a Conta gov.br, selecionar a opção **"Utilizar Assinatura Interna SEI"**.

.. figure:: _static/images/tela_opcao_pela_assinatura_via_Sei.png

Validação de Assinatura Eletrônica
-----------------------------------

Após a assinatura eletrônica, será possível submeter o documento assinado ao serviço de validação de assinaturas eletrônicas do Governo Federal e verificar o status de assinatura eletrônica ICP-Brasil, GOV.BR ou provenientes de acordos internacionais de reconhecimento mútuo.

Acessar o documento assinado eletrônicamente e clicar no link presente seção localizada abaixo das assinaturas eletrônicas do documento;

.. figure:: _static/images/doc_assinado.png

Ao acessar a tela de Conferência de Autenticidade de Documentos, preencher os campos **Código Verificado** e **Código CRC**, com as informações disponibilizadas no documento assinado, seção abaixo da assinatura. Em seguida, copiar o conteúdo do Capcha para o campo apropriado e clicar em **Pesquisar**;


.. figure:: _static/images/tela_conferencia_autenticidade.png

Realizar o download do conteúdo (1) e do certificado digital para para validação externa (2).

.. figure:: _static/images/documentos_download.png

.. admonition:: Nota

   Caso deseje visualizar a integra do documento, será possível por meio da opção em tela (3).

Após o dowload dos documentos, acessar o site do Validador por meio do endereço: https://h-validar.iti.gov.br/ , presente na seção da assinatura que deseja validar;

.. figure:: _static/images/Validador.png

Ao acessar o portal Validar:

1) Clicar no botão *Escolher Arquivo* - selecionar o arquivo com extensão **HTML** baixado anteriormente;
2) Marcar o select box **Assinatura Destacada**. 
3) Ao selecionar essa opção, o botão *Assinatura Destacada Arquivo" - selecionar o arquivo com extensão **p7s** baixado anteriormente;
4) Marcar o select box **Concordo com os termos de uso e política de privacidade.**;
5) Clicar no botão **Validar**.

.. figure:: _static/images/portal_validador.png

Será aberta a tela com a validação do documento, onde será possível:

1) ver o status da assinatura;
2) exportar o relatório para PDF;
3) ver relatório de Conformidade;

.. figure:: _static/images/validacao_documento.png

.. admonition:: Nota

   É importante ressaltar que nenhuma informação ou arquivo são armazenados nos ambientes operacionais do ITI. Os resultados da validação limitam-se exclusivamente a identificar o titular do certificado digital utilizado e confirmar se o documento assinado não sofreu nenhuma adulteração após a assinatura.

