def questao1():
#insira o salário, e será a base para o limite.
 salario = float(input("Digite seu salário:R$"))
 limite = salario/2.5
 print(f"Seu limite é:R${limite}")

#Digite seu saldo e o valor a ser pago no boleto
 saldo = float(input("Digite seu saldo:R$ "))
 divida = float(input("Digite o valor da do boleto:R$ "))


 if saldo>=divida:
    print("Você pode pagar!")
    return
 
#Se você não tiver saldo o suficiente, a opção empréstimo será aberta.
 elif divida > saldo:
    print("Você não pode pagar!")
    print(f"Você possui R${limite} disponível para empréstimo.")
    emprestimo = float(input("Qual o valor do empréstimo?:R$ "))
 
    while(True):
        if emprestimo<=limite:
            if divida - saldo > emprestimo:
                print("O valor do emprestimo não é suficiente, tente outro valor! ")
                emprestimo = float(input("Qual o valor do empréstimo?:R$ "))
                if emprestimo > limite:
                   print("O valor do emprestimo é maior que o limite, digite outro valor: ")
                   emprestimo = float(input("Qual o valor do empréstimo?:R$ "))

            elif emprestimo + saldo >= divida:
                meses = int(input("Em quantos meses quer parcelar?: "))
                print(f"Você poderá pagar o boleto! \nVocê pagará R${emprestimo/meses} de empréstimo por mês, durante {meses} meses.")
                break
            else:
                print("Te lasca!")
                break

 valorEmConta = (emprestimo+saldo)-divida
 print(f"Saldo restante em conta:R${valorEmConta}")


questao1()
