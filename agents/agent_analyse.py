from crewai import Agent, Task 

from sklearn.ensemble import RandomForestClassifier 

from sklearn.model_selection import train_test_split 

from sklearn.metrics import classification_report 

from config import llm_bonsai 

import pandas as pd 

 

class AgentAnalyse: 

    """ 

    Agent 1 — Orchestrateur 

    Calcule le score de risque d'absence pour chaque patient. 

    """ 

 

    def __init__(self, seuil=0.5): 

        self.seuil = seuil 

        self.model = RandomForestClassifier( 

            n_estimators=100, random_state=42) 

        self.trained = False 

 

        # Définition de l'agent CrewAI 

        self.crew_agent = Agent( 

            role='Analyste Médical IA', 

            goal='Identifier les patients à risque d absence aux RDV', 

            backstory=( 

                'Vous êtes un expert en analyse prédictive médicale. ' 

                'Vous analysez les données historiques de rendez-vous ' 

                'pour calculer un score de risque d absence fiable.' 

            ), 

            llm=llm_bonsai, 

            verbose=True, 

        ) 

 

    def entrainer(self, X_train, y_train): 

        """Entraîne le modèle RandomForest""" 

        self.model.fit(X_train, y_train) 

        self.trained = True 

        print('[AgentAnalyse] Modèle entraîné.') 

 

    def analyser(self, X): 

        """Calcule les scores de risque et retourne DataFrame enrichi""" 

        if not self.trained: 

            raise Exception('Modèle non entraîné !') 

 

        scores = self.model.predict_proba(X)[:, 1] 

        df_result = X.copy() 

        df_result['score_risque'] = scores 

        df_result['alerte'] = df_result['score_risque'] >= self.seuil 

 

        nb = df_result['alerte'].sum() 

        print(f'[AgentAnalyse] {nb} patients à risque détectés.') 

        return df_result 

 

    def evaluer(self, X_test, y_test): 

        """Affiche les métriques de performance""" 

        y_pred = self.model.predict(X_test) 

        print('[AgentAnalyse] Rapport :') 

        print(classification_report( 

            y_test, y_pred, 

            target_names=['Présent', 'Absent'])) 