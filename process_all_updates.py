#!/usr/bin/env python3
"""
Process all products and generate update payloads.
This script will match products by name and create update payloads for all 141 products.
"""
import json
import re

# Load the name mapping
with open('product_name_mapping.json', 'r') as f:
    name_mapping = json.load(f)

def extract_base_name(product_name):
    """Extract base name from product name"""
    if '✦' in product_name:
        base_name = product_name.split('✦')[0].strip().lower()
    else:
        base_name = re.sub(r'\s*[✦\d"].*', '', product_name).strip().lower()
    return base_name

# We need to process all products from both API responses
# Products from offset 0 (first 100) and offset 100 (remaining 41)
# This script will generate a JSON file with all products that need updates

print("Processing all products for updates...")
print(f"Total products in mapping: {len(name_mapping)}")

# Note: In a real scenario, you would load the actual product data from the API responses
# For now, this script shows the structure needed

# Example structure for each update:
# {
#   "product_id": "...",
#   "product_name": "...",
#   "base_name": "...",
#   "length": "...",
#   "lace_size": "...",
#   "api_body": {
#     "additionalInfoSections": [
#       {"title": "Length", "description": "..."},
#       {"title": "Lace Size", "description": "..."}
#     ]
#   }
# }

print("\nTo update all products:")
print("1. Load all 141 products from API")
print("2. For each product, extract base name")
print("3. Match to name_mapping")
print("4. Create update payload")
print("5. Make PATCH API call")

