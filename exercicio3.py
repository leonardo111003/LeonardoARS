preco = (input("qual o preço do produto"))
formadepagamento = (input("qual a forma do pagamento"))
avista = 0
umavez = 0
cincovezes = 0
dezvezes = 0
if formadepagamento = avista :
    avista = preco/2
    print("o preço a vista fica"avista)
else :
    pass  

if formadepagamento = umavez :
    umavez = preco/100
    precoparcialumavez = umavez*10
    precoumavez =  preco - precoparcialumavez
    print("o preço em uma vez fica "precoumavez)
else :
    pass

if formadepagamento = cincovezes :
    cincovezes = preco/100
    precoparcialcincovezes = cincovezes*10
    precocincovezes =  precoparcialcincovezes + preco
    print("o preço em uma vez fica "precocincovezes)
else :
    pass 


if formadepagamento = dezvezes :
    dezvezes = preco/100
    precoparcialdezvezes = dezvezes*50
    precodezvezes =  precoparcialdezvezes + preco
    print("o preço em uma vez fica "precodezvezes)
else :
    print("não temos outra opçãode pagamento")