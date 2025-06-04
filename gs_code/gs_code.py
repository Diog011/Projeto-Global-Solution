numero_desastres = []
tipo_desastre = []
paises = []
cidades = []
bairros = []
ruas = []
pessoas_afetadas = []

criancas = []
adultos = []
idosos = []
mobilidade_reduzida = []
feridos = []
pessoas_segmentadas = []

n_desastres = int(input("Insira a quantidade de desastres: "))
i = 0
while i in range(n_desastres):
    d = input("Qual o tipo de desastre: ")
    tipo_desastre.append(d)
    p = input("Qual o país do desastre? ")
    paises.append(p)
    c = input("Qual a cidade do desastre? ")
    cidades.append(c)
    b = input("Qual o bairro do desastre? ")
    bairros.append(b)
    r = input("Qual a rua do desastre? ")
    ruas.append(r)
    pa = int(input("Qual a quantidade de pessoas afetadas? "))
    pessoas_afetadas.append(pa)
    print("------------------------------------")
    cri = int(input("Quantidade de crianças afetadas: "))
    criancas.append(cri)
    ad = int(input("Quantidade de adultos afetados: "))
    adultos.append(ad)
    id = int(input("Quantidade de idosos afetados: "))
    idosos.append(id)
    mr = int(input("Quantidade de pessoas com mobilidade reduzidas afetadas"))
    mobilidade_reduzida.append(mr)
    fe = int(input("Quantidade de feridos afetadas"))
    feridos.append(fe)
    pessoas_soma = cri + ad + id + mr + fe
    pessoas_segmentadas.append(pessoas_soma)
    if pessoas_segmentadas == pessoas_afetadas:
        print("Número de pessoas válido")
    else:
        print("Número inválido")
        break
    i=i+1

print("------------------------------------")
total_afetadas = sum(pessoas_segmentadas)
soma_criancas = sum(criancas)
soma_adultos = sum(adultos)
soma_idosos = sum(idosos)
soma_mobilidade_reduzida = sum(mobilidade_reduzida)
soma_feridos = sum(feridos)
categorias = ["Crianças", "Adultos", "Idosos", "Mobilidade reduzida", "Feridos"]
valores = [soma_criancas, soma_adultos, soma_idosos, soma_mobilidade_reduzida, soma_feridos]
mais_afetada = categorias[valores.index(max(valores))]
indice_grave = pessoas_afetadas.index(max(pessoas_afetadas))


print("O número de desastres é ", n_desastres)
print("------------------------------------")
print("O número total de pessoas afetadas é ", total_afetadas)
print("------------------------------------")
print("O total por categorias")
print("Criancas:", soma_criancas,"|", "Adultos:", soma_adultos, "|", "Idosos:", soma_idosos, "|", "Mobilidade Reduzida:", soma_mobilidade_reduzida, "|", "Feridos:", soma_feridos)
print("------------------------------------")
print(f"\nCategoria mais afetada: {mais_afetada}")
print("------------------------------------")
print("\nDesastre com maior número de afetados:")
print(f"Tipo: {tipo_desastre[indice_grave]}")
print(f"Local: {ruas[indice_grave]}, {bairros[indice_grave]}, {cidades[indice_grave]}, {paises[indice_grave]}")