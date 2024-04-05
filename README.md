<h1 align="center">
  Teste Técnico - Desenvolver Python - Pecege
</h1>
<h2 align="center">
  Descrição
</h2>
<p align="center">
    Este repositório foi criado com o objetivo de trazer as respostas ao teste técnico para a vaga de Desenvolver Python do Instituto Pecege, além de orientar os recrutadores a como executar os scripts nele contidos.
</p>
<p align="center">
    Abaixo estão listadas as resoluções na mesma ordem em que foram trazidas no documento do teste, cujo está disponível no link: **INSERIR LINK**
</p>


## Resoluções

1. Sobre a query SQL

    `Query apresentada:`

    ```json
        select count(distinct origin_registration_id), new_status, old_status,
        from registration_fact
        where new_status == (1, 2, 3, 4, 5, 6)
        order by new_status
        group_by new_status;
    ```
    `Resposta:`

    Esta não é uma query funcional. Alguns pontos devem ser corrigidos
    
    - A vírgula ao final do "select" causa um erro, pois o interpretador estará esperando um novo nome de coluna para a seleção, porém, inicia-se a instrução "from";
    - O operador "==" não existe no SQL, se o desejo e que os valores de "new_status" trazidos estejam contidos na lista sugerida, deve-se ultilizar o operador "IN";
    - Uma vez que foi definida uma seleção de colunas específicar da tabela, é necessário passálas à cláusula "ORDER BY" para que o interpretador possa ordenar na ordem passada os valores da primeira coluna que serão iguais.


    ***Abaixo, a query corrigida:***

    ```json
        select count(distinct origin_registration_id), new_status, old_status
        from registration_fact
        where new_status in (1, 2, 3, 4, 5, 6)
        order by new_status, old_status
        group_by new_status;
    ```

    **Descrição da query:**
    ```json
        Selecione os valores das colunas "new_status" e "old_status" da tabela "registration_fact", cujos valores de "new_status" estejam contidos na lista apresentada. Ordene, de forma crescente, primeiro pelo valor de "new_status" e caso haja nessecidade, pelo valor de "old_status", depois agrupe o resultado pelos valores iguais de "new_status". Por fim, em uma nova coluna traga a contagem dos distintos valores de "origin_registration_id" trazidos na consulta.
    ```