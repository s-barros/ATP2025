# Aplicação para gestão de alunos
## Autor: Sara Belo Leal de Barros, A111690
## Resumo: aplicação criada em vscode que permite ao utilizador criar e gerir as suas turmas.
## Lista de resultados: 

```python
op = int(input('''olá! O que vamos fazer? 
           #menu: 1: Criar uma turma;
      #2: Inserir um aluno na turma;
      #3: Listar a turma;
      #4: Consultar um aluno por id;
      #5: Guardar a turma em ficheiro;
      #6: Carregar uma turma dum ficheiro;
      #0: Sair da aplicação'''))
while op != 0:
    if op == 1:
        i = 0
        turma = []
        num = int(input("Quantos alunos tem a sua turma?"))
        while i < num:
            nome = input("qual o nome do seu aluno")
            id = int(input(f"Qual o id do(a) {nome} ?"))
            notaTPC = float(input(f"Qual foi a nota do TPC do(a) {nome}?"))
            notaProj = float(input(f"Qual foi a nota do projeto do(a) {nome}?"))
            notaTeste = float(input(f"Quanto é que o(a) {nome} tirou no teste?"))
            aluno = (nome, id, [notaTPC, notaProj, notaTeste])
            turma.append(aluno)
            i = i + 1 
        print(turma)
    elif op == 2:
        nome = input("qual o nome do seu aluno")
        id = int(input(f"Qual o id do(a) {nome} ?"))
        notaTPC = float(input(f"Qual foi a nota do TPC do(a) {nome}?"))
        notaProj = float(input(f"Qual foi a nota do projeto do(a) {nome}?"))
        notaTeste = float(input(f"Quanto é que o(a) {nome} tirou no teste?"))
        aluno = (nome, id, [notaTPC, notaProj, notaTeste])
        turma.append(aluno)
        print(turma)
    elif op == 3:
        i = 0
        while i < len(turma):
            print(f'''Aluno: {turma[i][0]}
              ID: {turma[i][1]}
              Notas: TPC: {turma[i][2][0]}
                     Projeto:{turma[i][2][1]}
                     Teste:{turma[i][2][2]}''')
            i = i + 1
    elif op == 4:
        Id = int(input("qual o id do aluno que quer procurar?"))
        i = 0
        while i < len(turma):
            if Id == turma[i][1]:
                print(turma[i])
            i = i + 1
    elif op == 5:
        f = open("turma.txt", "w", encoding='utf-8')
        i = 0
        while i < len(turma):
            f.write(f"{turma[i][0]},{turma[i][1]},{turma[i][2][0]},{turma[i][2][1]},{turma[i][2][2]}\n")
            i = i + 1
        f.close()
    elif op == 6:
        f = open("turma.txt", "r", encoding = "utf-8")
        turma = []
        for a in f:
            info = a.strip().split(",")
            aluno = (info[0], int(info[1]), [float(info[2]), float(info[3]), float(info[4])])
            turma.append(aluno)
        f.close()
        print(turma)
    op = int(input('''olá! O que vamos fazer? 
           #menu: 1: Criar uma turma;
      #2: Inserir um aluno na turma;
      #3: Listar a turma;
      #4: Consultar um aluno por id;
      #5: Guardar a turma em ficheiro;
      #6: Carregar uma turma dum ficheiro;
      #0: Sair da aplicação'''))

print("Até já!")
```
