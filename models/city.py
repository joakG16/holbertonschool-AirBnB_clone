#!/usr/bin/python3
''' City class '''
from models.base_model import BaseModel


class City(BaseModel):
    ''' Subclass of BaseModel '''
    state_id = ""  # this will be the state.id
    name = ""
