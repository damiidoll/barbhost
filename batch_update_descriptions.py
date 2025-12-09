#!/usr/bin/env python3
"""
Batch update all products with Length and Lace Size descriptions.
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

# Sample product data structure
# We need to:
# 1. Fetch all products
# 2. For each product, extract base name and match to mapping
# 3. Update the descriptions for "Length" and "Lace Size" sections
# 4. Preserve all other sections
# 5. Use format: {"product": {"additionalInfoSections": [...]}}

print("Ready to batch update all product descriptions!")
print(f"Total products in mapping: {len(name_mapping)}")

