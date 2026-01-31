# -*- coding: utf-8 -*-
"""
Script pour executer preuve_thermodynamique_planeur.py 
et sauvegarder le resultat dans un fichier texte propre.
"""

import subprocess
import sys
import os

# Chemin du script principal
script_path = os.path.join(os.path.dirname(__file__), "preuve_thermodynamique_planeur.py")
output_path = os.path.join(os.path.dirname(__file__), "RESULTAT_PREUVE.txt")

print("=" * 70)
print("EXECUTION DE LA PREUVE THERMODYNAMIQUE DU PLANEUR PHENIX")
print("=" * 70)
print(f"\nLe resultat sera sauvegarde dans: {output_path}")
print("\nExecution en cours...\n")

# Executer le script et capturer la sortie
try:
    result = subprocess.run(
        [sys.executable, script_path],
        capture_output=True,
        text=True,
        encoding='utf-8',
        errors='replace'
    )
    
    output = result.stdout
    if result.stderr:
        output += "\n\n=== ERREURS ===\n" + result.stderr
    
    # Sauvegarder dans un fichier
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(output)
    
    print(f"[OK] Resultat sauvegarde dans: {output_path}")
    print(f"\nOuvrez ce fichier avec Notepad ou VS Code pour voir le resultat complet.")
    print(f"\nApercu des dernieres lignes:")
    print("-" * 70)
    
    # Afficher les 50 dernieres lignes
    lines = output.strip().split('\n')
    for line in lines[-50:]:
        print(line)
        
except Exception as e:
    print(f"[ERREUR] {e}")
