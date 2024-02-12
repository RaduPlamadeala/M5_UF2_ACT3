import unittest
from costPersonalMeu import calculaCostDelPersonal
from costPersonalMeu import calcul_cost_treballador
from Treballador2 import Treballador


def test_calculaCostDelPersonal(self):
    treballador_meu = Treballador("Pepe",1, 2000, 20 )
    calculaCostDelPersonal(treballador_meu)
    
    self.assertEqual(calculaCostDelPersonal(treballador_meu), calcul_cost_treballador(Treballador))
    
def test_calculaCostDelPersonal(self):
    treballador_meu = Treballador("Ramon", "DIRECTOR", 2000)
    calculaCostDelPersonal(treballador_meu)
    
    self.assertEqual(calculaCostDelPersonal(treballador_meu), calcul_cost_treballador(Treballador))
    
def test_calculaCostDelPersonal(self):
    treballador_meu = Treballador("David", "SUBDIRECTOR", 2000)
    calculaCostDelPersonal(treballador_meu)
    
    self.assertEqual(calculaCostDelPersonal(treballador_meu), calcul_cost_treballador(Treballador))
        
    
if __name__ == '__main__':
    unittest.main()