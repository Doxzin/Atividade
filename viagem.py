def calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios,# define o nome da função e os parametros que vão chama-la
custo_pedagio):

    custo_combustivel_total = (distancia / consumo_veiculo) * custo_combustivel# define o calculo para encontrar o custo do combustivel total

    custo_pedagio_total = numero_pedagios * custo_pedagio# define o calculo para encontrar o pedagio total

    custo_total = custo_combustivel_total + custo_pedagio_total # define o calculo para encontrar o 

    return custo_total, custo_combustivel_total, custo_pedagio_total # retorna os valores das contas a cima

distancia = float(input("Digite a distância da viagem (em km): ")) # pede a distância da viagem, custo do combustivel, consumo do veiculo,
#quantidade de pedagios no caminho e o custos deles
custo_combustivel = float(input("Digite o custo do combustível por litro (em R$): "))
consumo_veiculo = float(input("Digite o consumo do veículo (km por litro): "))
numero_pedagios = int(input("Digite o número de pedágios no percurso: "))
custo_pedagio = float(input("Digite o custo de um pedágio (em R$): "))

custo_total, custo_combustivel_total, custo_pedagio_total = calcular_custo_viagem(distancia, custo_combustivel, consumo_veiculo, numero_pedagios,
custo_pedagio)# faz retornar o valor do custo da viagem

print(f"Custo total da viagem: R${custo_total:.2f}") # printa o que esta escrito e com os resultados
print(f"Custo total com combustível: R${custo_combustivel_total:.2f}")
print(f"Custo total com pedágios: R${custo_pedagio_total:.2f}")