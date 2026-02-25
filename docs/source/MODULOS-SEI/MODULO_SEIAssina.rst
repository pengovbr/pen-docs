MANUAL DE UTILIZAÇÃO DO MÓDULO SEIAssina!
=========================================

1. INTRODUÇÃO 
-------------

O Módulo SEIAssina! possibilita que os usuários assinem documentos por meio de assinatura avançada (`Pergunta 1.4 <https://wiki.processoeletronico.gov.br/pt-br/homologacao/MODULOS_SEI/SEI_Assina/Perguntas_Frequentes_FAQ.html#conceito>`__ ) e qualificada (`Pergunta 1.5 <https://wiki.processoeletronico.gov.br/pt-br/homologacao/MODULOS_SEI/SEI_Assina/Perguntas_Frequentes_FAQ.html#conceito>`__). O novo módulo unifica todos os meios de assinatura, elimina o antigo componente Java do SEI e cria padronização entre órgãos. Os modelos de certificado compatíveis com o módulo estão enumerados na `Pergunta 3.1 do FAQ <https://wiki.processoeletronico.gov.br/pt-br/homologacao/MODULOS_SEI/SEI_Assina/Perguntas_Frequentes_FAQ.html#certificado-digital>`__

2. ASSINATURA ELETRÔNICA EM ÚNICO DOCUMENTO
-------------------------------------------

Os novos tipos de assinaturas são acessados por meio da funcionalidade Assinar Documento. De acordo com o tipo do documento, a forma como a tela é exibida para o usuário muda.  

.. figure:: _static/images/02_assinatura_sei.png

2.1 DOCUMENTOS INTERNOS
^^^^^^^^^^^^^^^^^^^^^^^

Se for um documento interno, depois de clicar na funcionalidade “Assinar Documento”, é exibida a tela abaixo. 

.. figure:: _static/images/02_docum_interno.png

Após clicar em Assinatura Eletrônica, uma nova tela exibida comas seguintes informações para o usuário.

1.  **Órgão Assinante:** selecionar o órgão do assinante;
2.	**Assinante:** Indicar o nome do assinante;
3.	**Cargo/função:** selecionar o cargo do assinante.

  **OBS1: Apenas os campos Órgão Assinante e Cargo/função estão habilitados para edição pelo usuário.**

Além das informações acima, também são exibidos os tipos de assinatura habilitados pelo Administrador do SEI no seu órgão. O usuário deve escolher um dos tipos para assinar o documento interno.

.. figure:: _static/images/02-1_assinatura_docum_interno.png
  
  **OBS2: A partir da 1.3.0, essa funcionalidade está disponível para usuários externos.**

2.2 DOCUMENTOS EXTERNOS
^^^^^^^^^^^^^^^^^^^^^^^

Se for um documento externo (um pdf, por exemplo) é exibida a tela com os dados do assinante e tipos de certificados habilitados, depois de clicar no botão “Assinar Documento”. O usuário deve escolher um dos tipos para assinar o documento externo.

.. figure:: _static/images/02-2_docum_externo.png

  **OBS: A partir da 1.4.0, essa funcionalidade está disponível para usuários externos.**


2.3 GOV.BR
^^^^^^^^^^

.. figure:: _static/images/02-3_govbr.png

O módulo possibilita que o usuário realize a assinatura por meio do GOV.BR. Após a autenticação, o sistema encaminhará um SMS ou uma mensagem para o aplicativo gov.br (que deverá estar instalado no celular do usuário) com um código de autenticação.
Incluir o código de autorização encaminhado ao aplicativo gov.br no campo “Código” e clicar em “Autorizar”.

.. figure:: _static/images/02-3_govbr-autorizacao.png

Após esta ação, o documento assinado via gov.br será atualização com a respectiva assinatura eletrônica.

  **OBS1: Na `Pergunta 4.6 <https://wiki.processoeletronico.gov.br/pt-br/homologacao/MODULOS_SEI/SEI_Assina/Perguntas_Frequentes_FAQ.html#assinar-e-validar/>`__ do FAQ é explicado quais usuários podem assinar utilizando o GOV.BR.**


2.4 SERPROID
^^^^^^^^^^^^

.. figure:: _static/images/02-4_serproid.png

O módulo possibilita a assinatura utilizando o `certificado em nuvem emitido <https://wiki.processoeletronico.gov.br/pt-br/homologacao/MODULOS_SEI/SEI_Assina/Perguntas_Frequentes_FAQ.html#conceito/>`__ pelo SERPRO. Para utilizar esse tipo de certificado, o usuário deve escolher a opção SERPROID, aparecerá um modal com o QRCode do SerproID, permitindo que, usando o app do Serpro, possa se fazer a leitura do respectivo código e fazer a validação da assinatura.


.. figure:: _static/images/02-4_serproid-autorizacao.png


Abra o app mobile SerproID, escolha a opção "Autorizar Aplicação” e depois realize a leitura do QRCode exibido na tela do SEI.


.. figure:: _static/images/02-4_serproid-aplicacao.png

Em seguida, escolha o seu certificado em nuvem e utilize a sua biometria para concluir a assinatura do documento desejado.


.. figure:: _static/images/02-4_serproid-certificado.png


  **OBS1: O SERPROID possui a opção “Assinar Arquivo”, na qual o usuário pode realizar upload de um arquivo e realizar a assinatura no próprio aplicativo. Essa opção não é a correta para realizar a assinatura utilizando o certificado em nuvem no SEI.**
  
  **OBS2: O CPF vinculado ao certificado em nuvem deve ser o mesmo que está vinculado ao usuário autenticado no SEI. Caso seja diferente, o sistema informa que não é possível realizar a assinatura.**


2.5 CERTIFICADO A1
^^^^^^^^^^^^^^^^^^

.. figure:: _static/images/02-5_cert-a1.png

Ao optar por essa opção, o sistema abrirá uma pequena tela para que você localize o arquivo do certificado (que deve estar previamente guardado em uma pasta de seu computador). Após localizar o arquivo, deve-se digitar a senha especifica desse certificado e, em seguida, no botão “Assinar”. 























.. figure:: _static/images/02_assinatura_sei.png

`Texto do link <https://domain.invalid/>`__
