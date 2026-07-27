def transforma_base(questoes):
    base = {}
    
    for questao in questoes:
        nivel = questao['nivel']
        
        if nivel not in base:
            base[nivel] = []
        
        base[nivel].append(questao)
    
    return base

def valida_questao(questao):
    erros = {}

    chaves_obrigatorias = ['titulo', 'nivel', 'opcoes', 'correta']
    for chave in chaves_obrigatorias:
        if chave not in questao:
            erros[chave] = 'nao_encontrado'

    if len(questao) != 4:
        erros['outro'] = 'numero_chaves_invalido'

    if 'titulo' in questao:
        titulo = questao['titulo']
        if titulo.strip() == '':
            erros['titulo'] = 'vazio'

    if 'nivel' in questao:
        if questao['nivel'] not in ['facil', 'medio', 'dificil']:
            erros['nivel'] = 'valor_errado'

    if 'opcoes' in questao:
        opcoes = questao['opcoes']

        if len(opcoes) != 4:
            erros['opcoes'] = 'tamanho_invalido'
        else:
            chaves_validas = ['A', 'B', 'C', 'D']
            if sorted(opcoes.keys()) != chaves_validas:
                erros['opcoes'] = 'chave_invalida_ou_nao_encontrada'
            else:
                opcoes_vazias = {}
                for chave in chaves_validas:
                    if opcoes[chave].strip() == '':
                        opcoes_vazias[chave] = 'vazia'
                if opcoes_vazias:
                    erros['opcoes'] = opcoes_vazias

    if 'correta' in questao:
        if questao['correta'] not in ['A', 'B', 'C', 'D']:
            erros['correta'] = 'valor_errado'

    return erros

def valida_questoes(questoes):
    resultado = []
    for questao in questoes:
        resultado.append(valida_questao(questao))
    return resultado

from random import choice

def sorteia_questao(questoes, nivel):
    return choice(questoes[nivel])

def sorteia_questao_inedita(questoes, nivel, questoes_sorteadas):
    while True:
        questao = sorteia_questao(questoes, nivel)
        if questao not in questoes_sorteadas:
            questoes_sorteadas.append(questao)
            return questao

def questao_para_texto(questao, id):
    texto = "----------------------------------------\n"
    texto += f"QUESTAO {id}\n\n"
    texto += f"{questao['titulo']}\n\n"
    texto += "RESPOSTAS:\n"
    texto += f"A: {questao['opcoes']['A']}\n"
    texto += f"B: {questao['opcoes']['B']}\n"
    texto += f"C: {questao['opcoes']['C']}\n"
    texto += f"D: {questao['opcoes']['D']}"
    return texto

from random import randint, sample

def gera_ajuda(questao):
    erradas = []

    for letra, resposta in questao["opcoes"].items():
        if letra != questao["correta"]:
            erradas.append(resposta)

    quantidade = randint(1, 2)
    sorteadas = sample(erradas, quantidade)

    return "DICA:\nOpções certamente erradas: " + " | ".join(sorteadas)