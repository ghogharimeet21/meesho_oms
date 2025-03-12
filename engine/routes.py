import os
from flask import Blueprint
from fastapi import APIRouter, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from engine.meesho.orders.utils import order_processor
from engine.meesho.orders.models import Order, Base

router = APIRouter()

engine_bp = Blueprint("engine", __name__, url_prefix="/engine")

# Create the database table
# Base.metadata.create_all(bind=engine)

# def get_db():
#     """Dependency to get a database session."""
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

@router.post("/upload-orders/")
async def upload_orders(file: UploadFile = File(...)):
    """API endpoint to upload and process a CSV file."""
    file_path = f"./uploaded_files/{file.filename}"

    # Save the uploaded file
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Process the orders
    orders_data = order_processor.load_data(file_path)

    # Save orders in the database
    for product, dates in orders_data.items():
        for order_date, sub_orders in dates.items():
            for sub_order_no, packets in sub_orders.items():
                for packet_id, details in packets.items():
                    order = Order(
                        product_name=product,
                        order_date=order_date,
                        sub_order_no=sub_order_no,
                        packet_id=packet_id,
                        size=details.get("Size"),
                        quantity=details.get("Quantity", 1),
                        sku=details.get("SKU"),
                        supplier_price=details.get("Supplier Listed Price (Incl. GST + Commission)", 0.0),
                    )
                    # db.add(order)

    # db.commit()
    return {"message": "Orders processed successfully!", "total_orders": len(orders_data)}
