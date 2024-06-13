from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db import crud, models, schemas, session
import logging

logger = logging.getLogger("fastapi-logger")

router = APIRouter()


@router.get("/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(session.get_db)):
    logger.info(f"API call to read item with ID: {item_id}")
    item = crud.get_item(db, item_id=item_id)
    if item is None:
        logger.warning(f"Item with ID {item_id} not found")
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@router.post("/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(session.get_db)):
    logger.info(f"API call to create item with data: {item}")
    return crud.create_item(db=db, item=item)
