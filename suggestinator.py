def suggest(product_idea):
    if len(product_idea) <=3:
        raise ValueError ("Escreva mais de 3 letras")
    return product_idea + "inator"

suggest(product_idea)