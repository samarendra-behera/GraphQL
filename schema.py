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


@strawberry.input
class RegisterInput:
    name: str
    email: str
    password: str

@strawberry.input
class LoginInput:
    email:str
    password: str

@strawberry.type
class LoginType:
    email: str
    token: str

@strawberry.type
class UserType:
    id: int 
    name: str
    email: str

