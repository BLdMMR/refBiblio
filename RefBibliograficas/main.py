
# Programa para formatar referências bibliográficas

def main():
    while(True):

        print("Tipo de referência bibliográfica:\n1. Artigo em pp\n2. Obra\n3. Artigo em obra coletiva\n4. Website\n5. Legislação Nacional\n6. Tratado Internacional\n7. Jurisprudência")
        option = input("Que tipo de referência quer formatar? ")

        if (option == "1"):
            artigoEmPP()
        elif (option == "2"):
            obra()
        elif (option == "3"):
            artigoObraColetiva()
        elif (option == "4"):
            website()
        elif (option == "5"):
            legislacaoNacional()
        elif (option == "6"):
            tratadoInternacional()
        elif (option == "7"):
            jurisprudencia()

        more = input("\n\nFormatar mais referências? (S/N) ")

        more = more.upper()

        if (more == "S"):
            continue
        elif (more == "N"):
            break
        else:
            print("Era uma pergunta de Sim ou Não..... Gente burra")
            break

def obra():
    autores = construirNomes()
    nome_corpo, nome_rodape, nome_biblio = formatarNomes(autores)

    title = input("Título: ")
    edicao = input("Edição: ")
    editora = input("Editora: ")
    vol = input("Vol.: ")
    year = input("Ano: ")
    page = input("Página(s): ")

    formated_page = ''
    if page.find("-"):
        formated_page = "pp. " + page
    else:
        formated_page = "p. "

    edicao = edicao + ".ª ed."

    corpo = "(" + nome_corpo + ": " + year + ", " + page + ")"
    rodape = nome_rodape + ",\033[3m " + title + "\033[0m, " + vol + ", " + edicao + ", " + editora + ", " + year + ", " + formated_page + "."
    final = nome_biblio + ",\033[3m in \"" + title + "\033[0m\", " + vol + ", " + edicao + ", " + editora + ", " + year + "."

    print("\nCorpo: \n" + corpo + "\n\nRodapé: \n" + rodape + "\n\nFinal: \n" + final)

    return

def artigoObraColetiva():

    autores = construirNomes()
    nome_corpo, nome_rodape, nome_biblio = formatarNomes(autores)

    title = input("Título: ")
    book = input("Nome da Obra: ")
    dir_Coord = input("Director ou Coordenador (Dir./Coord.): ")
    dirsCoords_list = construirNomesDirCoord()
    dir_coord_nomes = "(" + dir_Coord + ") " + formatarDirsCoords(dirsCoords_list)

    print(dir_coord_nomes)

    edicao = input("Edição: ")
    editora = input("Editora: ")
    vol = input("Vol.: ")
    year = input("Ano: ")
    page = input("Página específica: ")
    paginas = input("Intervalo de páginas (ex. 200-210): ")

    paginas = "pp. " + paginas

    if page.find("-") != -1:
        formated_page = "pp. " + page
    else:
        formated_page = "p. " + page

    corpo = "(" + nome_corpo + ": " + year + ", " + page + ")"
    rodape = nome_rodape + ", \"" + title + "\"\033[3m, in " + book + "\033[0m, " + dir_coord_nomes + ", " + vol + ", " + edicao + ".ª ed., "+ editora + ", " + year + ", " + formated_page + "."
    final = nome_biblio + " - \"" + title + "\"\033[3m, in " + book + "\033[0m, " + dir_coord_nomes + ", " + vol + ", " + edicao + ".ª ed., "+ editora + ", " + year + ", " + paginas + "."
    print("\nCorpo: \n" + corpo + "\nRodapé: \n" + rodape + "\n\n" + "Final: \n" + final)

    return
def artigoEmPP():

    autores = construirNomes()
    nome_corpo, nome_rodape, nome_biblio = formatarNomes(autores)

    title = input("Título: ")
    book = input("Nome da Revista: ")
    n = input("Nº: ")
    details = input("Volume, Períodicidade, etc.: (ex. Vol. X, Jan-Jul)")
    year = input("Ano: ")
    page = input("Página específica: ")
    paginas = input("Intervalo de páginas (ex. 200-210): ")

    paginas = "pp. " + paginas

    formated_page = ''
    if page.find("-") != -1:
        formated_page = "pp. " + page
    else:
        formated_page = "p. " + page

    corpo = "(" + nome_corpo + ": " + year + ", " + page + ")"
    rodape = nome_rodape + ", \"" + title + "\"\033[3m, in " + book + "\033[0m, nº " + n + ", " + details + ", " + year + ", " + formated_page + "."
    final = nome_biblio + " - \"" + title + "\"\033[3m, in " + book + "\033[0m, nº " + n + ", " + details + ", " + year + ", " + paginas + "."
    print("\nCorpo: \n" + corpo + "\nRodapé: \n" + rodape + "\n\n" + "Final: \n" + final)

    return
def website():
    return

def legislacaoNacional():
    return

def tratadoInternacional():
    return

def jurisprudencia():
    return


def apelidoPrimeiro(nome):
    nomeFinal = nome[len(nome) - 1].upper() + ","

    for i in nome:
        if i == nome[len(nome) - 1]:
            break
        nomeFinal = nomeFinal + " " + i

    return nomeFinal



def construirNomes():
    numAutores = int(input("Numero de autores: "))
    autores = []
    i = 1
    while i <= numAutores:
        if (i == 3):
            autores.append("et al.")
            break
        autores.append(input("Nome do " + str(i) + "º autor: "))
        i += 1
    return autores

def construirNomesDirCoord():
    numAutores = int(input("Numero de Diretores/Coordenadores: "))
    dirsCoords = []
    i = 1
    while i <= numAutores:
        if (i == 3):
            dirsCoords.append("et al.")
            break
        dirsCoords.append(input("Nome do " + str(i) + "º autor: "))
        i += 1
    return dirsCoords

def formatarDirsCoords(dirsCoords):
    nomes = ''

    for dirCoord in dirsCoords:
        nomes = nomes + dirCoord + ", "

    return nomes[:-2]


def formatarNomes(autores):
    nome_corpo_list = []
    nome_rodape_list = []
    nome_biblio_list = []
    i = 0
    for autor in autores:
        if autor == "et al.":
            nome_corpo_list.append(autor + ", ")
            nome_rodape_list.append(autor + ", ")
            nome_biblio_list.append(autor + ", ")
            break

        nome_split = autor.split(' ')

        apelido = nome_split[len(nome_split) - 1]
        nome = autor.replace(" " + apelido, '', 1)

        nome_corpo_list.append(apelido.upper() + ", ")  # APELIDO
        nome_rodape_list.append(autor.upper() + ", ")  # NOME COMPLETO
        nome_biblio_list.append(apelido.upper() + ", " + nome + ", ")  # APELIDO, Nome

    nome_corpo = ''
    nome_rodape = ''
    nome_biblio = ''

    for i in range(len(nome_corpo_list)):
        nome_corpo = nome_corpo + nome_corpo_list[i]
        nome_rodape = nome_rodape + nome_rodape_list[i]
        nome_biblio = nome_biblio + nome_biblio_list[i]

    return nome_corpo[:-2], nome_rodape[:-2], nome_biblio[:-2]


if __name__ == "__main__":
    main()