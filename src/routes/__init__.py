from fastapi import APIRouter
from src.models.models import IprCalcRequest, IprCalcResponse

main_router = APIRouter(prefix="/ipr", tags=["IPR"])


@main_router.post("/calc", response_model=IprCalcResponse)
async def my_profile(ipr_in: IprCalcRequest):
    """Эндпоинт расчёта IPR"""
    from src.calculations.vogel_ipr import calc_ipr
    parsed = ipr_in.dict()
    result = calc_ipr(parsed['p_res'], parsed['pi'], parsed['wct'], parsed['pb'])
    return result
    pass
