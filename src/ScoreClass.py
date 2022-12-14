from os import remove

class Score:
    """
    Classe responsável pela verificação, criação, exclusão e gestão do arquivo .txt que armazena as pontuações e nomes dos jogadores.
    """

    def score_verifier():  # Realiza a abertura do score.txt e retorna sua existência ou não
        try:
            file = open("score.txt", "r")
        except:
            return False
        else:
            file.close()
            return True

    def player_info_getter():  # Retorna as informações contidas em score.txt
        file = open("score.txt", "r")
        lines = file.readlines()
        player01 = [lines[0].split("#")[1], int(lines[0].split("#")[2].replace("\n", ""))]
        player02 = [lines[1].split("#")[1], int(lines[1].split("#")[2].replace("\n", ""))]
        machine = int(lines[2].split("#")[1])
        file.close()
        return player01, player02, machine

    def write_data(player01, player02, machine):  # Escreve pontuações e nomes em score.txt
        file = open("score.txt", "w")
        file.write(f"PLAYER 01#{ player01[0] }#{ player01[1] }\nPLAYER 02#{ player02[0] }#{ player02[1] }\nMACHINE#{ machine }")
        file.close()

    def reset_game():  # Exclui o arquivo 'score.txt'
        try:
            remove("score.txt")
        except:
            return False
        else:
            return True
