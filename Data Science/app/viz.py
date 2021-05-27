"""Data visualization functions"""

from fastapi import APIRouter

router = APIRouter()


@router.get('/viz')
async def viz():
    """This supposed to return a viz but nah"""
    y_pred = 'E'
    return {'here your viz': y_pred}