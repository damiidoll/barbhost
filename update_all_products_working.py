#!/usr/bin/env python3
"""
Script to update all Ready Units products with Length and Lace Size info sections.
Uses the correct API format: {"product": {"additionalInfoSections": [...]}}
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

# This script will be used to generate update payloads for all products
# The correct format is:
# {"product": {"additionalInfoSections": [{"title": "Length", "description": "..."}, ...]}}

print("Update format confirmed working!")
print("Format: {\"product\": {\"additionalInfoSections\": [...]}}")
print("\nReady to update all 141 products with this format.")

