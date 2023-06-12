![image](https://github.com/SamuelSpalla/p2_estrutura_dados/assets/118549226/2b29253a-1699-4b1f-b313-32268fb01b08)

**Curso:** Engenharia de software

**Período:** 3º

**Disciplina:** Estrutura de Dados

**Professor:** [Márcio Alexandre Dias Garrido](https://github.com/marciogarridoLaCop)

**Participante:** Samuel Spalla da Silva 

**PROJETO:**

A Universidade de Vassouras do Campus 1 foi convidada pela prefeitura de Maricá para promover uma solução tecnológica em um dos problemas sociais da cidade, o abandono de animais. Mesmo considerado crime (O abandono de animais é crime, previsto na Lei de Crimes Ambientais - Lei Federal n° 9.605 de 1998), e notório que o índice de abandono vem crescendo a cada ano.
Os alunos do curso de Engenharia de Software foram convocados para a reunião com a secretaria da cidade para entender a demanda solicitada e alguns pontos foram levantados.
A prefeitura precisa de um sistema que possa cadastrar todos os animais por tipo (canino, felino, etc.) e para tanto, é uma premissa que seja possível inserir novos tipos dinamicamente. Precisa ainda, que sejam classificados por idade aproximada, cor, porte e se possui alguma particularidade. No mesmo sistema, deverá ter também um cadastro de pessoas interessadas na adoção, contendo os dados principais de contato e qual espécie teria o interesse de adotar. Ao escolher a espécie, deve também informar se possui alguma preferência do animal. Por fim, no final do mês a prefeitura emitirá um relatório de cruzamento de espécies disponíveis x possíveis candidatos, ou quando um candidato a adoção ligar, que o atendente possa pesquisar se há algum animal com as características informadas.
Os alunos anotaram atentamente a todas as observações, criaram o fluxograma do estudo de caso, e posteriormente o primeiro protótipo em Python, ainda que em modo texto, e sem requisitos gráficos. A ideia foi apenas validar a proposta do programa junto ao solicitante.

**INTERFACE DO TERMINAL:**

![Screenshot_3](https://github.com/SamuelSpalla/p2_estrutura_dados/assets/118549226/4ff339ee-53e3-4b1f-82d0-9932cb10e50e)

Caso deseje cadastrar um animal um cadastro passo a passo sera gerado para você:

![Screenshot_1](https://github.com/SamuelSpalla/p2_estrutura_dados/assets/118549226/fe25950d-4047-4e6a-bfb3-954d22bbac21)

Caso deseje cadastrar uma pessoa será gerado este cadastro:

![Screenshot_2](https://github.com/SamuelSpalla/p2_estrutura_dados/assets/118549226/4f47cfe5-47ba-4a59-b628-8c1114c5ec74)

Caso deseje buscar um animal, você passará por algumas perguntas para definir o filtro de pesquisa desejado e logo após será gerado o resultado da pesquisa:

![Screenshot_5](https://github.com/SamuelSpalla/p2_estrutura_dados/assets/118549226/40657fbd-20ec-43c6-939e-9ef0bec4f117)

O relatório é gerado baseado na espécie preferida de cada pessoa cadastrada:

![Screenshot_6](https://github.com/SamuelSpalla/p2_estrutura_dados/assets/118549226/7f928393-c16f-4b25-b3dc-4e9dd21b0324)


**CÓDIGO**

Primeiro foram criadas as classes Animal e PessoaInteressada:

![Screenshot_7](https://github.com/SamuelSpalla/p2_estrutura_dados/assets/118549226/6908ef0c-6588-4971-910e-ff85a46673f8)

Depois foi criada a classe Prefeitura, onde serão efetuadas todas as operações, abaixo temos os cadastros dos Animais e Pessoas, além da busca:


![Screenshot_8](https://github.com/SamuelSpalla/p2_estrutura_dados/assets/118549226/fb15c659-2a5d-4b53-878f-2a37fb18332e)

Para diminuir a chance de erros, criei uma função para a pessoa que estiver utilizando o código conseguir conferir se o que digitou está correto:

![Screenshot_9](https://github.com/SamuelSpalla/p2_estrutura_dados/assets/118549226/6f27c04a-7173-4ddf-928d-8d022fafdaca)


**CONCLUSÃO**

Foi um trabalho legal de se construir, algumas dificuldades, mas que foram, em sua maioria, superadas. Este é um tema que deve ser mais abordado, pelo bem dos nossos amiguinhos animais, e por isso pretendo futuramente criar uma ferramenta (inicialmente tive a ideia de um bot no discord) para que as pessoas possam adotar novos animais de estimação. Obrigado!



