from fastapi import APIRouter, Depends, status
from blog import schemas, database, oauth2
from sqlalchemy.orm import Session
from blog.repository import blog as blog_repo

router = APIRouter(
    prefix="/blogs",
    tags=["Blogs"],
    responses={404: {"description": "Not Found"}}
)

get_db = database.get_db


@router.get("/", response_model=list[schemas.ShowBlog])
def all_blogs(db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repo.show_all(db)




@router.post("/", status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db),  current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repo.create(request, db)



@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, db: Session = Depends(get_db),  current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repo.delete(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db),  current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repo.update(id, request, db)



@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=schemas.ShowBlog)
def show_blog(id: int, db: Session = Depends(get_db),  current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blog_repo.show(id, db)