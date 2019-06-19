class Carro:

    def __init__(self,consumo):
        self.consumo = consumo
        self.nivelGasolina = 0
        
    def andar(self,km):
        consumo = km/self.consumo
        self.nivelGasolina -= consumo
    
    def adicionarGasolina(self,nivel):
        self.nivelGasolina += nivel
        
    def obterGasolina(self):
        print('Combustível restante é:',self.nivelGasolina,'Litros')
    
carro = Carro(15)
carro.adicionarGasolina(20)
carro.andar(100)
carro.obterGasolina()

        
        
        
        
