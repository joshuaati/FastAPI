import fastapi

router = fastapi.APIRouter()


@router.get("/courses")
async def read_courses():
    return {"courses": []}


@router.post("/courses")
async def create_courses():
    return {"courses": []}


@router.get("/courses/{id}")
async def read_courses():
    return {"courses": []}


@router.patch("/courses/{id}")
async def update_courses():
    return {"courses": []}


@router.delete("/courses/{id}")
async def delete_courses():
    return {"courses": []}