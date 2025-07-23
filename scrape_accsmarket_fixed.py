import requests
from bs4 import BeautifulSoup
import json
import re
import time

def scrape_accsmarket():
    url = "https://accsmarket.com/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        categories_data = []
        subcategories_data = []
        products_data = []

        category_id_counter = 1
        product_id_counter = 1

        # Find all category sections
        # Categories are typically found in <h2> tags with a specific class or structure
        # From the HTML, it looks like categories are within <h2> tags, and subcategories are within <a> tags inside a div with class 'category-block'
        
        # Let's try to find all 'category-block' divs
        category_blocks = soup.find_all('div', class_='category-block')

        for block in category_blocks:
            # Extract main category name from <h2> tag within the block
            main_category_tag = block.find('h2')
            if main_category_tag:
                main_category_name = main_category_tag.get_text(strip=True)
                main_category_slug = re.sub(r'[^a-z0-9]+', '-', main_category_name.lower())
                
                # Ensure slug is not too long
                if len(main_category_slug) > 255:
                    main_category_slug = main_category_slug[:255]

                # Add main category if not already added
                if not any(cat['slug'] == main_category_slug for cat in categories_data):
                    categories_data.append({
                        "id": category_id_counter,
                        "name": main_category_name,
                        "slug": main_category_slug,
                        "description": f"{main_category_name} accounts for social media marketing"
                    })
                    current_main_category_id = category_id_counter
                    category_id_counter += 1
                else:
                    current_main_category_id = next(cat['id'] for cat in categories_data if cat['slug'] == main_category_slug)

                # Extract subcategories within this block
                subcategory_links = block.find_all('a', class_='category-link') # Assuming subcategory links have this class
                for sub_link in subcategory_links:
                    subcategory_name = sub_link.get_text(strip=True)
                    subcategory_slug = re.sub(r'[^a-z0-9]+', '-', subcategory_name.lower())
                    
                    # Ensure slug is not too long
                    if len(subcategory_slug) > 255:
                        subcategory_slug = subcategory_slug[:255]

                    if not any(sub['slug'] == subcategory_slug for sub in subcategories_data):
                        subcategories_data.append({
                            "id": category_id_counter,
                            "name": subcategory_name,
                            "slug": subcategory_slug,
                            "description": f"{main_category_name} {subcategory_name} accounts",
                            "parent_id": current_main_category_id
                        })
                        category_id_counter += 1

        # Now, extract products
        product_items = soup.find_all('div', class_='product-item') # Assuming product items have this class

        for item in product_items:
            # Extract product name
            name_tag = item.find('div', class_='product-name')
            product_name = name_tag.get_text(strip=True) if name_tag else "No Name"

            # Extract description (often in a sibling or child element)
            description_tag = item.find('div', class_='product-description') # Assuming a class for description
            description = description_tag.get_text(strip=True) if description_tag else product_name

            # Extract price
            price_tag = item.find('span', class_='price') # Assuming a class for price
            price = 0.0
            if price_tag:
                price_match = re.search(r'\$(\d+\.?\d*)', price_tag.get_text(strip=True))
                if price_match:
                    price = float(price_match.group(1))
            
            # Extract stock quantity
            stock_tag = item.find('span', class_='stock-quantity') # Assuming a class for stock
            stock_quantity = 0
            if stock_tag:
                stock_match = re.search(r'(\d+)', stock_tag.get_text(strip=True))
                if stock_match:
                    stock_quantity = int(stock_match.group(1))

            # Extract rating (assuming a common pattern like '4.5 stars' or '4.5/5')
            rating_tag = item.find('div', class_='rating') # Assuming a class for rating
            rating = 0.0
            if rating_tag:
                rating_match = re.search(r'(\d+\.?\d*)', rating_tag.get_text(strip=True))
                if rating_match:
                    rating = float(rating_match.group(1))

            # Try to infer category from product name or surrounding elements
            assigned_category_id = None
            for cat in categories_data:
                if cat['name'].lower() in product_name.lower():
                    assigned_category_id = cat['id']
                    break
            
            # If no direct category match, try to find a subcategory match
            if not assigned_category_id:
                for sub_cat in subcategories_data:
                    if sub_cat['name'].lower() in product_name.lower():
                        assigned_category_id = sub_cat['id']
                        break

            # Fallback to a default category if nothing found
            if not assigned_category_id and categories_data:
                assigned_category_id = categories_data[0]['id'] # Assign to first category if no match

            if assigned_category_id:
                products_data.append({
                    "id": product_id_counter,
                    "category_id": assigned_category_id,
                    "name": product_name,
                    "description": description,
                    "base_price": price if price > 0 else 0.5,  # Default price
                    "stock_quantity": stock_quantity if stock_quantity > 0 else 100,  # Default stock
                    "rating": rating if rating > 0 else 4.5,  # Default rating
                    "return_rate": 2.0,  # Default return rate
                    "delivery_time": "48h",  # Default delivery time
                    "is_active": True
                })
                product_id_counter += 1

        # Write to JSON files in the correct directory
        import os
        data_dir = "src/data"
        os.makedirs(data_dir, exist_ok=True)
        
        with open(f"{data_dir}/categories.json", "w") as f:
            json.dump(categories_data, f, indent=4)
        with open(f"{data_dir}/subcategories.json", "w") as f:
            json.dump(subcategories_data, f, indent=4)
        with open(f"{data_dir}/products.json", "w") as f:
            json.dump(products_data, f, indent=4)

        print(f"Scraping complete!")
        print(f"Categories: {len(categories_data)}")
        print(f"Subcategories: {len(subcategories_data)}")
        print(f"Products: {len(products_data)}")
        print("Data saved to src/data/ directory")

    except Exception as e:
        print(f"Error during scraping: {e}")
        return

if __name__ == "__main__":
    scrape_accsmarket()



