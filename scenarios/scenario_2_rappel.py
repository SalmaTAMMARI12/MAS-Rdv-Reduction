# scenario_2_rappel.py 

from utils.data_loader import load_data, get_features 

from agents.agent_analyse import AgentAnalyse 

from agents.agent_rappel import AgentRappel 

from sklearn.model_selection import train_test_split 

 

def run(): 

    print('=== SCÉNARIO 2 — MAS partiel (Analyse + Rappel) ===') 

    df = load_data() 

    X, y = get_features(df) 

    X_train, X_test, y_train, y_test = train_test_split( 

        X, y, test_size=0.2, random_state=42) 

 

    agent1 = AgentAnalyse(seuil=0.5) 

    agent1.entrainer(X_train, y_train) 

    df_analyse = agent1.analyser(X_test) 

 

    agent2 = AgentRappel() 

    df_rappel = agent2.envoyer_rappels(df_analyse) 

 

    alertes = df_rappel['alerte'].sum() 

    confirmations = df_rappel['confirmation'].sum() 

    taux_conf = confirmations / alertes * 100 if alertes > 0 else 0 

 

    print(f'Patients à risque    : {alertes}') 

    print(f'Confirmations reçues : {confirmations}') 

    print(f'Taux confirmation    : {taux_conf:.1f}%') 

    print('→ Sans Agent 3 : les absences restantes ne sont pas replanifiées.') 

    return df_rappel 

 

if __name__ == '__main__': 

    run() 