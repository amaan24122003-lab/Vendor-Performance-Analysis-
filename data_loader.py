
import pandas as pd
from pathlib import Path

def load_data():

    # Get the folder containing data_loader.py
    base_path = Path(__file__).resolve().parent

    data_path = base_path / "Data"

    begin_inventory = pd.read_csv(data_path / "begin_inventory.csv")
    end_inventory = pd.read_csv(data_path / "end_inventory.csv")
    purchase_prices = pd.read_csv(data_path / "purchase_prices.csv")
    purchases = pd.read_csv(data_path / "purchases.csv")
    vendor_invoice = pd.read_csv(data_path / "vendor_invoice.csv")

    return begin_inventory, end_inventory, purchase_prices, purchases, vendor_invoice

    