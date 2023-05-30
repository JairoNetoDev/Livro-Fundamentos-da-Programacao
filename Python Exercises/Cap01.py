from os import system
system("cls");
q=int(input("(Digite 0 p/ Encerrar o Programa) (Digite 1 p/ Iniciar o Programa).\n"));
print();
while q != 0:
    questao=int(input("Digite o número da questão: ")); print();
    #Subtração de Dois números:
    if questao == 1:
        print("Quetão 01: Subtração de Dois números.\n");
        num1=float(input('Digite o primeiro Número: '));
        num2=float(input('Digite o segundo Número: '));
        sub=num1-num2;
        print(f"A subtração do Primeiro pelo Segundo é de: {sub:.2f}"); print();
        print('====================================================');
        q=int(input("(Digite 0 p/ Encerrar o programa) (Digite 1 p/ Continuar).\n")); print();
    #Múltiplicação de três números
    elif questao == 2:
        print("Questão 02: Múltiplicação de três números.\n");
        num1=float(input("Insira o primeiro número: "));
        num2=float(input("Insira o segundo número: "));
        num3=float(input("Insira o terceiro número: "));
        mult=num1*num2*num3
        print(f"Multiplicação dos números: {mult:.2f}"); print();
        print('====================================================');
        q=int(input("(Digite 0 p/ Encerrar o programa) (Digite 1 p/ Continuar).\n")); print();
    #Divisão de dois Números
    elif questao == 3:
        print("Questão 03: Divisão de dois Números.\n")
        num1=float(input("Insira seu primerio número: "));
        num2=float(input("Insira seu segundo número: "));
        while num2 == 0:
            print('Você digitou o segundo número = 0. Não é possível dividir.');
            num2=float(input('Digite outro número novamente: '));
        div=num1/num2;
        print(f"Divisão dos números {num1}/{num2}: {div:.2f}"); print();
        print('====================================================');
        q=int(input("(Digite 0 p/ Encerrar o programa) (Digite 1 p/ Continuar).\n")); print();
    #Média ponderada de duas Notas / Peso 2 para nota1; Peso 3 para nota2
    elif questao == 4:
        print("Questão 04: Média ponderada de duas Notas / Peso 2 para nota1; Peso 3 para nota2.\n");
        nota1=float(input("Digite a primeira Nota: "));
        nota2=float(input("Digite a segunda Nota: "));
        med=((nota1 * 2) + (nota2 * 3))/2;
        print("Peso 2 para Primeira Nota / Peso 3 Segunda Nota.");
        print(f"Média Ponderada das Notas: {med:.2f}"); print();
        print('====================================================');
        q=int(input("(Digite 0 p/ Encerrar o programa) (Digite 1 p/ Continuar).\n")); print();
    #Preço do Produto com desconto X; pp(Preço do Produto); ppd(Preço do Produto com Desconto)
    elif questao == 5:
        print("Questão 5: Preço do Produto com desconto x.\n");
        pp=float(input('Insira o preço do produto (R$): '));
        desc=float(input("Insira o desconto do produto (%): "));
        ppd=pp-(pp*desc/100); print(f"Novo preço do produto com {desc:.2f}% de desconto: {ppd:.2f}R$"); print();
        print('====================================================');
        q=int(input("(Digite 0 p/ Encerrar o programa) (Digite 1 p/ Continuar).\n")); print();
    elif questao == 6:
        print("Questão 6: Aumento do Salário Fixo do funcionário caso venda X produtos, com comissão de X%.\n");
        salf=float(input("Insira o Salário Fixo do Funcionário (R$): "));
        qtdp=int(input("Quantidade de Produtos vendidos pelo Funcionário, no Mês: "));
        aumcomi=float(input("Insira a taxa de comissão (%): "));
        newsalf=salf+(salf*aumcomi/100);
        print(f"Aumento do Salário do Funcionário com a Taxa da comissão de {aumcomi}%: {newsalf:.2f}R$"); print();
        print('====================================================');
        q=int(input("(Digite 0 p/ Encerrar o programa) (Digite 1 p/ Continuar).\n")); print();
    elif questao == 7:
        print("Questão 7: Peso da Pessoa caso engorde x% e emagreça x%\n");
        peso=float(input("Insira o Peso (Kg): "));
        eng=float(input("Insira a (%) e descubra o Peso caso engorde (x%): ")); peng=peso+(peso*eng/100); print(f"Peso após engordar {eng}%: {peng:.2f}KG");
        ema=float(input("Insira a (%) e descubra o Peso caso emagreça (x%): ")); pema=peso-(peso*ema/100); print(f"Peso após emagrecer {ema}%: {pema:.2f}KG"); print();
        print('====================================================');
        q=int(input("(Digite 0 p/ Encerrar o programa) (Digite 1 p/ Continuar).\n")); print();
    elif questao == 8:
        print("Questão 8: Peso em Quilogramas(KG) para Gramas(G)\n");
        peso=float(input("Informe o Peso em KG: ")); pesog=peso*1000;
        print(f"Peso em Quilogramas: {peso:.2f}KG / Peso em Gramas(G): {pesog}G");
        print('====================================================');
        q=int(input("(Digite 0 p/ Encerrar o programa) (Digite 1 p/ Continuar).\n")); print();




