# crew/crew_rdv.py 

# Ce fichier assemble les 3 agents en un Crew CrewAI 

 

from crewai import Crew, Task, Process 

from agents.agent_analyse import AgentAnalyse 

from agents.agent_rappel import AgentRappel 

from agents.agent_replanification import AgentReplanification 

from utils.data_loader import load_data, get_features 

from sklearn.model_selection import train_test_split 

 

class CrewRDV: 

    """ 

    Orchestre les 3 agents en pipeline séquentiel. 

    Process.SEQUENTIAL = chaque agent attend la sortie du précédent. 

    """ 

 

    def __init__(self, seuil=0.5): 

        self.agent_analyse = AgentAnalyse(seuil=seuil) 

        self.agent_rappel = AgentRappel() 

        self.agent_replanif = AgentReplanification() 

 

    def run(self, verbose=True): 

        """Lance le pipeline complet""" 

 

        # 1. Charger et préparer les données 

        print('[CrewRDV] Chargement des données...') 

        df = load_data() 

        X, y = get_features(df) 

        X_train, X_test, y_train, y_test = train_test_split( 

            X, y, test_size=0.2, random_state=42) 

 

        # 2. Agent 1 — Analyse 

        print('[CrewRDV] Agent 1 : Analyse...') 

        self.agent_analyse.entrainer(X_train, y_train) 

        if verbose: 

            self.agent_analyse.evaluer(X_test, y_test) 

        df_analyse = self.agent_analyse.analyser(X_test) 

 

        # 3. Agent 2 — Rappel 

        print('[CrewRDV] Agent 2 : Rappel...') 

        df_rappel = self.agent_rappel.envoyer_rappels(df_analyse) 

 

        # 4. Agent 3 — Replanification 

        print('[CrewRDV] Agent 3 : Replanification...') 

        df_final = self.agent_replanif.replanifier(df_rappel) 

 

        return df_final 

 