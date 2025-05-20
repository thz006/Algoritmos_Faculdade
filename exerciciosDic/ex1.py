dicionario_traducao = {
    "apple": "maçã", "book": "livro", "car": "carro", "dog": "cachorro", "egg": "ovo",
    "fish": "peixe", "girl": "menina", "house": "casa", "ice": "gelo", "juice": "suco",
    "key": "chave", "love": "amor", "moon": "lua", "night": "noite", "orange": "laranja",
    "pen": "caneta", "queen": "rainha", "road": "estrada", "sun": "sol", "tree": "árvore",
    "umbrella": "guarda-chuva", "violin": "violino", "water": "água", "xylophone": "xilofone", "yogurt": "iogurte",
    "zebra": "zebra", "animal": "animal", "baby": "bebê", "cloud": "nuvem", "dance": "dançar",
    "eat": "comer", "family": "família", "garden": "jardim", "happy": "feliz", "idea": "ideia",
    "job": "trabalho", "kite": "pipa", "lamp": "lâmpada", "music": "música", "nose": "nariz",
    "open": "abrir", "pizza": "pizza", "quiet": "quieto", "rain": "chuva", "school": "escola",
    "table": "mesa", "under": "embaixo", "voice": "voz", "window": "janela", "zero": "zero",
    "air": "ar", "beach": "praia", "cat": "gato", "door": "porta", "earth": "terra",
    "fire": "fogo", "game": "jogo", "hat": "chapéu", "island": "ilha", "jungle": "selva",
    "king": "rei", "lake": "lago", "mountain": "montanha", "neck": "pescoço", "owl": "coruja",
    "pig": "porco", "queen": "rainha", "river": "rio", "star": "estrela", "train": "trem",
    "use": "usar", "village": "vila", "wall": "parede", "yard": "quintal", "zoo": "zoológico",
    "ant": "formiga", "bridge": "ponte", "circle": "círculo", "dream": "sonho", "energy": "energia",
    "flower": "flor", "gift": "presente", "hill": "colina", "insect": "inseto", "jacket": "jaqueta",
    "knife": "faca", "leaf": "folha", "mirror": "espelho", "net": "rede", "ocean": "oceano",
    "photo": "foto", "quiet": "silêncio", "rock": "rocha", "sand": "areia", "tent": "barraca",
    "up": "cima", "valley": "vale", "wind": "vento", "year": "ano", "zip": "zíper",
    "afternoon": "tarde", "ball": "bola", "cold": "frio", "dark": "escuro", "engine": "motor",
    "fast": "rápido", "gift": "presente", "horse": "cavalo", "iron": "ferro", "jam": "geleia",
    "kite": "pipa", "light": "luz", "milk": "leite", "name": "nome", "old": "velho",
    "paint": "pintar", "quiet": "silêncio", "red": "vermelho", "stone": "pedra", "time": "tempo",
    "uncle": "tio", "vase": "vaso", "watch": "relógio", "yellow": "amarelo", "zone": "zona",
    "arm": "braço", "blue": "azul", "cup": "copo", "duck": "pato", "elbow": "cotovelo"
}

palavra = input("palavra: ").lower()

traducao = dicionario_traducao.get(palavra)

if traducao:
    print(f"A tradução de '{palavra}' é: {traducao}")
else:
    print("essa palavra não está no dicionário.")
