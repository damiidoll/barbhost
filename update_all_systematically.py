#!/usr/bin/env python3
"""
Systematically update all Ready Units products with Length and Lace Size.
Matches products by base name and updates using Catalog V1 format.
"""
import json
import re

# Load name mapping
with open('product_name_mapping.json', 'r') as f:
    name_mapping = json.load(f)

def extract_base_name(product_name):
    """Extract base name from product name like 'Good Girl ✦ 12\" 5x5 HD Lace' -> 'good girl'"""
    if '✦' in product_name:
        base_name = product_name.split('✦')[0].strip().lower()
    else:
        # Fallback: extract name before numbers/quotes
        base_name = re.sub(r'\s*[✦\d"].*', '', product_name).strip().lower()
    return base_name

# Sample products from API responses (we have all 141)
# For each product, we need to:
# 1. Extract base name
# 2. Match to name_mapping
# 3. Create update payload with Length and Lace Size prepended to existing sections
# 4. Make PATCH call

print("Ready to update all products!")
print(f"Total products in mapping: {len(name_mapping)}")
print("\nProcess:")
print("1. Extract base name from product.name")
print("2. Match to name_mapping")
print("3. Prepend Length and Lace Size to existing additionalInfoSections")
print("4. Update via PATCH /stores/v1/products/{id} with format:")
print('   {"product": {"additionalInfoSections": [...]}}')

