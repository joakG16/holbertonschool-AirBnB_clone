#!/usr/bin/python3
''' Review Class '''
from models.base_model import BaseModel


class Review(BaseModel):
    """ Subclass of BaseModel """
    place_id = ""
    user_id = ""
    text = ""
