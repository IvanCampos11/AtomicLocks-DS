"""Database functions"""

import os
from psycopg2.extensions import register_adapter, AsIs
from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import psycopg2
from pydantic import BaseModel, Field, validator
import logging

log = logging.getLogger(__name__)
router = APIRouter()

# Load environment variables from .env
load_dotenv(
    "/home/ivancampos/Documents/Programming Stuff/AtomicLocks/Data Science/Data/.env")


class Player_ID(BaseModel):
    playerId: int


class PostgreSQL:
    def __init__(self):

        self.DB_NAME = os.getenv("DB_NAME")
        self.DB_USER = os.getenv("DB_USER")
        self.DB_PASSWORD = os.getenv("DB_PASSWORD")
        self.DB_HOST = os.getenv("DB_HOST")
        self.DB_PORT = os.getenv("DB_PORT")
        self.connection = psycopg2.connect(
            dbname=self.DB_NAME, user=self.DB_USER, password=self.DB_PASSWORD,
            host=self.DB_HOST, port='5432')

    def adapters(*args):
        for adapter in args:
            register_adapter(adapter, psycopg2._psycopg.AsIs)

    def cursor(self):
        self.cursor = self.connection.cursor()

    def execute(self, query):
        self.cursor.execute(query)

    def close(self):
        self.connection.close()

    def fetch_query_records(self, query: str):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def fetch_player_info(self, id_player: int):
        cursor = self.connection.cursor()
        query = """
                SELECT * FROM lcs_players
                WHERE PlayerId =""" + id_player + ";"
        cursor.execute(query)
        result = cursor.fetchall()
        return result


@router.get('/info')
async def get_player_info(players_id):
    """Given the player ID this will return
    all the info from that player in JSON
    """

    # player: float = Field(..., example=3.14)
    # project_code: int = Field(..., example=1014106)
    # x3: str = Field(..., example='banjo')
    
    pg = PostgreSQL()
    fetched_player_info = pg.fetch_player_info(players_id)
    keys = ['Id', 'PlayerId', 'FirstName', 'LastName', 'CommonName', 'MatchName',
            'Position', 'Gender', 'BirthDate', 'BirthCountry', 'Nationality', 'Updated']
    final_player_info = {key: value for key,
                         value in zip(keys, fetched_player_info)}

    return {'Player stuff': final_player_info}
