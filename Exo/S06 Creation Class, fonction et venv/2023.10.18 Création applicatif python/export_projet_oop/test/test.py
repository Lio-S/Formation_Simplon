# Test import
try: 
    import components.my_module
except ImportError:
    components.my_module = None

# Test de la fonction

from components.my_module import add,mul, balegoum

class Test_MyModule():

    def test_add(self):
        assert add(2,2) == 4 ,'balegoum is not feeling so good'

    def test_mul(self):
        assert mul(5,5) == 25

    def test_balegoum(self):
        assert balegoum('Balegoum') == 'Balegoum!', 'not good'
        assert balegoum('Labililili') == 'This is not Balegoum enough! ', 'wrong case broken'

