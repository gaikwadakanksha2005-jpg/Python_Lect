
orders = [
    {
        'id': 101,
        'customer': 'Asha',
        'status': 'DELIVERED',
        'items': [('keyboard', 2, 1499.0), ('mouse', 1, 599.0)]
    },
    {
        'id': 102,
        'customer': 'Ravi',
        'status': 'CANCELLED',
        'items': [('monitor', 1, 10999.0)]
    },
    {
        'id': 103,
        'customer': 'Asha',
        'status': 'DELIVERED',
        'items': [('cable', 5, 199.0)]
    },
    {
        'id': 104,
        'customer': 'Meera',
        'status': 'SHIPPED',
        'items': [('keyboard', 1, 1499.0), ('monitor', 1, 10999.0)]
    },
    {
        'id': 105,
        'customer': 'Ravi',
        'status': 'DELIVERED',
        'items': [('mouse', 3, 599.0)]
    }
]


def analyse(orders):

    revenue = {}
    products = {}
    all_customers = set()
    not_delivered = set()

    for order in orders:

        customer = order['customer']
        status = order['status']

        all_customers.add(customer)

        if status != 'DELIVERED':
            not_delivered.add(customer)

        if status != 'CANCELLED':

            total = 0

            for item in order['items']:

                name = item[0]
                quantity = item[1]
                price = item[2]

                total = total + quantity * price

                if name in products:
                    products[name] = products[name] + quantity
                else:
                    products[name] = quantity

            if customer in revenue:
                revenue[customer] = revenue[customer] + total
            else:
                revenue[customer] = total

    top_products = sorted(
        products.items(),
        key=lambda x: (-x[1], x[0])
    )[:2]

    fully_delivered = sorted(all_customers - not_delivered)

    return {
        'revenue': revenue,
        'top_products': top_products,
        'fully_delivered': fully_delivered
    }


result = analyse(orders)
print(result)
