preco = float(input('Digite o valor do produto: '))

print('''>>>Opções de pagamento<<<

[1] - À vista dinheiro/ cheque: 10% de desconto
[2] - À vista no cartão? 5% de desconto
[3] - em até 2x no cartão: preço normal
[4] - 3x ou mais no cartão: 20% de juros ''')

condicao = int(input('Digite o modo de pagamento: '))

if condicao == 1:
  print("O valor a ser pago com desconto é R${: .2f}".format(preco * 0.9))
elif condicao == 2:
  print("O valor a ser pago com desconto é R${: .2f}".format(preco * 0.95))
elif condicao == 3:
  print("O valor a ser pago é R${: .2f}".format(preco))
elif condicao == 4:
  print("O valor a ser pago com o juros é R${: .2f}".format(preco * 1.20))