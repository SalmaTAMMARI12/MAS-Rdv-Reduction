# config.py 

# Configuration de la connexion au LLM Bonsai local 

 

from crewai import LLM 

 

# LLM Bonsai via llama-server (tourne sur votre machine) 

# Assurez-vous que llama-server est lancé avant d'exécuter le projet 

llm_bonsai = LLM( 

    model='openai/bonsai',          # nom du modèle 

    base_url='http://localhost:8080/v1',   # URL du serveur local 

    api_key='not-needed',            # pas de clé requise en local 

    temperature=0.3,                 # faible = réponses stables 

    max_tokens=512, 

) 