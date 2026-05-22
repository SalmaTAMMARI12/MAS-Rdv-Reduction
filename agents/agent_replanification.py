# agents/agent_replanification.py 

from crewai import Agent 

from config import llm_bonsai 

 

class AgentReplanification: 

    """ 

    Agent 3 — Worker 2 

    Propose un nouveau créneau pour les patients n'ayant pas confirmé. 

    """ 

 

    # Agenda simulé du médecin (créneaux disponibles) 

    CRENEAUX_LIBRES = [ 

        '2024-06-10 09:00', '2024-06-10 10:30', 

        '2024-06-11 14:00', '2024-06-12 11:00', 

        '2024-06-13 08:30', '2024-06-14 15:00', 

        '2024-06-17 09:30', '2024-06-18 16:00', 

    ] 

 

    def __init__(self): 

        self.crew_agent = Agent( 

            role='Gestionnaire de Planning Médical', 

            goal='Optimiser l agenda du médecin en replanifiant les absences', 

            backstory=( 

                'Vous gérez l agenda d un cabinet médical privé. ' 

                'Votre rôle est de proposer rapidement un nouveau créneau ' 

                'aux patients qui risquent de manquer leur rendez-vous.' 

            ), 

            llm=llm_bonsai, 

            verbose=True, 

        ) 

 

    def replanifier(self, df): 

        """ 

        Pour chaque patient sans confirmation après rappel : 

        → propose automatiquement le prochain créneau libre. 

        Stratégie : timeout passif (pas de confirmation = absence anticipée) 

        """ 

        df = df.copy() 

        df['nouveau_creneau'] = None 

        df['replanifie'] = False 

 

        a_replanifier = df[ 

            (df['rappel_envoye'] == True) & 

            (df['confirmation'] == False) 

        ] 

 

        creneaux = self.CRENEAUX_LIBRES.copy() 

 

        for idx, row in a_replanifier.iterrows(): 

            if creneaux: 

                creneau = creneaux.pop(0) 

                df.at[idx, 'nouveau_creneau'] = creneau 

                df.at[idx, 'replanifie'] = True 

                print(f'  [AgentReplanif.] #{idx} → {creneau}') 

            else: 

                print(f'  [AgentReplanif.] #{idx} → aucun créneau libre') 

 

        print(f'[AgentReplanif.] {a_replanifier.shape[0]} patients traités.') 

        return df 