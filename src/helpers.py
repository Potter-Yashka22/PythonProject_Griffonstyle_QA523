import random
def generate_random_email(base_name="akakiy"):
    random_number=random.randint(100,999)
    return f"{base_name}_{random_number}@griffonstyle.ru"


def validate_category_id(category_id):
    if not isinstance(category_id,str):
        return False
    return len(category_id)>0


def clean_search_query(raw_query):
    if not isinstance(raw_query, str):
        return ""
    clean_query=raw_query.strip()
    clean_query=clean_query.lower()
    forbidden_chars=[";","DROP","SELECT","'",'"']
    for char in forbidden_chars:
        clean_query=clean_query.replace(char,"")
    return clean_query


def sort_products_by_price(products,direction="asc"):
    if not isinstance(products,list):
        return []
    if direction=="asc":
        return sorted(products,key=lambda x: x.get('price',0))
    elif direction=="desc":
        return sorted(products,key=lambda x: x.get('price',0),reverse=True)
    return products
















