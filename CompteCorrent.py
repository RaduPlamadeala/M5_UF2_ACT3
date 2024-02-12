class CompteCorrent:
    def __init__(self, saldoInicial, cs):
        self.saldo = saldoInicial
        self.contrasenya = cs

    def dipositar(self, pasta: float) -> float:
        
        self.saldo += pasta
        return self.saldo

    def retirar(self, pasta: float, cs: str) -> float:

        if cs == self.contrasenya:
            if self.saldo >= pasta:
                self.saldo -= pasta
                return self.saldo
            else:
                return -1 
        else:
            return -2  

    def getSaldo(self, cs: str) -> float:

        if cs == self.contrasenya:
            return self.saldo
        else:
            return -2  # Contraseña incorrecta

    def setContrasenya(self, antiga: str, nova: str) -> int:

        if antiga == self.contrasenya:
            self.contrasenya = nova
            return 0
        else:
            return -2  

if __name__ == "__main__":

    compte = CompteCorrent(100, "password")

    assert compte.dipositar(50) == 150 
  
    assert compte.retirar(30, "wrong_password") == -2  

    assert compte.retirar(200, "password") == -1  

    assert compte.retirar(30, "password") == 120  

    assert compte.getSaldo("password") == 120 

    assert compte.getSaldo("wrong_password") == -2  

    assert compte.setContrasenya("password", "new_password") == 0  

    assert compte.setContrasenya("wrong_password", "new_password") == -2  
