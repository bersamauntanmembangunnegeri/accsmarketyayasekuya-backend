
import requests
from bs4 import BeautifulSoup
import json
import re

def scrape_accsmarket():
    url = "https://accsmarket.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    categories_data = []
    subcategories_data = []
    products_data = []

    # Extract main categories and subcategories from the dropdown menu
    # This part is tricky as it's a dynamic dropdown. We'll rely on the main page structure for now.
    # The previous browser_navigate output showed h2 tags with links like: ## [Facebook Accounts]() / [Facebook Softregs]()
    # We'll parse these to get categories and subcategories.

    # Extract categories and subcategories from h2 tags on the main page
    category_slug_map = {}
    category_id_counter = 1

    h2_sections = soup.find_all("h2")
    for h2 in h2_sections:
        main_cat_tag = h2.find("a", href=re.compile(r"/category/"))
        sub_cat_tag = h2.find("a", href=re.compile(r"/category/.*/"))

        if main_cat_tag and sub_cat_tag:
            main_cat_name = main_cat_tag.get_text(strip=True).replace(" Accounts", "").strip()
            main_cat_slug = main_cat_name.lower().replace(" ", "-")

            sub_cat_name = sub_cat_tag.get_text(strip=True)
            sub_cat_slug = sub_cat_name.lower().replace(" ", "-")

            # Add main category if not already added
            if main_cat_slug not in category_slug_map:
                categories_data.append({
                    "id": category_id_counter,
                    "name": main_cat_name,
                    "slug": main_cat_slug,
                    "description": f"Accounts for {main_cat_name}"
                })
                category_slug_map[main_cat_slug] = category_id_counter
                category_id_counter += 1
            
            parent_id = category_slug_map[main_cat_slug]

            # Add subcategory
            subcategories_data.append({
                "id": category_id_counter,
                "name": sub_cat_name,
                "slug": sub_cat_slug,
                "description": f"Subcategory for {main_cat_name} - {sub_cat_name}",
                "parent_id": parent_id,
                "parent_slug": main_cat_slug
            })
            category_slug_map[sub_cat_slug] = category_id_counter
            category_id_counter += 1

            # Extract products for this subcategory
            current_element = h2.next_sibling
            while current_element:
                if current_element.name == 'div' and 'product-item' in current_element.get('class', []):
                    name_tag = current_element.find('div', class_='name')
                    desc_tag = current_element.find('div', class_='desc')
                    price_tag = current_element.find('div', class_='price')
                    stock_tag = current_element.find('div', class_='stock')
                    rating_tag = current_element.find('div', class_='rating')
                    return_rate_tag = current_element.find('div', class_='return-rate')
                    delivery_time_tag = current_element.find('div', class_='delivery-time')

                    product_name = name_tag.get_text(strip=True) if name_tag else "N/A"
                    product_description = desc_tag.get_text(strip=True) if desc_tag else "N/A"
                    product_base_price = float(re.search(r'\d+\.?\d*', price_tag.get_text(strip=True)).group()) if price_tag and re.search(r'\d+\.?\d*', price_tag.get_text(strip=True)) else 0.0
                    product_stock_quantity = int(re.search(r'\d+', stock_tag.get_text(strip=True)).group()) if stock_tag and re.search(r'\d+', stock_tag.get_text(strip=True)) else 0
                    product_rating = float(rating_tag.get_text(strip=True)) if rating_tag else 0.0
                    product_return_rate = float(re.search(r'\d+\.?\d*', return_rate_tag.get_text(strip=True)).group()) if return_rate_tag and re.search(r'\d+\.?\d*', return_rate_tag.get_text(strip=True)) else 0.0
                    product_delivery_time = delivery_time_tag.get_text(strip=True) if delivery_time_tag else "N/A"

                    products_data.append({
                        "category_slug": sub_cat_slug,
                        "name": product_name,
                        "description": product_description,
                        "base_price": product_base_price,
                        "stock_quantity": product_stock_quantity,
                        "rating": product_rating,
                        "return_rate": product_return_rate,
                        "delivery_time": product_delivery_time,
                        "is_active": True
                    })
                current_element = current_element.next_sibling

    # Write to JSON files
    with open("categories.json", "w") as f:
        json.dump(categories_data, f, indent=4)
    with open("subcategories.json", "w") as f:
        json.dump(subcategories_data, f, indent=4)
    with open("products.json", "w") as f:
        json.dump(products_data, f, indent=4)

    print("Scraping complete. Data saved to categories.json, subcategories.json, and products.json")

if __name__ == "__main__":
    scrape_accsmarket()


