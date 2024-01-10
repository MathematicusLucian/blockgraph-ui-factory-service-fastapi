from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

# Queries the blockgraph database (Mongo)
# Maybe add Pylint

app = FastAPI()

@app.get("/")
def read_root():
    return {"testing": "api"}

class Component(BaseModel):
    number: float
    content: str
    # Not final structure

class Blockgraph(BaseModel):
    component: Component
    # Not final structure

#--------#
# Skills #
#--------#

# Get the blockgraph tree
@app.get("/get_blockgraph/{id_site}")
def get_blockgraph(id_site: int):
    
    # Traverse the tree/graph of components
    # Any endpoints referred to are queried  
    # Response from endpoints added to the tree (strategy pattern if necessary)
    # JSON returned for attention of Ng component resolver (deprecated; new approach)
    
    return get_blockgraph_components

# Update a Skill
@app.post("/update_blockgraph/{id_site}")
def update_blockgraph(id_site: int):
    return {}

# Add a Skill
# api/add_block/[x]?block=[y]
@app.put("/add_block/{id_site}")
def add_block(id_site: int, component: Component):
    return {}