from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import Optional
from database import get_db
from models import Note

router = APIRouter()

class NoteCreate(BaseModel):
    content: str
    source: Optional[str] = None

class NoteResponse(BaseModel):
    id: str
    content: str
    source: Optional[str]

    class Config:
        from_attributes = True

@router.post("/notes", response_model=NoteResponse)
def create_note(note: NoteCreate, db: Session = Depends(get_db)):
    db_note = Note(content=note.content, source=note.source)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return NoteResponse(id=str(db_note.id), content=db_note.content, source=db_note.source)

@router.get("/notes")
def get_notes(db: Session = Depends(get_db)):
    notes = db.query(Note).all()
    return [{"id": str(n.id), "content": n.content, "source": n.source} for n in notes]

@router.delete("/notes/{note_id}")
def delete_note(note_id: str, db: Session = Depends(get_db)):
    note = db.query(Note).filter(Note.id == note_id).first()
    if not note:
        raise HTTPException(status_code=404, detail="Note not found")
    db.delete(note)
    db.commit()
    return {"deleted": True}