# atividade 1
veiculos= ['aviao','carro','moto','jetsik','caminhao']
def upper_it(lista: list[str]): # -> list[str]:
    return [x.upper() for x in lista]

def upper_map(veiculo: str):
    return str.upper(veiculo)

# LAMBAD FUNC
#@lambda_fuc: lambda x: str.upper(x)

#maisculos= list(map(lambda_fuc,veiculos))



#if __name__=='__main__':
 #   print(map(upper_map,veiculos))
 #   print(upper_it(veiculos))
  #  print(f"COM LAMBAD FUNC : {maiusculos}")
# end atividade 1

# atividade 2

lista :list[int] = [0,1,2,3,4,5,6,7,8,9,10,12,23,5,6,2,12,54,2,1,2,5]


is_par= lambda x: x%2 ==0


print(list(filter(is_par,lista)))
# end atividade 2

# atividade 3 
lista_numeros :list[float]=[9.312321,7.34237,3.9282,6.342]
lista_precisao: list[int]=[2,2,3,3]

arrend= lambda x,y: round(x,y)

resultado = list(map(arrend,lista_numeros,lista_precisao))
print(f"atividade 3: {resultado}")


# END AVITIDADE 3

# atividade 4


numero =[1,2,3,4,5,6,7,8,9,10]

print(f"Ativiade 4:  {sum(numero)}")
