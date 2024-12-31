def main():
    snacks = [
        {"code": 1, "Specification": "Cachorro quente", "price": 4.00},
        {"code": 2, "Specification": "X-Salada", "price": 4.50},
        {"code": 3, "Specification": "X-Bacon", "price": 5.00},
        {"code": 4, "Specification": "Torrada Simples", "price": 2.00},
        {"code": 5, "Specification": "Refrigerante", "price": 1.50}
    ]
    
    productcode = int(input("Please, enter the product code: "))
    quantity = int(input("Please, enter the quantity of the product: "))
    
    if productcode < 1 or productcode > 5:
        response = input("Invalid product code. Do you want to see the menu? (Y/N)")
        if response == 'Y':
            for snack in snacks:
                while True:
                    print(f"{snack['code']} | {snack['Specification']} | R$ {snack['price']}")
                    break
            productcode = int(input("Which product do you want to buy? (Enter the code)"))
            quantity = int(input("How many product do you want to buy?"))
            for snack in snacks:
                if snack['code'] == productcode:
                    total = snack['price'] * quantity
                    print(f"---------------------------------------------------")
                    print(f"The product selected is: {snack['Specification']}")
                    print(f"The quantity selected is: {quantity}")
                    print(f"The total price is: R$ {total}")
                    print(f"---------------------------------------------------")
                    print(f"Thank you for your purchase!")
                    exit(0)
        else:
            print("Ok, bye!")
            exit(0)                
    else:
        for snack in snacks:
            if snack['code'] == productcode:
                total = snack['price'] * quantity
                print(f"---------------------------------------------------")
                print(f"The product selected is: {snack['Specification']}")
                print(f"The quantity selected is: {quantity}")
                print(f"The total price is: R$ {total}")
                print(f"---------------------------------------------------")
                print(f"Thank you for your purchase!")
                
if __name__ == "__main__":
    main()
    
    
