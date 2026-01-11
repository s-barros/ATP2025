# Universidade do Minho
### Licenciatura em Engenharia Biomédica
### Algoritmos e Técnicas de Programação
#
#
#
# Relatório do Projeto de Programação
### Simulação de uma Clínica Médica
### Grupo 28
#
#
#### Autores: Isadora de Carvalho (A109413); 
#### 	       Milaine Renata António Oliveira (A112875); 
#### 	       Sara Belo Leal de Barros (A111690).
#
#



### 1.	Introdução


#### 1.1 Contextualização

Comummente, podemos ouvir e ver que os serviços de saúde disponíveis em alguns países, como Portugal, não satisfazem as necessidades da comunidade, ocorrendo falhas prejudiciais ao paciente, que podem mesmo conduzir ao seu falecimento. É disso exemplo a falta de médicos obstetras em muitos hospitais espalhados pelo país. Nesse contexto, algumas grávidas acabam por ter o bebé sem estarem acompanhadas por um especialista, aumentando a probabilidade de óbito dos dois utentes.


#### 1.2 Motivação

O desenvolvimento de aplicações de simulação permite obter resultados capazes de melhorar as condições de funcionamento das unidades de saúde, facilitando a gestão dos recursos, bem como o estudo e planificação das mesmas unidades, ao mesmo tempo que evita problemas com o tempo de espera, a qualidade do serviço médico e os custos, entre outros.


#### 1.3 Objetivos 

No âmbito desta unidade curricular desenvolvemos um projeto que tem como objetivo ajudar a comunidade médica ao:

- > Desenvolver uma aplicação modular em Python; 
- > Implementar um sistema de autenticação com login e registo de utilizadores; 
- > Simular o funcionamento interno de uma clínica médica; 
- > Permitir a configuração de parâmetros de simulação; 
- > Armazenar dados de forma persistente; 
- > Representar graficamente os resultados obtidos. 

Este projeto visa aplicar os conceitos fundamentais de programação aprendidos ao longo do semestre, incluindo modelação, estruturas de controlo, manipulação de ficheiros e desenvolvimento de interfaces gráficas. 


#### 1.4. Descrição do trabalho

A aplicação desenvolvida permite simular o atendimento médico numa clínica fictícia, recolhendo dados relevantes sobre o seu funcionamento, de forma que o utilizador possa alterar as condições de funcionamento, como, por exemplo, o número de médicos e rececionistas.


#### 1.5 Organização do relatório 

Para além da secção que já foi introdutória até agora apresentada, o relatório está dividido nas seguintes partes:

2. Material utilizado no desenvolvimento do projeto

3. A Aplicação

   3.1 Descrição geral da aplicação
   3.2 Descrição do funcionamento da simulação
   3.3 Resultados da simulação
   3.4 Ficheiros que constituem o projeto
   3.5 Descrição dos ficheiros utilizados
   3.6 Descrição dos parâmetros usados na simulação
   3.7 Dificuldades encontradas e estratégias de superação

4. Conclusões e trabalho futuro

### 2.	Material utilizado no desenvolvimento do projeto 


Este projeto teve por base o material disponibilizado pelo professor e tudo aquilo que foi desenvolvido e trabalhado durante o percurso curricular. Foi desenvolvido em Python no VSCode, utilizando as bibliotecas numpy, matplotlib e simpleGUI.


### 3.	A Aplicação


#### 3.1 Descrição geral da aplicação

A aplicação desenvolvida simula uma clínica médica, na qual o utilizador pode autenticar-se, configurar os respetivos recursos e executar uma simulação da mesma gerada a partir de dados definidos pelo próprio. 
Quando o utilizador abrir pela primeira vez a aplicação, será recebido com uma janela de login na qual poderá registar-se ou, se já estiver registado, autenticar-se. Quando concluir essa etapa, a janela de login fechar-se-á automaticamente e abrir-se-á uma nova janela na qual o utilizador poderá escolher fazer uma nova simulação ou consultar o seu histórico. Se decidir fazer uma nova simulação, poderá fornecer ao programa todos os dados que entender para que a sua clínica funcione da maneira desejada. Durante a simulação, são considerados diferentes tipos de médicos e tempos associados ao atendimento, permitindo obter estatísticas como o tamanho médio e máximo das filas de espera, a duração média do atendimento e das consultas, o tempo médio de espera para o atendimento (quer da triagem quer da consulta), a taxa de ocupação média dos médicos e dos rececionistas, entre outras. No final da simulação o utilizador terá acesso a essas estatísticas bem como aos gráficos da evolução dos tamanhos das filas de espera e da taxa de ocupação dos médicos e dos rececionistas ao longo do tempo.



#### 3.2 Descrição do funcionamento da simulação

No início, o utilizador opta por fazer uma simulação clínica e insere a quantidade de funcionários que a sua clínica terá, bem como o tempo da simulação. Quando esses dados forem fornecidos, a simulação começará automaticamente. 
No momento da simulação o programa deverá gerar uma lista de tempos de chegada que, de seguida, será utilizada para gerar uma lista de eventos de chegada, na qual cada evento é constituído por um tempo, o tipo de evento (se o doente está a chegar, se foi atendido ou se está de saída) e os dados do paciente, que serão os dados presentes no ficheiro pessoas.json. No final, depois de todos os médicos e rececionistas terem sido contabilizados e inseridos no sistema, e terminada a lista de eventos, a simulação em si poderá começar. Durante o tempo de simulação o programa estará a retirar pacientes da lista de eventos, a colocá-los na fila de espera para que sejam atendidos e a verificar se existe algum(a) rececionista disponível. No caso de haver rececionistas disponíveis, o paciente deverá ser atendido de acordo com a sua idade – dando-se prioridade aos pacientes com idade superior a 65 anos –, sendo depois redirecionado para a fila de espera da especialidade correspondente ao seu problema, tendo esta sido gerada por meio de uma função de caráter probabilístico e aleatório. Se houver médicos disponíveis, o doente deverá ser atendido e, no final da consulta, sair. O atendimento dos doentes deixou de ser feito com base na sua idade, passando a ser determinado pela gravidade do seu problema.
O programa deverá seguir esta lógica de eventos até que o tempo de simulação termine.


#### 3.3 Resultados da simulação

Para além de todos os acontecimentos registados ao longo da simulação, o utilizador, no final da mesma, deverá ter acesso a todas as estatísticas da simulação no terminal e aos gráficos da evolução dos tamanhos das filas de espera e da taxa de ocupação dos médicos e dos rececionistas ao longo do tempo, em janelas separadas.


#### 3.4 Ficheiros que constituem o projeto
 
O projeto é constituído pelos seguintes ficheiros: 

-> `clinic_login.py` 

->`clinic_registo.py` 

->`clinicApp.py` 

->`faux_clinic.py` 

->`clinic_dados_simulacao.py` 

->`simula_graf_test_final.py` 

->`clinic_historico.json` 

->`clinic_users.json`

->`pessoas.json`

Cada ficheiro desempenha um papel fundamental no funcionamento global da aplicação. 




#### 3.5 Descrição dos ficheiros utilizados

-> Login (`clinic_login.py`) 
Este ficheiro é responsável pela autenticação dos utilizadores. Através de uma interface gráfica, este introduz o nome de utilizador e a palavra-passe. O programa verifica se as credenciais correspondem a um utilizador registado, permitindo ou não o acesso à aplicação. Se o utilizador estiver registado e as credenciais inseridas estiverem corretas, deverá passar a ter acesso a outra parte da aplicação.
Este processo garante que apenas utilizadores autenticados possam aceder às funcionalidades da clínica simulada. 

-> Registo (`clinic_registo.py`) 
Caso o utilizador não esteja registado, o ficheiro de registo permite a criação de novos utilizadores. Os dados introduzidos são validados e armazenados, evitando a criação de utilizadores iguais. Este módulo complementa o sistema de login, assegurando a gestão correta dos utilizadores. 

-> App Principal (`clinicApp.py`) 
Este ficheiro corresponde ao núcleo da aplicação. É responsável por coordenar o fluxo do programa, chamando os restantes módulos conforme necessário. Neste módulo são definidas as opções principais da aplicação, bem como a ligação entre a interface gráfica e a lógica da simulação.

-> Funções Auxiliares (`faux_clinic.py`) 
O ficheiro `faux_clinic.py` contém todas as funções que são utilizadas em todos os módulos relacionados com a parte gráfica da aplicação. 

-> Gestão de Dados da Simulação (`clinic_dados_simulacao.py`) 
Este ficheiro é responsável por recolher e organizar os dados gerados durante a simulação. Quando um utilizador deseja fazer uma simulação, este ficheiro fará com que seja possível a formação de uma janela onde poderá especificar os dados a serem usados na simulação, como, por exemplo, o número de médicos e de rececionistas presentes na clínica e o tempo de duração da simulação.
 
-> Simulação (`simula_graf_test_final.py`) 
Este ficheiro é o responsável por tudo o que está envolvido no ato da simulação, desde as funções até ao código responsável pela simulação em si.

-> Histórico de Simulações (`clinic_historico.json`) 
O histórico de simulações é um ficheiro json que tem como função armazenar todos os dados que o utilizador já forneceu para fazer cada simulação. Os conteúdos desse ficheiro estarão disponíveis para consulta durante a utilização da aplicação.

-> Dados pessoais ( `pessoas.json`)
Este ficheiro foi fornecido pelo professor e é um ficheiro json no qual estão armazenadas centenas (ou milhares) de dados que estão a ser utilizados na parte da simulação, de forma a permitir ao utilizador ter o resultado mais próximo possível da realidade.

-> Utilizadores ( `clinic_users.json`)
O ficheiro `clinic_users.json` é um ficheiro json no qual estão armazenados todos os utilizadores criados na aplicação. No momento do login, este ficheiro será consultado pela aplicação de forma a verificar se as credenciais que o utilizador inseriu são válidas e se realmente existem.


#### 3.6 Descrição dos parâmetros utilizados na simulação

Os nomes dos parâmetros apresentados estão de acordo com aquilo que está no ficheiro de simulação.

->TEMPO_MEDIO_ATENDIMENTO: tempo médio que demora o atendimento de um paciente;

->DISTRIBUICAO_TEMPO_ATENDIMENTO: tipo de distribuição utilizada para o atendimento de pacientes;

->TEMPO_MEDIO_CONSULTA: tempo médio que demora uma consulta;

->DISTRIBUICAO_TEMPO_CONSULTA: tipo de distribuição utilizada para as consultas de pacientes;

->RECEPCIONISTAS: número de rececionistas que estão presentes na clínica;

->MEDICOS: 

		- cardiologia: número de médicos de cardiologia presentes na clínica;
    
		- ortopedia: número de médicos de ortopedia presentes na clínica;
    
		- clinica geral: número de médicos de clinica geral presentes na clínica;
    
		- dermatologia: número de médicos de dermatologia presentes na clínica;
    
		- pediatria: número de médicos de pediatria presentes na clínica;
    
->TEMPO_SIMULACAO: tempo de duração da simulação.




#### 3.7 Dificuldades Encontradas e Estratégias de Superação

Ao longo do tempo de desenvolvimento deste projeto foram sendo encontradas inúmeras dificuldades, tendo a mais relevante sido a integração das diferentes partes do código desenvolvidas por cada elemento do grupo, em especial a articulação entre a lógica da simulação, o cálculo das estatísticas e a geração dos gráficos. Este desafio exigiu um forte espírito de equipa, comunicação constante e desenvolvimento de raciocínio em programação, pois foi necessário compreender o código uns dos outros, identificar incoerências (como dados inconsistentes ao longo do tempo ou gráficos vazios) e redefinir estruturas e fluxos de execução. A superação desta dificuldade passou pela divisão clara de tarefas, testes frequentes em conjunto e reformulação colaborativa de funções-chave, o que resultou num sistema mais robusto, coerente e alinhado com os objetivos da simulação.



### 4.	Conclusão e trabalho futuro

Este projeto permitiu aplicar conceitos fundamentais de programação em Python e compreender a importância da simulação de sistemas no contexto da Engenharia Biomédica e do quotidiano, levando a pensamentos de resolução típicos da Industria 4.0 – por meio de computação e ferramentas probabilísticas, reduzir o custo de análises de novas ferramentas sem desenvolver um protótipo custoso ou testar na prática.
A aplicação desenvolvida cumpre plenamente os objetivos inicialmente propostos, constituindo uma base sólida para o estudo e a simulação do funcionamento de uma clínica médica. Pretendemos continuar a aperfeiçoar esta aplicação, de forma a torná la cada vez mais eficaz e flexível, acrescentando novas funcionalidades que permitam ao utilizador extrair o máximo proveito da ferramenta. Como trabalho futuro, destaca se a possibilidade de inserir e remover especialidades clínicas de forma dinâmica, a inclusão de novas métricas e estatísticas relevantes para a tomada de decisão e o desenvolvimento de uma interface gráfica mais interativa, com um estilo próximo de um jogo, que permita visualizar de forma clara e intuitiva a evolução do estado da clínica. 
Para além disso, ambiciona se a integração de métodos de análise de variáveis em tempo real, permitindo acompanhar de forma contínua indicadores críticos como taxas de chegada, tempos médios de espera e níveis de ocupação de recursos. Esta abordagem possibilitaria a identificação antecipada de padrões de risco e cenários de sobrecarga, oferecendo ao utilizador uma pré visualização de problemas operacionais, antes mesmo de estes se manifestarem. Dessa forma, a unidade de saúde poderia organizar se de forma preventiva, ajustando recursos, redistribuindo profissionais ou alterando parâmetros de funcionamento com antecedência, de modo a garantir maior eficiência, resiliência do sistema e qualidade no atendimento aos pacientes.
