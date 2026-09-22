from Product_Inventory_System import class_module

products = []

for i in range(5):
    print(f"\nEnter details of Product {i + 1}")

    product_id = int(input("Enter Product ID: "))
    product_name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    quantity = int(input("Enter Quantity: "))

    product = class_module.Product(
        product_id,
        product_name,
        price,
        quantity
    )

    products.append(product)

print("\nAll Products:")
for product in products:
    product.display()

print("\nProduct Total Values:")
for product in products:
    print(
        f"{product.product_name} = "
        f"{product.total_value():.0f}"
    )


print("\nLow Stock Products:")
for product in products:
    if product.quantity < 10:
        print(product.product_name)


highest_price_product = max(
    products,
    key=lambda product: product.price
)

print("\nHighest Price Product:")
print(
    f"{highest_price_product.product_name} = "
    f"{highest_price_product.price:.0f}"
)


total_inventory_value = sum(
    product.total_value() for product in products
)

print("\nTotal Inventory Value:")
print(f"{total_inventory_value:.0f}")


search_id = int(input("\nSearch Product Id: "))

found_product = None

for product in products:
    if product.product_id == search_id:
        found_product = product
        break

if found_product:
    print("\nProduct Found:")
    found_product.display()
else:
    print("\nProduct Not Found")
