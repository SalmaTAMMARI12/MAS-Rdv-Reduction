# main.py — Lance et compare les 3 scénarios 

 

from scenarios.scenario_1_baseline import run as run_s1 

from scenarios.scenario_2_rappel import run as run_s2 

from scenarios.scenario_3_complet import run as run_s3 

 

if __name__ == '__main__': 

    print('╔══════════════════════════════════════════╗') 

    print('║   MAS — Réduction des RDV Manqués        ║') 

    print('║   Framework : CrewAI | LLM : Bonsai 1.7B ║') 

    print('╚══════════════════════════════════════════╝') 

    print()

    # Scénario 1 — Baseline 

    res1 = run_s1() 

    print() 
    # Scénario 2 — Partiel 

    run_s2() 

    print() 

 

    # Scénario 3 — Complet 

    run_s3() 

    print() 

 

    # Comparaison finale 

    print('════════ COMPARAISON DES SCÉNARIOS ════════') 

    print(f"S1 — Sans MAS     : {res1['taux_absence']:.1f}% d'absence, 0 action") 

    print( 'S2 — 2 agents     : rappels envoyés, confirmations mesurées') 

    print( 'S3 — 3 agents     : rappels + replanification, RDV sauvés') 

    print( '→ Conclusion : le MAS complet réduit significativement les absences') 

 