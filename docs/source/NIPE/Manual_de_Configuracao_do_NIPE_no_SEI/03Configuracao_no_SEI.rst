3. Configuração no SEI
----------------------

A configuração da numeração deve ser realizada por um administrador do sistema no menu Administração > Órgãos.


3.1. Máscara de Numeração
+++++++++++++++++++++++++

Para implementar a lógica do NIPE, a máscara de numeração deve ser inserida no campo correspondente do Órgão no SEI. No caso do Estado do Tocantins, utilizando o prefixo fixo 17.
Ao final, o código ficará com a estrutura abaixo, sendo o número 17 uma constante e os demais números construídos por meio de variáveis do sistema:




  **Máscara para o Estado do Tocantins / Municípios do TO:**

  17.@cod_orgao_sei_03d@@cod_unidade_sei_03d@.@seq_anual_cod_unidade_sei_06d@/@ano_4d@-@dv_mod11_executivo_federal_2d@


3.2. Semântica das Tags
+++++++++++++++++++++++

* **17.**: Prefixo fixo inserido manualmente (representa o Identificador de Origem do Tocantins).

* **@cod_orgao_sei_03d@**: Mapeia o campo "Código" do Órgão no SEI (neste caso, o código 137 referente a Palmas). É uma 

* **@cod_unidade_sei_03d@**: Mapeia o código da Unidade Protocolizadora cadastrado na Unidade administrativa.

* **@seq_anual_cod_unidade_sei_06d@**: Garante que a sequência de 7 dígitos seja única por Unidade Protocolizadora e reiniciada anualmente.

* **@ano_4d@**: Ano com 4 dígitos.

* **@dv_mod11_executivo_federal_2d@**: Aplica o algoritmo de cálculo do DV (Mod11) padrão NUP/NIPE.



