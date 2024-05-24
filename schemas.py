from pydantic import BaseModel

class ToDoItemBase(BaseModel):
    title: str
    description: str | None = None

class ToDoItemCreate(ToDoItemBase):
    pass

class ToDoItemUpdate(BaseModel):
    done: bool

class ToDoItem(ToDoItemBase):
    id: int
    done: bool

    class Config:
        orm_mode = True