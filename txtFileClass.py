class txtFile:

    def ScoreVerifier():
        try:
            file = open("score.txt", "r")
        except:
            # CRIAR
            return False
        else:
            file.close()
            return True

    def PlayerInfoGetter():
        if txtFile.ScoreVerifier():
            file = open("score.txt", "r")
            lines = file.readlines()
            player01 = [lines[0].split("#")[1], lines[0].split("#")[2].replace("\n", "")]
            player02 = [lines[1].split("#")[1], lines[1].split("#")[2].replace("\n", "")]

            return [player01, player02]
        else:
            return False

    def CreateScore():
        # criar arquivo
        pass
