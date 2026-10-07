from fastapi import FastAPI, HTTPException

import s38_model
from s38_model import SessionLocal, init_db
from s38_schema import TaskIn


app = FastAPI(title="Bounty Board", version="0.3.0 (s38, MySQL)")


@app.get("/task-uri")
def lista_task_uri():
    with SessionLocal() as s:
        return [{"id": t.id, "titlu": t.titlu, "limbaj": t.limbaj,
                 "dificultate": t.dificultate, "recompensa": t.recompensa,
                 "rezolvat": t.rezolvat} for t in s38_model.toate_task_urile(s)]


@app.get("/task-uri/{task_id}")
def un_task(task_id: int):
    with SessionLocal() as s:
        t = s38_model.un_task(s, task_id)
        if t is None:
            raise HTTPException(status_code=404, detail=f"task-ul {task_id} nu exista")
        return {"id": t.id, "titlu": t.titlu, "limbaj": t.limbaj,
                "dificultate": t.dificultate, "recompensa": t.recompensa,
                "rezolvat": t.rezolvat}


@app.post("/task-uri", status_code=201)
def adauga_task(data: TaskIn):
    with SessionLocal() as s:
        t = s38_model.adauga_task(s, data.titlu, data.limbaj, data.dificultate, data.recompensa)
        return {"id": t.id, "titlu": t.titlu, "limbaj": t.limbaj,
                "dificultate": t.dificultate, "recompensa": t.recompensa,
                "rezolvat": t.rezolvat}


@app.put("/task-uri/{task_id}/rezolva")
def rezolva_task(task_id: int):
    with SessionLocal() as s:
        t = s38_model.marcheaza_rezolvat(s, task_id)
        if t is None:
            raise HTTPException(status_code=404, detail=f"task-ul {task_id} nu exista")
        return {"id": t.id, "rezolvat": t.rezolvat}


@app.delete("/task-uri/{task_id}")
def sterge_task(task_id: int):
    with SessionLocal() as s:
        t = s38_model.sterge_task(s, task_id)
        if not t:
            raise HTTPException(status_code=404, detail=f"task-ul {task_id} nu exista")
        return {"sters": task_id}


@app.get("/recompensa-disponibila")
def recompensa_disponibila():
    with SessionLocal() as s:
        return {"recompensa_totala": s38_model.recompensa_disponibila(s)}


import uvicorn

uvicorn.run(app, host="127.0.0.1", port=8000)
