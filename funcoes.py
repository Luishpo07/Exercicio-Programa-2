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