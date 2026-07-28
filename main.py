from funcoes import (
    transforma_base,
    valida_questoes,
    sorteia_questao_inedita,
    questao_para_texto,
    gera_ajuda
)

VERMELHO = "\033[91m"
VERDE = "\033[92m"
AMARELO = "\033[93m"
AZUL = "\033[94m"
CIANO = "\033[96m"
ROXO = "\033[95m"
NEGRITO = "\033[1m"
RESET = "\033[0m"

PONTOS = [1000, 5000, 10000, 30000, 50000, 100000, 300000, 500000, 1000000]


def cor_por_premio(premio):
    if premio < 10000:
        return CIANO
    elif premio < 100000:
        return AZUL
    elif premio < 500000:
        return AMARELO
    return VERDE


def pede_opcao():
    while True:
        opcao = input(f"{NEGRITO}Sua resposta (A/B/C/D/pula/ajuda): {RESET}").strip().lower()
        if opcao in ["a", "b", "c", "d", "pula", "ajuda"]:
            return opcao
        print(VERMELHO + "Opção inválida. Digite A, B, C, D, pula ou ajuda." + RESET)


def aguarda_enter(msg="Aperte ENTER para continuar..."):
    input(AMARELO + msg + RESET)


def mostra_manual():
    print(NEGRITO + ROXO + "\nManual do jogo:" + RESET)
    print(" - Digite A, B, C ou D para responder.")
    print(" - Digite ajuda para receber uma dica.")
    print(" - Digite pula para pular a questão.")
    print(" - As questões seguem a ordem: fácil, médio e difícil.")
    print(" - Aperte ENTER quando o jogo pedir para continuar.\n")


def nivel_da_questao(numero_questao):
    if numero_questao <= 3:
        return "facil"
    elif numero_questao <= 6:
        return "medio"
    return "dificil"


def mensagem_nivel(nivel):
    if nivel == "facil":
        return "HEY! Você começou no nível FACIL!"
    elif nivel == "medio":
        return "HEY! Você passou para o nível MEDIO!"
    return "HEY! Você chegou ao nível DIFICIL!"


def mostra_inicio_nivel(numero_questao):
    nivel = nivel_da_questao(numero_questao)
    print(NEGRITO + ROXO + "\n" + mensagem_nivel(nivel) + RESET)
    aguarda_enter()


def joga():
    nome = input("Digite seu nome: ").strip()

    print(NEGRITO + CIANO + "\nBem-vindo ao Fortuna DesSoft!" + RESET)
    print("Responda perguntas, use 3 pulos e 2 ajudas, e tente chegar ao prêmio máximo.")
    mostra_manual()

    questoes = [
        {'titulo': 'Qual o resultado da operação 57 + 32?',
         'nivel': 'facil',
         'opcoes': {'A': '-19', 'B': '85', 'C': '89', 'D': '99'},
         'correta': 'C'},

        {'titulo': 'Qual a capital do Brasil?',
         'nivel': 'facil',
         'opcoes': {'A': 'Brasília', 'B': 'Rio de janeiro', 'C': 'São Paulo', 'D': 'Osasco'},
         'correta': 'A'},

        {'titulo': 'Quando é o feriado da Independência do Brasil?',
         'nivel': 'facil',
         'opcoes': {'A': '21 de Abril', 'B': '12 de Outubro', 'C': '07 de Setembro', 'D': '15 de Novembro'},
         'correta': 'C'},

        {'titulo': '_________ é um conjunto de particularidades que caracterizam um grupo de pessoas, uma família ou uma sociedade. É formada por princípios morais, hábitos, costumes, histórias, manifestações religiosas, entre outros. Qual palavra melhor completa o início da frase?',
         'nivel': 'facil',
         'opcoes': {'A': 'Missão', 'B': 'Cultura', 'C': 'Curso superior', 'D': 'Culinária'},
         'correta': 'B'},

        {'titulo': 'Qual destes termos menos tem relação com o fenômeno da globalização?',
         'nivel': 'facil',
         'opcoes': {'A': 'Aculturação', 'B': 'Neoliberalismo', 'C': 'União Europeia', 'D': 'Caldeirão do Huck'},
         'correta': 'D'},

        {'titulo': 'Qual o feriado do aniversário da cidade de São Paulo?',
         'nivel': 'facil',
         'opcoes': {'A': '25 de Janeiro', 'B': '24 de Março', 'C': '9 de Julho', 'D': '12 de Novembro'},
         'correta': 'A'},

        {'titulo': 'Qual destas não é uma fruta?',
         'nivel': 'facil',
         'opcoes': {'A': 'Laranja', 'B': 'Maça', 'C': 'Tomate', 'D': 'Abacate'},
         'correta': 'B'},

        {'titulo': 'Em qual ano o TikTok atingiu 1 bilhão de usuários?',
         'nivel': 'facil',
         'opcoes': {'A': '2019', 'B': '2021', 'C': '2015', 'D': '2018'},
         'correta': 'B'},

        {'titulo': 'Qual destes não é um app com foco em streaming de vídeo?',
         'nivel': 'facil',
         'opcoes': {'A': 'Netflix', 'B': 'Disney Plus', 'C': 'TIDAL', 'D': 'HBO Max'},
         'correta': 'C'},

        {'titulo': 'Qual destes parques não se localiza em São Paulo?!',
         'nivel': 'facil',
         'opcoes': {'A': 'Ibirapuera', 'B': 'Parque do Carmo', 'C': 'Parque Villa Lobos', 'D': 'Morro da Urca'},
         'correta': 'D'},

        {'titulo': 'Qual destas não é uma linguagem de programação?',
         'nivel': 'facil',
         'opcoes': {'A': 'Miratdes', 'B': 'Python', 'C': 'Lua', 'D': 'C++'},
         'correta': 'A'},

        {'titulo': 'Dentre os listados, qual destes esportes é menos praticado no Brasil?',
         'nivel': 'facil',
         'opcoes': {'A': 'Natação', 'B': 'Vôlei', 'C': 'Ski Cross Country', 'D': 'Futebol'},
         'correta': 'C'},

        {'titulo': 'Qual o resultado da operação 5 + 2 * 3?',
         'nivel': 'medio',
         'opcoes': {'A': '21', 'B': '11', 'C': '30', 'D': '10'},
         'correta': 'B'},

        {'titulo': 'Qual destas é uma pseudociência que estuda os corpos celestes e as prováveis relações que possuem com a vida das pessoas e os acontecimentos na Terra?',
         'nivel': 'medio',
         'opcoes': {'A': 'Astronomia', 'B': 'Física quântica', 'C': 'Astrologia', 'D': 'Computação'},
         'correta': 'C'},

        {'titulo': 'Qual destas não foi considerada em 2007 uma das sete maravilhas do mundo moderno?',
         'nivel': 'medio',
         'opcoes': {'A': 'Muralha da China', 'B': 'Machu Picchu', 'C': 'Cristo Redentor', 'D': 'Torre Eiffel'},
         'correta': 'D'},

        {'titulo': 'Qual destas pessoas conduziu importantes estudos sobre radioatividade, sendo ganhadora de dois prêmios Nobel?',
         'nivel': 'medio',
         'opcoes': {'A': 'Marie Curie', 'B': 'Paul Erdős', 'C': 'Clive W.J. Granger', 'D': 'Maria Ressa'},
         'correta': 'A'},

        {'titulo': 'Quem é considerada a primeira pessoa programadora do mundo?!',
         'nivel': 'medio',
         'opcoes': {'A': 'Marie Curie', 'B': 'Alan Turing', 'C': 'Ada Lovelace', 'D': 'Edsger Dijkstra'},
         'correta': 'C'},

        {'titulo': 'Qual destes números é primo?',
         'nivel': 'medio',
         'opcoes': {'A': '259', 'B': '85', 'C': '49', 'D': '19'},
         'correta': 'D'},

        {'titulo': 'Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?',
         'nivel': 'medio',
         'opcoes': {'A': 'Collatz', 'B': 'Goldbach', 'C': 'Poincaré', 'D': 'Hodge'},
         'correta': 'A'},

        {'titulo': 'Como faço para chamar o SAMU?',
         'nivel': 'medio',
         'opcoes': {'A': 'Ligue 101', 'B': 'Ligue 192', 'C': 'Ligue 109', 'D': 'Ligue 122'},
         'correta': 'B'},

        {'titulo': 'Qual a segunda pessoa mais seguida no Instagram?',
         'nivel': 'medio',
         'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Kylie Jenner'},
         'correta': 'D'},

        {'titulo': 'Qual a pessoa mais seguida no Instagram?',
         'nivel': 'medio',
         'opcoes': {'A': 'Cristiano Ronaldo', 'B': 'Dwayne Johnson', 'C': 'Kim Kardashian', 'D': 'Lionel Messi'},
         'correta': 'A'},

        {'titulo': 'A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?',
         'nivel': 'dificil',
         'opcoes': {'A': 'Autogamia', 'B': 'Esporulação', 'C': 'Partenogênese', 'D': 'Divisão binária'},
         'correta': 'A'},

        {'titulo': 'Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?',
         'nivel': 'dificil',
         'opcoes': {'A': '441', 'B': '86', 'C': 'Nenhuma das outras respostas', 'D': '23'},
         'correta': 'D'},

        {'titulo': 'Quem é Oxóssi?!',
         'nivel': 'dificil',
         'opcoes': {'A': 'Rede de mercados', 'B': 'Tipo de poema Dissílabo', 'C': 'Divindade das religiões africanas', 'D': 'Trapper brasileiro'},
         'correta': 'C'},

        {'titulo': 'Qual a altura do Cristo Redentor?',
         'nivel': 'dificil',
         'opcoes': {'A': 'entre 0 e 20 metros', 'B': 'Entre 21 e 40 metros', 'C': 'Entre 41 e 60 metros', 'D': 'Mais que 60 metros'},
         'correta': 'B'},

        {'titulo': 'Em que ano faleceu Charles Babbage?',
         'nivel': 'dificil',
         'opcoes': {'A': '2022', 'B': '1791', 'C': '1935', 'D': '1871'},
         'correta': 'A'},

        {'titulo': 'Einstein foi Nobel de física em qual ano?',
         'nivel': 'dificil',
         'opcoes': {'A': '1906', 'B': '1905', 'C': '1920', 'D': '1921'},
         'correta': 'D'},

        {'titulo': 'Qual o número atômico do nitrogênio?',
         'nivel': 'dificil',
         'opcoes': {'A': '9', 'B': '7', 'C': '6', 'D': '8'},
         'correta': 'B'},

        {'titulo': 'Qual o ponto de fusão do nitrogênio?',
         'nivel': 'dificil',
         'opcoes': {'A': '120º C', 'B': '15º C', 'C': '-210º C', 'D': '-180º C'},
         'correta': 'C'},

        {'titulo': 'Quantos gols Pelé fez oficialmente?',
         'nivel': 'dificil',
         'opcoes': {'A': '815', 'B': '762', 'C': '1100', 'D': '1057'},
         'correta': 'B'},

        {'titulo': 'O que é Necrose?',
         'nivel': 'dificil',
         'opcoes': {'A': 'Uma banda de Rock', 'B': 'Uma marca de luxo', 'C': 'Cidade Francesa', 'D': 'Morte de tecido orgânico'},
         'correta': 'D'},

         {'titulo': 'Qual é o maior artilheiro do futebol no século 21?',
         'nivel': 'medio',
         'opcoes': {'A': 'Neymar', 'B': 'Cristiano Ronaldo', 'C': 'Lionel Messi', 'D': 'Pelé'},
         'correta': 'B'},

         {'titulo': 'Qual é o maior finalizador da história do UFC?',
         'nivel': 'medio',
         'opcoes': {'A': 'Islam Makhachev', 'B': 'Demetrious Johnson', 'C': 'Demian Maia', 'D': 'Charles Oliveira'},
         'correta': 'D'}
    ]

    erros = valida_questoes(questoes)
    for i, erro in enumerate(erros):
        if erro != {}:
            print(VERMELHO + f"Erro na questão {i + 1}: {erro}" + RESET)
            return

    base = transforma_base(questoes)
    questoes_sorteadas = []

    pulos_restantes = 3
    ajudas_restantes = 2
    premio_atual = 0
    indice_premio = 0
    numero_questao = 1

    while True:
        if indice_premio == len(PONTOS):
            print(NEGRITO + VERDE + f"\nParabéns, {nome}! Você ganhou o prêmio máximo!" + RESET)
            return

        if numero_questao > len(PONTOS):
            print(NEGRITO + CIANO + f"\nFim do jogo! Você saiu com R$ {premio_atual:.2f}." + RESET)
            return

        if numero_questao in [1, 4, 7]:
            mostra_inicio_nivel(numero_questao)
        else:
            aguarda_enter()

        nivel = nivel_da_questao(numero_questao)

        disponiveis = [q for q in base[nivel] if q not in questoes_sorteadas]
        if not disponiveis:
            print(AMARELO + f"Não há mais questões inéditas no nível {nivel}." + RESET)
            return

        questao = sorteia_questao_inedita(base, nivel, questoes_sorteadas)
        if questao not in questoes_sorteadas:
            questoes_sorteadas.append(questao)

        ajuda_usada_nesta_questao = False

        while True:
            print()
            print(ROXO + questao_para_texto(questao, numero_questao) + RESET)
            print(NEGRITO + cor_por_premio(premio_atual) + f"\nPrêmio atual: R$ {premio_atual:.2f}" + RESET)
            print(CIANO + f"Pulos restantes: {pulos_restantes}" + RESET)
            print(CIANO + f"Ajudas restantes: {ajudas_restantes}" + RESET)

            opcao = pede_opcao()

            if opcao == "ajuda":
                if ajudas_restantes == 0:
                    print(AMARELO + "Você não tem mais ajudas." + RESET)
                    continue
                if ajuda_usada_nesta_questao:
                    print(AMARELO + "Você já usou ajuda nesta questão." + RESET)
                    continue

                print(AMARELO + gera_ajuda(questao) + RESET)
                ajudas_restantes -= 1
                ajuda_usada_nesta_questao = True
                continue

            if opcao == "pula":
                if pulos_restantes == 0:
                    print(AMARELO + "Você não tem mais pulos." + RESET)
                    continue

                pulos_restantes -= 1
                print(AMARELO + "Questão pulada." + RESET)
                numero_questao += 1
                break

            if opcao.upper() == questao["correta"]:
                premio_atual = PONTOS[indice_premio]
                indice_premio += 1

                print(VERDE + "Resposta correta!" + RESET)
                print(VERDE + f"Seu prêmio atual é de R$ {premio_atual:.2f}" + RESET)

                numero_questao += 1
                break

            else:
                print(VERMELHO + "Resposta errada." + RESET)
                print(VERMELHO + "Você saiu sem prêmio." + RESET)
                return


def menu_principal():
    while True:
        joga()

        novamente = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        while novamente not in ["s", "n"]:
            novamente = input("Digite s ou n: ").strip().lower()

        if novamente == "n":
            print(CIANO + "Até mais!" + RESET)
            break


if __name__ == "__main__":
    menu_principal()