cand1=[]
cand2=[]
cand3=[]
eleitores=int(input("digite o numero de eleitores: "))
for i in range(0,eleitores):
    def votar():
        print("candidato1=1\ncandidato2=2\ncandidato3=3")
        voto=int(input("voto: "))
        if voto == 1:
            cand1.append(voto)
        elif voto == 2:
            cand2.append(voto)
        elif voto == 3:
            cand3.append(voto)
        else:
            print("numero inválido")
            votar()
    votar()
if cand1 > cand2 and cand1 > cand3:
    print("campeão: candidado 1")
elif cand2 > cand1 and cand2 > cand3:
    print("campeão: candidado 2")
elif cand3 > cand1 and cand3 > cand2:
    print("campeão: candidado 3")
elif cand1 == cand2 and cand1 == cand3:
    print("empate dos 3")
    
print(f"candidato 1: {len(cand1)} votos\ncandidato 2: {len(cand2)} votos\ncandidato 3: {len(cand3)} votos")