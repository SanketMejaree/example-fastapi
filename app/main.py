#Importing Libraries
from fastapi import FastAPI
from . import models
from .database import engine
from .routers import post, user, auth, vote
from fastapi.middleware.cors import CORSMiddleware

#Instance of Fastapi
app = FastAPI()

#CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Connect models to main file
#models.Base.metadata.create_all(bind=engine)

#Routing
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)



# #Functions
# def find_post(id):
#     for post in my_posts:
#         if post['id'] == id:
#             return post

# def find_index_post(id:int):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i


#CRUD Operations for Posts
@app.get("/")
async def root():
    return{"message":"Hello World"}




