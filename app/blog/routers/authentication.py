from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from blog import database, models, token
from blog.hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm as OAuth2

router = APIRouter(
    prefix="/login",
    tags=["Authentication"],
    responses={404: {"description": "Not Found"}}
)


@router.post('/')
def login(request:OAuth2 = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Credentials")
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Password Mismatch")
    
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}