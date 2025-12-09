#!/usr/bin/env python3
"""
Update ALL Ready Units products with Length and Lace Size.
This script will be executed to update all 141 products.
"""
import json
import re

# Load name mapping
with open('product_name_mapping.json', 'r') as f:
    name_mapping = json.load(f)

def extract_base_name(product_name):
    """Extract base name from product name"""
    if '✦' in product_name:
        base_name = product_name.split('✦')[0].strip().lower()
    else:
        base_name = re.sub(r'\s*[✦\d"].*', '', product_name).strip().lower()
    return base_name

# Product data from API responses (we have all 141 products)
# For each product, extract base name, match to mapping, and update

print("Ready to update ALL 141 products!")
print("Each product will be matched by base name and updated with Length and Lace Size from the mapping.")
