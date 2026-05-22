# agents/agent_rappel.py 

from crewai import Agent 

from config import llm_bonsai 

import random 

 

class AgentRappel: 

    """ 

    Agent 2 — Worker 1 

    Envoie des rappels personnalisés selon le score de risque. 

    Trois niveaux : URGENT / STANDARD / SIMPLE 

    """ 

 

    SEUIL_URGENT = 0.75 

    SEUIL_STANDARD = 0.5 

 

    def __init__(self): 

        self.crew_agent = Agent( 

            role='Coordinateur de Rappels Patients', 

            goal='Envoyer le bon rappel au bon patient au bon moment', 

            backstory=( 

                'Vous êtes spécialisé dans la communication patient. ' 

                'Vous adaptez le niveau d urgence du rappel selon ' 

                'le score de risque calculé par l agent analyste.' 

            ), 

            llm=llm_bonsai, 

            verbose=True, 

        ) 

 

    def envoyer_rappels(self, df): 

        """ 

        Pour chaque patient en alerte : 

        - score >= 0.75 → rappel URGENT (appel + SMS + email) 

        - score >= 0.50 → rappel STANDARD (SMS + email) 

        - sinon        → rappel SIMPLE (SMS seul) 

        """ 

        df = df.copy() 

        df['rappel_envoye'] = False 

        df['type_rappel'] = 'aucun' 

        df['confirmation'] = False 

 

        alertes = df[df['alerte'] == True] 

 

        for idx, row in alertes.iterrows(): 

            score = row['score_risque'] 

 

            if score >= self.SEUIL_URGENT: 

                type_msg = 'URGENT — appel + SMS + email' 

            elif score >= self.SEUIL_STANDARD: 

                type_msg = 'STANDARD — SMS + email' 

            else: 

                type_msg = 'SIMPLE — SMS uniquement' 

 

            print(f'  [AgentRappel] #{idx} | score={score:.2f} | {type_msg}') 

 

            df.at[idx, 'rappel_envoye'] = True 

            df.at[idx, 'type_rappel'] = type_msg 

 

            # Simulation : patient confirme avec probabilité inverse au risque 

            df.at[idx, 'confirmation'] = (random.random() > score) 

 

        print(f'[AgentRappel] {len(alertes)} rappels envoyés.') 

        return df 