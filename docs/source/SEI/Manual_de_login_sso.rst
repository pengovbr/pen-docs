Manual de login no SEI com Gov.br, Microsoft Entra ou Google Workspace
======================================================================

O que é o login por provedor de identidade
------------------------------------------

O SEI permite ao usuário interno entrar com uma conta de um provedor de identidade, sem usar usuário e senha do próprio sistema. Os provedores disponíveis dependem do que o administrador configurou, entre eles Gov.br, Microsoft Entra e Google Workspace.

Na tela de login, cada provedor aparece como um botão próprio. O botão mostra o logo do provedor ou, quando não há logo, o texto do título configurado, por exemplo ``Entrar com gov.br``.

Ao escolher um provedor, o sistema leva você até a página desse provedor para autenticar. Após autenticar, o provedor devolve você ao SEI já conectado.

Antes de começar
----------------

Você precisa ter uma conta ativa no provedor que vai usar, como a conta Gov.br, a conta Microsoft Entra da sua organização ou a conta Google Workspace.

Seu cadastro no SEI precisa estar vinculado ao mesmo identificador usado pelo provedor, o CPF ou o e-mail, conforme a configuração do administrador. Sem esse vínculo, o provedor autentica, mas o SEI não reconhece o usuário.

Se a tela de login não mostrar o botão do provedor desejado, procure o administrador do sistema. O provedor só aparece depois de cadastrado e associado ao sistema.

Como entrar no SEI por um provedor
----------------------------------

1. Acesse o endereço do SEI. A tela de login é exibida.

A tela de login mostra os campos **Usuário**, **Senha** e **Órgão**, com o botão **ACESSAR**, quando a autenticação por usuário e senha está habilitada, e os botões dos provedores configurados.

.. figure :: _static/images/Cap1_Como_entrar_no_SEI_por_um_provedor.png

Os botões dos provedores ficam abaixo do botão **ACESSAR**, na ordem definida pelo administrador. Cada botão mostra o logo e o título do provedor, como **Entrar com Google**, **Entrar com gov.br** e **Entrar com Microsoft**.

2. Selecione o botão do provedor desejado, por exemplo o botão do Gov.br, do Microsoft Entra ou do Google Workspace.
3. Na página do provedor, informe suas credenciais e confirme o acesso.

Após a autenticação, o provedor devolve você ao SEI e a sessão é aberta.

Quando a autenticação por usuário e senha está desabilitada, a tela mostra apenas os botões dos provedores, sem os campos de usuário e senha.

Como entrar pelo Gov.br no Acesso Externo
-----------------------------------------

O Acesso Externo do SEI, usado por quem recebe acesso a processos sem ser servidor, oferece a entrada pelo Gov.br quando o ambiente habilita essa opção. Microsoft Entra e Google Workspace não aparecem no Acesso Externo.

1. Acesse a tela de **Acesso Externo** do SEI.
2. Selecione o botão do Gov.br.
3. Autentique no Gov.br e confirme o acesso.

.. figure :: _static/images/Cap2_Como_entrar_pelo_Govbr_no_Acesso_Externo.png

Como sair do sistema
--------------------

Use a opção de sair do SEI para encerrar a sessão. Quando o provedor tem um endereço de logout configurado, o sistema redireciona você para esse endereço ao sair.

Encerrar a sessão no SEI nem sempre encerra a sessão no provedor. Para acessos em computadores compartilhados, saia também da conta do provedor.

Se o login não funcionar
------------------------

.. figure :: _static/images/Cap3_Como_sair_do_sistema.png
