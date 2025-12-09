#!/usr/bin/env python3
"""
Update all products with Length and Lace Size descriptions.
The info sections are already added, we just need to update the descriptions.
"""
import json
import re

# Load the name mapping
with open('product_name_mapping.json', 'r') as f:
    name_mapping = json.load(f)

def extract_base_name(product_name):
    """Extract base name from product name (everything before ✦)"""
    if '✦' in product_name:
        base_name = product_name.split('✦')[0].strip().lower()
    else:
        # Fallback: remove common patterns
        base_name = re.sub(r'\s*[✦\d"].*', '', product_name).strip().lower()
    return base_name

# This script will be used to generate update payloads for all products
# The correct format is:
# {"product": {"additionalInfoSections": [{"title": "Length", "description": "..."}, ...]}}

print("Ready to update all product descriptions!")
print(f"Total products in mapping: {len(name_mapping)}")

