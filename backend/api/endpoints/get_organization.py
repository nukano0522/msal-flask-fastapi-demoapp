from fastapi import APIRouter, Query
from backend.db import get_db_connection

router = APIRouter()


@router.get("/organ", summary="Get user's organization", name="get_organization")
def read_organization(belong: int = Query(..., description="The ID of the organization to filter")):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        select organization from organizations where id=%s
    """
    cursor.execute(query, (belong,))
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return {"organ_name": rows[0]["organization"]}
