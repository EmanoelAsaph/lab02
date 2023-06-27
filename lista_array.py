from estrutura_elementar import estrutura_elementar


class ArrayList(estrutura_elementar):
    def __init__(self):
        self.lista = []
        pass

    def esta_vazio(self) -> bool:
        x = len(self.lista)
        if len(self.lista) == 0:
            return True
        return False

    def inserir(self, item):
        self.lista.append(item)
        pass

    def remove(self, item):
         self.lista.remove(item)
        

    def tamanho(self) -> int:
        tamanhoarray = len(self.lista)
        return tamanhoarray
        

    def limpa(self):
        self.lista = []
        

    def procura(self, item) -> bool:
        for i in range(len(self.lista)):
            if self.lista[i] == item:
                return True
        return False
        

    def indice_de(self, item):
        for i in range(len(self.lista)):
            if self.lista[i] == item:
                return i
        
        return -1

    def recupera_indice(self, index):
        if index < len(self.lista):
            return self.lista[index]
        return None
