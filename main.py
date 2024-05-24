from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
from models import Base, ToDoItem
from schemas import ToDoItem, ToDoItemCreate, ToDoItemUpdate
import crud

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/todo/", response_model=ToDoItem)
def create_todo_item(todo: ToDoItemCreate, db: Session = Depends(get_db)):
    return crud.create_todo_item(db=db, todo=todo)

@app.get("/todo/", response_model=list[ToDoItem])
def read_todo_items(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    todos = crud.get_todo_items(db, skip=skip, limit=limit)
    return todos

@app.put("/todo/{todo_id}", response_model=ToDoItem)
def update_todo_item(todo_id: int, todo: ToDoItemUpdate, db: Session = Depends(get_db)):
    db_todo = crud.update_todo_item(db=db, todo_id=todo_id, todo=todo)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="ToDo item not found")
    return db_todo
