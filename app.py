class Computador:
    def __init__(self, marca, memoria_ram, placa_de_video):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video = placa_de_video

    def ligar(self):
        print("Estou ligando o computador!")   

    def desligar(self):
        print('Estou deslingando o computador!')


    def exibir_dados_computador(self):
        print(
            f'Computador da marca {self.marca}, com {self.memoria_ram} de memória ram que usa placa de vídeo {self.placa_de_video}'
        )


computador1 = Computador('Asus', '32gb', 'Nvida')
computador1.ligar()
computador1.desligar()
computador1.exibir_dados_computador()



        
