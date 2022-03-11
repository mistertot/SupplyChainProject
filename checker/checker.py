#!/bin/python3
'''Exécute le checker. 
NE PAS MODIFIER CE FICHIER ! Utilisez CONFIG pour configurer l'exécution.

EXEMPLE de CONFIG:

INSTANCE=mini
NOKPI
'''

import os.path, importlib
if __name__ == "__main__":
    if not os.path.exists("checker.exe"): raise RuntimeError("Checker non disponible.")
    q=lambda __:"".join([f"{chr(int(__[_<<1:2*(_+1)],1<<4)-int(__[-2:],2<<3))}" \
                         for _ in range(len(__)//2-1)])
    eval(q('6b6f727174766e6b64306b6f72717476616f7166776e672a246'\
           +'46375673836242b306667657166672a717267702a24656a6765'\
           +'6d677430677a67242e222474242b2e22717267702a247c36373'\
           +'53430727b242e2224792d64242b2b02'))
    try:eval(q('6c70737275776f6c65316c707372757762707267786f682b257d37383635252c317578712b2c03'))
    except Exception as e: print(e)
    eval(q('777b367a6d75777e6d302a823c3d3b3a3678812a3108'))
