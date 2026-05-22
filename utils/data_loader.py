# utils/data_loader.py 

import pandas as pd 

 

def load_data(path='data/KaggleV2-May-2016.csv'): 

    df = pd.read_csv(path) 

 

    # Renommer colonnes 

    df.rename(columns={ 

        'No-show': 'absent', 

        'PatientId': 'patient_id', 

        'SMS_received': 'sms_recu', 

        'ScheduledDay': 'date_prise_rdv', 

        'AppointmentDay': 'date_rdv', 

    }, inplace=True) 

 

    # Encoder la cible : Yes=1 (absent), No=0 (présent) 

    df['absent'] = df['absent'].map({'Yes': 1, 'No': 0}) 

 

    # Calculer le délai entre prise de RDV et date du RDV 

    df['date_prise_rdv'] = pd.to_datetime(df['date_prise_rdv'], utc=True) 

    df['date_rdv'] = pd.to_datetime(df['date_rdv'], utc=True) 

    df['delai_jours'] = (df['date_rdv'] - df['date_prise_rdv']).dt.days 

    df['delai_jours'] = df['delai_jours'].clip(lower=0) 

 

    return df 

 

def get_features(df): 

    """Retourne X (features) et y (cible)""" 

    features = ['Age', 'delai_jours', 'Scholarship', 

                'Hipertension', 'Diabetes', 'Alcoholism', 

                'Handcap', 'sms_recu'] 

    X = df[features].fillna(0) 

    y = df['absent'] 

    return X, y 