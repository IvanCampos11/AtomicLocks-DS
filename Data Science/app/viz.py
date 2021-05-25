"""Data visualization functions"""

from fastapi import APIRouter

router = APIRouter()


@router.get('/viz')
async def predict():
    """returns 200000. Legit nothing else."""
    y_pred = 'E'
    return {'here your viz': y_pred}