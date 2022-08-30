from fastapi import APIRouter
from src.models.models import IprCalcRequest, IprCalcResponse
from src.calculations.vogel_ipr import calc_ipr

main_router = APIRouter(prefix="/ipr", tags=["IPR"])


@main_router.post("/calc", response_model=IprCalcResponse)
def post_ipr(ipr_in: IprCalcRequest):
    """
    Эндпоинт расчёта IPR

    :param ipr_in - модель входных параметров пласта
    """
    ipr = calc_ipr(ipr_in.p_res, ipr_in.pi, ipr_in.wct, ipr_in.pb)
    ipr_response = IprCalcResponse(**{
        "q_liq": ipr["q_liq"],
        "p_wf": ipr["p_wf"]
    })
    return ipr_response
