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
    Abaixo estão listadas as resoluções na mesma ordem em que foram trazidas no documento do teste, cujo está disponível no link: <a href="https://github.com/Miguelnapolitano/teste_tecnico_pecege/blob/main/DesafioPython.pdf">Desafio Python</a>
</p>

## Resoluções

1. **Sobre a query SQL**

    `Query apresentada:`

    ```
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

    ```
        select count(distinct origin_registration_id), new_status, old_status
        from registration_fact
        where new_status in (1, 2, 3, 4, 5, 6)
        order by new_status, old_status
        group_by new_status;
    ```

    **Descrição da query:**
    ```
        Selecione os valores das colunas "new_status" e "old_status" da tabela "registration_fact", cujos valores de
     "new_status" estejam contidos na lista apresentada. Ordene, de forma crescente, primeiro pelo valor de "new_status"
     e caso haja nessecidade, pelo valor de "old_status", depois agrupe o resultado pelos valores iguais de "new_status".
     Por fim, em uma nova coluna traga a contagem dos distintos valores de "origin_registration_id" trazidos na consulta.
    ```

2. **Gráfico de Barras com os tipos dos primeiros 100 pokemons**   

    **Descrição da solução**

    Para resolver a segunda e terceira partes do desafio, criei um script em python para gerar os resultados pedidos. Abaixo está o passo a passo para executá-lo.
    
    **Como executar**

    1 - Faça o clone deste repositório para a sua máquina;  
    2 - Pelo terminal de comando da sua preferência, abra no diretório do projeto;  
    3 - Instale as bibliotecas pokebase, pandas, futures e matplotlib:      
    - `pip install pokebase pandas futures matplotlib`     
    
    4 -execute o script:   
    - `python3 main.py`

    **O que acontecerá?**   
           
    O script irá executar, o que pode demorar entre 4 e 10 minutos devido a todas as 100 requisições na API pokemon. A velocidade de execução irá depender do poder de processamento do computador e da velocidade de conexão com a internet.
    Ao fim da execução duas coisas irão acontecer:   
        1 - Abrirá em seu computador uma janela com o gráfico de barras solicitado no desafio 2;  
        2 - No seu terminal irá imprimir o dataframe referente ao desafio 3;

3. **Datafram com dados dos primeiro 50 pokemons**   

    **Descrição da solução**

    Para resolver este desafio, criei um script em python para gerar os resultados pedidos.   
    Você irá encontrar as informações de como executar acima, na resolução do desafio 2.

2. **Converter de Flask para FastAPI**   

    **Descrição da solução**

    Considerando que o código fornecido é o que está contido como "A Minimal Application" da documentação do Flask. Trouxe como solução o trecho análogo da documentação do FastAPI, sendo assim, a resposta ao desafio está logo abaixo.
     
    ***Rota transformada para FastAPI***

    ```json
        from fastapi import FastAPI    

        app = FastAPI()

        @app.get("/")
        async def root():
            return {"message": "Hello World"}
    ```