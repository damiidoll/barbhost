#!/usr/bin/env python3
"""
Script to update all Ready Units products with Length and Lace Size info sections.
Uses the correct Catalog V1 format: {"product": {"additionalInfoSections": [...]}}
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
        # Fallback: extract name before any numbers or quotes
        base_name = re.sub(r'\s*[✦\d"].*', '', product_name).strip().lower()
    return base_name

print(f"Loaded {len(name_mapping)} products from mapping")
print("\nSample mappings:")
for i, (name, data) in enumerate(list(name_mapping.items())[:5]):
    print(f"  {name}: Length={data['length']}, Lace Size={data['lace_size']}")

# This script prepares the update data
# The actual API calls will be made separately
print("\nReady to update products!")
print("Format: {\"product\": {\"additionalInfoSections\": [...]}}")
