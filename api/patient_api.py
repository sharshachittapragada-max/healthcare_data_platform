from fastapi import FastAPI

app = FastAPI()

patients = [
    {
        "patient_id": 1,
        "name": "Harsha Ch",
        "age": 45,
        "gender": "M",
        "diagnosis": "Diabetes",
        "provider_id": 101
    },
    {
        "patient_id": 2,
        "name": "Jane Smith",
        "age": 60,
        "gender": "F",
        "diagnosis": "Hypertension",
        "provider_id": 102
    }
]

@app.get("/patients")
def get_patients():
    return patients