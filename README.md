# MAS — Réduction des Rendez-vous Manqués

Système multi-agents pour réduire les absences aux rendez-vous médicaux.  
Développé dans le cadre du cours **IA & Applications** — ENSIAS.

---

## Présentation

Le projet simule un cabinet médical qui utilise des agents intelligents pour détecter les patients à risque d'absence, leur envoyer un rappel personnalisé, et proposer une replanification si nécessaire.

Trois scénarios sont comparés :
- **S1** — baseline sans aucune intervention
- **S2** — rappels automatiques uniquement
- **S3** — système MAS complet avec replanification

---

## Architecture

```
Dataset Kaggle
     │
     ▼
Agent Risque        ← RandomForest, score d'absence 0→1
     │
     ▼
Agent Rappel        ← Message URGENT / STANDARD / SIMPLE
     │
     ▼
Agent Replanif.     ← Propose un créneau libre si non-réponse
```

**Framework** : [CrewAI](https://github.com/joaomdmoura/crewAI)  
**LLM local** : TinyLlama 1.1B via [llama.cpp](https://github.com/ggerganov/llama.cpp)  
**Dataset** : [Kaggle Medical Appointment No Shows](https://www.kaggle.com/datasets/joniarroba/noshowappointments)

---

## Prérequis

- Python 3.10+
- Git
- llama.cpp (voir ci-dessous)
- Le fichier `KaggleV2-May-2016.csv` placé dans `data/`

---

## Installation

```bash
git clone https://github.com/VOTRE_USERNAME/mas_rdv_crewai
cd mas_rdv_crewai
pip install -r requirements.txt
```

Cloner et compiler llama.cpp (ou télécharger le `.exe` pré-compilé) :

```bash
git clone https://github.com/ggerganov/llama.cpp
```

Télécharger le modèle GGUF et le placer dans `llama.cpp/models/` :  
→ [tinyllama-1.1b-chat-v1.0.Q4_0.gguf](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF)

---

## Lancer le projet

>  Les deux terminaux doivent rester ouverts en même temps.

**Terminal 1 — démarrer le serveur LLM :**

```bash
cd llama.cpp
./llama-server.exe -m models/tinyllama-1.1b-chat-v1.0.Q4_0.gguf --port 8080
```

Attendre le message : `llama server listening at http://127.0.0.1:8080`

**Terminal 2 — lancer la simulation (mode terminal) :**

```bash
PYTHONIOENCODING=utf-8 python main.py
```

---

## Interface web

Pour une démonstration visuelle dans le navigateur, utiliser l'interface Flask à la place de `main.py`.

**Terminal 2 — lancer le serveur web :**

```bash
PYTHONIOENCODING=utf-8 python app.py
```

Puis ouvrir **http://localhost:5000** dans le navigateur et cliquer sur **"Lancer les agents"**.

> Le Terminal 1 (llama-server) doit toujours être actif avant de lancer `app.py`.

---

## Structure du projet

```
mas_rdv_crewai/
├── main.py                  # Point d'entrée principal
├── app.py                   # Serveur Flask (interface web)
├── index.html
├── Demo/             # Frontend de démo
├── data/
│   └── KaggleV2-May-2016.csv
├── crew/
│   └── crew_rdv.py          # Définition de la crew CrewAI
├── scenarios/
│   ├── scenario_1_baseline.py
│   ├── scenario_2_rappels.py
│   └── scenario_3_complet.py
├── utils/
│   └── data_loader.py
└── requirements.txt
```



## Membres

- Salma TAMMARI
- Assmaa EL HIDANI
