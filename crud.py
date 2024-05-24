from sqlalchemy.orm import Session
from models import ToDoItem
from schemas import ToDoItemCreate, ToDoItemUpdate

def get_todo_items(db: Session, skip: int = 0, limit: int = 10):
    return db.query(ToDoItem).offset(skip).limit(limit).all()

def create_todo_item(db: Session, todo: ToDoItemCreate):
    db_todo = ToDoItem(**todo.dict())
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo_item(db: Session, todo_id: int, todo: ToDoItemUpdate):
    db_todo = db.query(ToDoItem).filter(ToDoItem.id == todo_id).first()
    if db_todo:
        db_todo.done = todo.done
        db.commit()
        db.refresh(db_todo)
    return db_todo
