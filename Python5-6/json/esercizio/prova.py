import json

# Funzione per deserializzare il file JSON
def Deserialize(file_path) -> dict:
    try:
        with open(file_path, "r") as json_file:
            dict_1 = json.load(json_file)
        return dict_1
    except Exception as errore:
        print(f"Errore: {errore}")
        return None

# Funzione per rispondere alle domande richieste
def analyze_quiz_data(data):
    total_questions = 0
    total_options = 0
    math_questions = 0

    # Iteriamo su ogni categoria del quiz (es. 'sport', 'maths')
    for category, questions in data["quiz"].items():
        # Iteriamo su ogni domanda in una categoria
        for q_id, q_data in questions.items():
            total_questions += 1  # Aumentiamo il conteggio delle domande
            total_options += len(q_data["options"])  # Sommiamo il numero di opzioni della domanda

            # Se la categoria è 'maths', contiamo le domande di matematica
            if category == "maths":
                math_questions += 1

    # Calcoliamo la media delle risposte possibili per domanda
    avg_options_per_question = total_options / total_questions if total_questions > 0 else 0

    # Risultati
    print(f"Totale domande nel questionario: {total_questions}")
    print(f"Numero medio di risposte per domanda: {avg_options_per_question:.2f}")
    print(f"Totale domande di matematica: {math_questions}")

# Deserializziamo il file JSON e analizziamo i dati
quiz_data = Deserialize("quiz.json")

# Se il file è stato caricato correttamente, analizziamo i dati
if quiz_data:
    analyze_quiz_data(quiz_data)
