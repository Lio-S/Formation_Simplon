# Test import
try: 
    import components.my_module
except ImportError:
    components.my_module = None

# Test de la fonction

from components.my_module import add,mul, test

class Test_MyModule():

    def test_add(self):
        assert add(2,2) == 4 ,' not feeling so good'

    def test_mul(self):
        assert mul(5,5) == 25

    def test(self):
        assert test('test') == 'test!', 'not good'
        assert test('Labililili') == 'This is not test enough! ', 'wrong case broken'

