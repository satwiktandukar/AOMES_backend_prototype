import datetime
from telnetlib import STATUS
from fastapi import FastAPI, Depends, Response, status
from typing import Optional
import logging
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from jose import JWTError, jwt
from fastapi.middleware.cors import CORSMiddleware
from random import choices


from sqlalchemy.orm import Session
from passlib.context import CryptContext

from blog.schemas import *
from blog.token import ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token
from . import models
from blog.database import SessionLocal, engine
from .hashing import *

origins = ['*']
# origins = [
#     *,
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
#     "http://127.0.0.1:8000",
#     "http://localhost:34201"

# ]

models.Base.metadata.create_all(engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f'{exc}'.replace('\n', ' ').replace('   ', ' ')
    logging.error(f"{request}: {exc_str}")
    content = {'status_code': 10422, 'message': exc_str, 'data': None}
    return JSONResponse(content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY)


# @app.post("/user")
# def create(response: Response, request: Login, db: Session = Depends(get_db)):
#     response.headers["Access-Control-Allow-Origin"] = "*"
#     if (len(blogs) > 20):
#         blog = choices(blogs, k=21)
#         blogs = blog

# #     hashedPassword = pwd_cxt.hash(request.password)
#     new_user = models.Login(phone = request.phone, password = hashedPassword)
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

@app.post("/create", tags=['Login']) 
def login(request: Login, response: Response, db: Session = Depends(get_db)):
    response.headers["Access-Control-Allow-Origin"] = "*"
    # if (len(blogs) > 20):
    #     blog = choices(blogs, k=21)
    #     blogs = blog
    hashedPassword = pwd_cxt.hash(request.password)
    new_user = models.Login(phone=request.phone, password=hashedPassword)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.get("/admin", tags=['Admin'])
def login(response: Response, db: Session = Depends(get_db), phone: str = ""):
    response.headers["Access-Control-Allow-Origin"] = "*"

    new_user = models.Admin(phone=phone)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"detail": "done"}


@app.post("/login", tags=['Login'])
def login(request: Login, response: Response, db: Session = Depends(get_db)):
    response.headers["Access-Control-Allow-Origin"] = "*"

    user = db.query(models.Login).filter(
        models.Login.phone == request.phone).first()
    admin_check = db.query(models.Admin).filter(
        models.Admin.phone == request.phone).first()

    if (not user):
        return {"info": "Not found"}

    if not Hash.verify(user.password, request.password):
        return {"info": "incorrect password"}

    else:
        if (admin_check):
            return {"info": "Admin"}

        # return {"info": "logged_in"}
        access_token = create_access_token(data={"sub": user.phone})
        return {"access_token": access_token, "token_type": "bearer"}


# @app.post("/question/post/MBBS", status_code=status.HTTP_201_CREATED, tags=['MBBS'])
# def post_question(request: MBBS, db: Session = Depends(get_db),):

#     new = models.MBBS(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
#                       answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
#     db.add(new)
#     db.commit()
#     db.refresh(new)
#     return new


# @app.post("/question/post/Nursing", status_code=status.HTTP_201_CREATED, tags=['Nursing'])
# def post_question(request: MBBS, db: Session = Depends(get_db),):

#     new_blog = models.Nursing(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
#                               answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.get("/question/get/Nursing", tags=['Nursing'])
# def get_question(response: Response, db: Session = Depends(get_db)):
#     blogs = db.query(models.Nursing).all()

#     response.headers["Access-Control-Allow-Origin"] = "*"
    # if (len(blogs) > 20):
    #     blog = choices(blogs, k=21)
    #     blogs = blog

#     # header("Access-Control-Allow-Origin: *");
#     return blogs


# @app.post("/question/post/BMLT", tags=['BMLT'])
# def post_question(request: MBBS, db: Session = Depends(get_db),):

#     new_blog = models.BMLT(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
#                            answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.get("/question/get/BMLT", tags=['BMLT'])
# def get_question(response: Response, db: Session = Depends(get_db)):
#     blogs = db.query(models.BMLT).all()
# #     response.headers["Access-Control-Allow-Origin"] = "*"
#     if (len(blogs) > 20):
#         blog = choices(blogs, k=21)
#         blogs = blog

#     # header("Access-Control-Allow-Origin: *");
#     return blogs


# @app.post("/question/post/Agriculture", tags=['Agriculture'])
# def post_question(request:MBBS db: Session = Depends(get_db),):

#     new_blog = models.Agriculture(question=question, answer_1=answer_1,
#                                   answer_2=answer_2, answer_3=answer_3, answer_4=answer_4, correct=correct,)
#     db.add(new_blog)
#     db.commit()
#     db.refresh(new_blog)
#     return new_blog


# @app.get("/question/get/Agriculture", tags=['Agriculture'])
# def get_question(response: Response, db: Session = Depends(get_db)):
#     blogs = db.query(models.Agriculture).all()
#     response.headers["Access-Control-Allow-Origin"] = "*"
    # if (len(blogs) > 20):
    #     blog = choices(blogs, k=21)
    #     blogs = blog

#     # header("Access-Control-Allow-Origin: *");
#     return blogs


@app.post("/question/post/MBBS/Zoology", status_code=status.HTTP_201_CREATED, tags=['MBBS'])
def post_question(request: MBBS, db: Session = Depends(get_db),):

    new_blog = models.MBBS_Zoology(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                   answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/MBBS/Zoology", status_code=status.HTTP_200_OK, tags=['MBBS'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.MBBS_Zoology).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/MBBS/Zoology/", status_code=status.HTTP_201_CREATED, tags=['MBBS'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.MBBS_Zoology).filter(
        models.MBBS_Zoology.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/MBBS/Botany", status_code=status.HTTP_201_CREATED, tags=['MBBS'])
def post_question(request: MBBS, db: Session = Depends(get_db),):

    new_blog = models.MBBS_Botany(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                  answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.delete("/question/delete/MBBS/Botany/", status_code=status.HTTP_201_CREATED, tags=['MBBS'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.MBBS_Botany).filter(models.MBBS_Zoology.question ==
                                        question).delete(synchronize_session=False)
    db.commit()
    db.commit()
    return {'done'}


@app.get("/question/get/MBBS/Botany", status_code=status.HTTP_200_OK, tags=['MBBS'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.MBBS_Botany).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.post("/question/post/MBBS/Chemistry", status_code=status.HTTP_201_CREATED, tags=['MBBS'])
def post_question(request: MBBS, db: Session = Depends(get_db),):

    new_blog = models.MBBS_Chemistry(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                     answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/MBBS/Chemistry", status_code=status.HTTP_200_OK, tags=['MBBS'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.MBBS_Chemistry).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/MBBS/Chemistry/", status_code=status.HTTP_201_CREATED, tags=['MBBS'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.MBBS_Chemistry).filter(
        models.MBBS_Chemistry.question == question).delete(synchronize_session=False)
    db.commit()
    db.commit()
    return {'done'}


@app.post("/question/post/MBBS/MAT", status_code=status.HTTP_201_CREATED, tags=['MBBS'])
def post_question(request: MBBS, db: Session = Depends(get_db),):

    new_blog = models.MBBS_MAT(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                               answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/MBBS/MAT", status_code=status.HTTP_200_OK, tags=['MBBS'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.MBBS_MAT).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/MBBS/MAT/", status_code=status.HTTP_201_CREATED, tags=['MBBS'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.MBBS_MAT).filter(models.MBBS_MAT.question ==
                                     question).delete(synchronize_session=False)
    db.commit()
    db.commit()
    return {'done'}


@app.post("/question/post/BMLT/Zoology", status_code=status.HTTP_201_CREATED, tags=['BMLT'])
def post_question(request: BMLT, db: Session = Depends(get_db),):

    new_blog = models.BMLT_Zoology(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                   answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/BMLT/Zoology", status_code=status.HTTP_200_OK, tags=['BMLT'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.BMLT_Zoology).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/BMLT/Zoology/", status_code=status.HTTP_201_CREATED, tags=['BMLT'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.BMLT_Zoology).filter(
        models.BMLT_Zoology.question == question).delete(synchronize_session=False)
    db.commit()
    db.commit()
    return {'done'}


@app.post("/question/post/BMLT/Botany", status_code=status.HTTP_201_CREATED, tags=['BMLT'])
def post_question(request: BMLT, db: Session = Depends(get_db),):

    new_blog = models.BMLT_Botany(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                  answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/BMLT/Botany", status_code=status.HTTP_200_OK, tags=['BMLT'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.BMLT_Botany).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/BMLT/Botany/", status_code=status.HTTP_201_CREATED, tags=['BMLT'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.BMLT_Botany).filter(models.BMLT_Botany.question ==
                                        question).delete(synchronize_session=False)
    db.commit()
    db.commit()

    return {'done'}


@app.post("/question/post/BMLT/Chemistry", status_code=status.HTTP_201_CREATED, tags=['BMLT'])
def post_question(request: BMLT, db: Session = Depends(get_db),):

    new_blog = models.BMLT_Chemistry(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                     answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/BMLT/Chemistry", status_code=status.HTTP_200_OK, tags=['BMLT'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.BMLT_Chemistry).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/BMLT/Chemistry/", status_code=status.HTTP_201_CREATED, tags=['BMLT'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.BMLT_Chemistry).filter(
        models.BMLT_Chemistry.question == question).delete(synchronize_session=False)
    db.commit()
    db.commit()

    return {'done'}


@app.post("/question/post/BMLT/MAT", status_code=status.HTTP_201_CREATED, tags=['BMLT'])
def post_question(request: BMLT, db: Session = Depends(get_db),):

    new_blog = models.BMLT_MAT(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                               answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/BMLT/MAT", status_code=status.HTTP_200_OK, tags=['BMLT'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.BMLT_MAT).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/BMLT/MAT/", status_code=status.HTTP_201_CREATED, tags=['BMLT'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.BMLT_MAT).filter(models.BMLT_MAT.question ==
                                     question).delete(synchronize_session=False)
    db.commit()

    return {'done'}


@app.post("/question/post/Agriculture/English", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def post_question(request: Agriculture, db: Session = Depends(get_db),):

    new_blog = models.Agriculture_English(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                          answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Agriculture/English", status_code=status.HTTP_200_OK, tags=['Agriculture'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Agriculture_English).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Agriculture/English/", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Agriculture_English).filter(
        models.Agriculture_English.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/Agriculture/Physics", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def post_question(request: Agriculture, db: Session = Depends(get_db),):

    new_blog = models.Agriculture_Physics(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                          answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Agriculture/Physics", status_code=status.HTTP_200_OK, tags=['Agriculture'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Agriculture_Physics).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Agriculture/Physics/", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Agriculture_Physics).filter(
        models.Agriculture_Physics.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/Agriculture/Chemistry", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def post_question(request: Agriculture, db: Session = Depends(get_db),):

    new_blog = models.Agriculture_Chemistry(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                            answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Agriculture/Chemistry", status_code=status.HTTP_200_OK, tags=['Agriculture'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Agriculture_Chemistry).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Agriculture/Chemistry/", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Agriculture_Chemistry).filter(
        models.Agriculture_Chemistry.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/Agriculture/Maths", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def post_question(request: Agriculture, db: Session = Depends(get_db),):

    new_blog = models.Agriculture_Maths(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                        answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Agriculture/Maths", status_code=status.HTTP_200_OK, tags=['Agriculture'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Agriculture_Maths).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Agriculture/Maths/", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Agriculture_Maths).filter(
        models.Agriculture_Maths.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/Agriculture/Botany", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def post_question(request: Agriculture, db: Session = Depends(get_db),):

    new_blog = models.Agriculture_Botany(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                         answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Agriculture/Botany", status_code=status.HTTP_200_OK, tags=['Agriculture'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Agriculture_Botany).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Agriculture/Botany/", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Agriculture_Botany).filter(
        models.Agriculture_Botany.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/Agriculture/Zoology", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def post_question(request: Agriculture, db: Session = Depends(get_db),):

    new_blog = models.Agriculture_Zoology(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                          answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Agriculture/Zoology", status_code=status.HTTP_200_OK, tags=['Agriculture'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Agriculture_Zoology).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Agriculture/Zoology/", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Agriculture_Zoology).filter(
        models.Agriculture_Zoology.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/Agriculture/GK", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def post_question(request: Agriculture, db: Session = Depends(get_db),):

    new_blog = models.Agriculture_GK(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                     answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Agriculture/GK", status_code=status.HTTP_200_OK, tags=['Agriculture'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Agriculture_GK).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Agriculture/GK/", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Agriculture_GK).filter(
        models.Agriculture_GK.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/Agriculture/Relevant Science", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def post_question(request: Agriculture, db: Session = Depends(get_db),):

    new_blog = models.Agriculture_Relevant_Science(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                                   answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Agriculture/Relevant Science", status_code=status.HTTP_200_OK, tags=['Agriculture'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Agriculture_Relevant_Science).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Agriculture/Relevant Science/", status_code=status.HTTP_201_CREATED, tags=['Agriculture'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Agriculture_Relevant_Science).filter(
        models.Agriculture_Relevant_Science.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/Nursing License/Integrated Science", status_code=status.HTTP_201_CREATED, tags=['Nursing_License'])
def post_question(request: Nursing_License, db: Session = Depends(get_db),):

    new_blog = models.Nursing_License_Integrated_Science(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                                         answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Nursing License/Integrated Science", status_code=status.HTTP_100_CONTINUE, tags=['Nursing_License'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Nursing_License_Integrated_Science).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Nursing License/Integrated Science/", status_code=status.HTTP_202_ACCEPTED, tags=['Nursing_License'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Nursing_License_Integrated_Science).filter(
        models.Nursing_License_Integrated_Science.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/Nursing License/Community Health Nursing", status_code=status.HTTP_201_CREATED, tags=['Nursing_License'])
def post_question(request: Nursing_License, db: Session = Depends(get_db),):

    new_blog = models.Nursing_License_Community_Health_Nursing(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                                               answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Nursing License/Community Health Nursing", status_code=status.HTTP_200_OK, tags=['Nursing_License'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Nursing_License_Community_Health_Nursing).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Nursing License/Community Health Nursing/", status_code=status.HTTP_202_ACCEPTED, tags=['Nursing_License'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Nursing_License_Community_Health_Nursing).filter(
        models.Nursing_License_Community_Health_Nursing.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/Nursing License/Fundamental of Nursing", status_code=status.HTTP_201_CREATED, tags=['Nursing_License'])
def post_question(request: Nursing_License, db: Session = Depends(get_db),):

    new_blog = models.Nursing_License_Fundamental_of_Nursing(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                                             answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Nursing License/Fundamental of Nursing", status_code=status.HTTP_202_ACCEPTED, tags=['Nursing_License'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Nursing_License_Fundamental_of_Nursing).delete()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Nursing License/Fundamental of Nursing/", status_code=status.HTTP_202_ACCEPTED, tags=['Nursing_License'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Nursing_License_Fundamental_of_Nursing).filter(
        models.Nursing_License_Fundamental_of_Nursing.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/Nursing License/Adult Nursing", status_code=status.HTTP_201_CREATED, tags=['Nursing_License'])
def post_question(request: Nursing_License, db: Session = Depends(get_db),):

    new_blog = models.Nursing_License_Adult_Nursing(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                                    answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Nursing License/Adult Nursing", status_code=status.HTTP_200_OK, tags=['Nursing_License'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Nursing_License_Adult_Nursing).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Nursing License/Adult Nursing/", status_code=status.HTTP_201_CREATED, tags=['Nursing_License'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Nursing_License_Adult_Nursing).filter(
        models.Nursing_License_Adult_Nursing.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/Nursing License/Child Health Nursing", status_code=status.HTTP_201_CREATED, tags=['Nursing_License'])
def post_question(request: Nursing_License, db: Session = Depends(get_db),):

    new_blog = models.Nursing_License_Child_Health_Nursing(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                                           answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Nursing License/Child Health Nursing", status_code=status.HTTP_200_OK, tags=['Nursing_License'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Nursing_License_Child_Health_Nursing).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Nursing License/Child Health Nursing/", status_code=status.HTTP_201_CREATED, tags=['Nursing_License'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Nursing_License_Child_Health_Nursing).filter(
        models.Nursing_License_Child_Health_Nursing.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/Nursing License/Midwifery and Gynecology", status_code=status.HTTP_201_CREATED, tags=['Nursing_License'])
def post_question(request: Nursing_License, db: Session = Depends(get_db),):

    new_blog = models.Nursing_License_Midwifery_and_Gynecology(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                                               answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Nursing License/Midwifery and Gynecology", status_code=status.HTTP_200_OK, tags=['Nursing_License'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Nursing_License_Midwifery_and_Gynecology).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Nursing License/Midwifery and Gynecology/", status_code=status.HTTP_201_CREATED, tags=['Nursing_License'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Nursing_License_Midwifery_and_Gynecology).filter(
        models.Nursing_License_Midwifery_and_Gynecology.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}


@app.post("/question/post/Nursing License/Leadership and Management", status_code=status.HTTP_201_CREATED, tags=['Nursing_License'])
def post_question(request: Nursing_License, db: Session = Depends(get_db),):

    new_blog = models.Nursing_License_Leadership_and_Management(question=request.question, answer_1=request.answer_1, answer_2=request.answer_2,
                                                                answer_3=request.answer_3, answer_4=request.answer_4, correct=request.correct,)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/question/get/Nursing License/Leadership and Management", status_code=status.HTTP_200_OK, tags=['Nursing_License'])
def get_question(response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Nursing_License_Leadership_and_Management).all()
    response.headers["Access-Control-Allow-Origin"] = "*"
    if (len(blogs) > 20):
        blog = choices(blogs, k=21)
        blogs = blog

    # header("Access-Control-Allow-Origin: *");
    return blogs


@app.delete("/question/delete/Nursing License/Leadership and Management/", status_code=status.HTTP_201_CREATED, tags=['Nursing_License'])
def delete_question(question: str, db: Session = Depends(get_db),):

    db.query(models.Nursing_License_Leadership_and_Management).filter(
        models.Nursing_License_Leadership_and_Management.question == question).delete(synchronize_session=False)
    db.commit()
    return {'done'}
