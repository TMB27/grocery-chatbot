# stock_db.py

# Sample shop stock (you can replace with actual database)
shop_stock = {
    "rice": 10,
    "dal": 5,
    "oil": 2,
    "salt": 8,
    "tomato": 15,
    "onion": 20
}

def is_item_in_stock(item):
    return item.lower() in shop_stock and shop_stock[item.lower()] > 0

def get_available_items():
    return [item for item, qty in shop_stock.items() if qty > 0]
