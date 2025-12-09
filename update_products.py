#!/usr/bin/env python3
"""
Script to update all Ready Units products with Length and Lace Size info sections.
"""
import json
import sys

# Load the parsed CSV data
with open('products_length_lace.json', 'r') as f:
    csv_data = json.load(f)

# Sample product data structure
# We'll need to fetch all products and match by exportProductId

print(f"Loaded {len(csv_data)} products from CSV data")
print(f"Sample entries:")
for i, (key, value) in enumerate(list(csv_data.items())[:3]):
    print(f"  {key}: Length={value['length']}, Lace Size={value['lace_size']}")

# Example update structure for a product
example_product_id = "product_45"
if example_product_id in csv_data:
    product_info = csv_data[example_product_id]
    
    # Create the two new info sections
    new_sections = [
        {
            "title": "Length",
            "description": product_info['length']
        },
        {
            "title": "Lace Size", 
            "description": product_info['lace_size']
        }
    ]
    
    # Example: if product has existing sections, we'd prepend these
    # For now, just show the structure
    print(f"\nExample update structure for {example_product_id}:")
    print(json.dumps(new_sections, indent=2))

