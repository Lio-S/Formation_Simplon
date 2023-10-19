# Try to import the module "mymodule"
try:
    from ..components import mymodule
except ImportError:
    mymodule = None

# test functions of "mymodule"
import os, sys

parent_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(parent_dir)
target_folder = os.path.join(parent_dir, "components")
sys.path.append(target_folder)

from mymodule import accélérer

class Test_Mymodule():
    def accélérer(self):
        accélérer(123)
        assert accélérer == 123,  "Test si vitesse est bien à 123"
        # assert ma_voiture.afficher_vitesse == 0,  "Test si vitesse est bien à 0"
