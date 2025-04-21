# summary.py

from stock_db import is_item_in_stock

def generate_order_summary(items_list):
    available = []
    unavailable = []

    for item in items_list:
        item = item.strip().lower()
        if is_item_in_stock(item):
            available.append(item)
        else:
            unavailable.append(item)

    summary = f"Order Summary:\n✅ Available: {', '.join(available)}\n❌ Unavailable: {', '.join(unavailable)}"
    return summary
