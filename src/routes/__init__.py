from fastapi import APIRouter
from src.models.models import IprCalcRequest, IprCalcResponse
from src.calculations.vogel_ipr import calc_ipr

main_router = APIRouter(prefix="/ipr", tags=["IPR"])


@main_router.post("/calc", response_model=IprCalcResponse)
async def my_profile(ipr_in: IprCalcRequest):
    """Эндпоинт расчёта IPR"""
    return calc_ipr(ipr_in.p_res, ipr_in.pi, ipr_in.wct, ipr_in.pb)
