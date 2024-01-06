import subprocess
import combinarJSON

subprocess.run(['python', './stores/gatoarcano.py'])
subprocess.run(['python', './stores/fortalezapuq.py'])
subprocess.run(['python', './stores/comercialsmc.py'])
subprocess.run(['python', './stores/laloseta.py'])

combinarJSON.combinar_archivos()