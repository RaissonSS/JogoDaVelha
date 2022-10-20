class txtFile:

    def ScoreVerifier():
        try:
            file = open("score.txt", "r")
        except:
            return False
        else:
            txtFile.PlayerInfoGetter(file)

    def PlayerInfoGetter(file):
        lines = file.readlines()
        player01 = [lines[0].split("#")[1], lines[0].split("#")[2].replace("\n", "")]
        player02 = [lines[1].split("#")[1], lines[1].split("#")[2].replace("\n", "")]
        print(player01, player02)
        return [player01, player02]  # TEM QUE RETORNAR O SCORE DA MÁQUINA!

    '''def CreateScore():
        file = open("score.txt", "w")
        file.close()
        return False'''  # MÉTODO ARQUIVADO / conflita com Menu.Opening()

    def WriteData(player01, player02, machine):
        file = open("score.txt", "w")
        file.write(f"PLAYER 01#{ player01[0] }#{ player01[1] }\nPLAYER 02#{ player02[0] }#{ player02[1] }\nMACHINE#{ machine }")
        file.close()

    # Para atualizar dados, chamar PlayerInfoGetter e levar apenas os dados que ficarão e os novos para WriteData
    # INCLUIR DATA DO JOGO NO SCORE
