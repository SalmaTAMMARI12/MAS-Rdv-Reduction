# scenario_3_complet.py 

from crew.crew_rdv import CrewRDV 
def run(): 

    print('=== SCÉNARIO 3 — MAS Complet (3 agents CrewAI) ===') 

 

    crew = CrewRDV(seuil=0.5) 

    df_final = crew.run(verbose=True) 

 

    # ── Résultats finaux ── 

    total = len(df_final) 

    alertes = df_final['alerte'].sum() 

    rappels = df_final['rappel_envoye'].sum() 

    confirmations = df_final['confirmation'].sum() 

    replanifies = df_final['replanifie'].sum() 

    rdv_sauves = confirmations + replanifies 

 

    print() 

    print('══════════ RÉSULTATS FINAUX ══════════') 

    print(f'Patients analysés    : {total:,}') 

    print(f'Patients à risque    : {alertes}') 

    print(f'Rappels envoyés      : {rappels}') 

    print(f'Confirmations        : {confirmations}') 

    print(f'RDV replanifiés      : {replanifies}') 

    print(f'Total RDV sauvés     : {rdv_sauves}') 

 

    if alertes > 0: 

        eff = rdv_sauves / alertes * 100 

        print(f'Efficacité globale   : {eff:.1f}%') 

 

    print('══════════════════════════════════════') 

    return df_final 

 

if __name__ == '__main__': 

    run() 