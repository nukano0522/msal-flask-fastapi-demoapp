from fastapi import APIRouter, Query
from backend.db import get_db_connection

router = APIRouter()


@router.get("/members", summary="Get members", name="get_members")
def read_members(belong: int = Query(..., description="The ID of the organization to filter members by")):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT organization, member_name 
        FROM member t1 
        INNER JOIN organizations t2 
        ON t1.organization_id = t2.id 
        WHERE t2.id = %s
    """
    cursor.execute(query, (belong,))
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return {"members": rows}
