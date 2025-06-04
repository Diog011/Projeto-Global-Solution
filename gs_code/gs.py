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
    print(pessoas_afetadas)
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
    pessoas_total = cri + ad + id + mr + fe
    pessoas_segmentadas.append(pessoas_total)
    print(pessoas_segmentadas)
    if pessoas_segmentadas == pessoas_afetadas:
        print("Número de pessoas válido")
    else:
        print("Número inválido")
        break
    i=i+1
