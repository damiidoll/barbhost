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

# Load products from the API response (we'll fetch them)
# For now, this script will be used to generate update payloads

print("Ready to update all product descriptions!")
print(f"Total products in mapping: {len(name_mapping)}")
print("\nFor each product:")
print("1. Extract base name from product name")
print("2. Match to name_mapping")
print("3. Update Length and Lace Size section descriptions")
print("4. Keep Texture and Color sections as-is")

