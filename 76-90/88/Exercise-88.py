def display_info(company, **kwargs):
    print(f'Company name: {company}')
    if 'price' in kwargs:
        print(f"Price: $ {kwargs['price']}")
    
    
display_info(company='CD Projekt', price=100)