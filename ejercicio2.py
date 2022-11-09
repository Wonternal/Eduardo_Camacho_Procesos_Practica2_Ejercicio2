import os
import platform
parametro = "-c"
if (platform.system() == "Windows"):
    parametro = "-n"
host = input("Dominio o IP a la que hacer el ping: ")

os.system(f"ping {parametro} 5 {host}")