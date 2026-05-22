# scenario_1_baseline.py 

from utils.data_loader import load_data 

 

def run(): 

    print('=== SCÉNARIO 1 — Baseline (sans MAS) ===') 

    df = load_data() 

 

    total = len(df) 

    absents = df['absent'].sum() 

    taux = absents / total * 100 

 

    print(f'Total RDV           : {total:,}') 

    print(f'RDV manqués         : {absents:,}') 

    print(f'Taux d absence      : {taux:.1f}%') 

    print('→ Sans MAS : aucune action. Les absences ne sont pas gérées.') 

    return {'taux_absence': taux, 'total': total, 'absents': absents} 

 

if __name__ == '__main__': 

    run() 