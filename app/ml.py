"""Machine learning functions"""

from fastapi import APIRouter

router = APIRouter()


@router.post('/predict')
async def predict():
    """returns 200000. Legit nothing else."""
    y_pred = 200000
    return {'predicted_price': y_pred}
