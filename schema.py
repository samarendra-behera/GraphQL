import strawberry
import strawberry.test

@strawberry.type
class NoteType:
    id: int
    name: str
    description: str


@strawberry.input
class NoteInput:
    name: str
    description: str