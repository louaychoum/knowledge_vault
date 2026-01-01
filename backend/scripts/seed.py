from database import SessionLocal
from models import Note, Tag, NoteTag

db = SessionLocal()

db.query(NoteTag).delete()
db.query(Note).delete()
db.query(Tag).delete()

tags = [
    Tag(name="productivity"),
    Tag(name="stoicism"),
    Tag(name="habits"),
]
db.add_all(tags)
db.commit()

notes = [
    Note(content="We suffer more in imagination than in reality.", source="Seneca - Letters from a Stoic"),
    Note(content="You do not rise to the level of your goals. You fall to the level of your systems.", source="James Clear - Atomic Habits"),
    Note(content="The obstacle is the way.", source="Ryan Holiday"),
    Note(content="Focus on what you can control, ignore what you cannot.", source="Epictetus"),
    Note(content="Small habits compound into remarkable results.", source="James Clear - Atomic Habits"),
]
db.add_all(notes)
db.commit()

# Link some notes to tags
db.add(NoteTag(note_id=notes[0].id, tag_id=tags[1].id))  # Seneca -> sto
db.add(NoteTag(note_id=notes[1].id, tag_id=tags[2].id))  # Atomic Habits -> habits
db.add(NoteTag(note_id=notes[2].id, tag_id=tags[1].id))  # Ryan Holiday -> stoicism
db.add(NoteTag(note_id=notes[3].id, tag_id=tags[1].id))  # Epictetus -> stoicism
db.add(NoteTag(note_id=notes[4].id, tag_id=tags[0].id))  # Atomic Habits -> productivity
db.add(NoteTag(note_id=notes[4].id, tag_id=tags[2].id))  # Atomic Habits -> habits
db.commit()

db.close()
print(f"Seeded {len(tags)} tags and {len(notes)} notes.")