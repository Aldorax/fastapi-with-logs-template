from sqlalchemy.orm import Session
from . import models, schemas
import logging

logger = logging.getLogger("fastapi-logger")


def get_item(db: Session, item_id: int):
    logger.info(f"Fetching item with ID: {item_id}")
    return db.query(models.Item).filter(models.Item.id == item_id).first()


def create_item(db: Session, item: schemas.ItemCreate):
    logger.info(f"Creating item with data: {item}")
    db_item = models.Item(name=item.name, description=item.description)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    logger.info(f"Item created with ID: {db_item.id}")
    return db_item
