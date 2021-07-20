from datetime import date

class Order:
    def __init__(self,orderno,customerno,orderdate):
        self.orderno = orderno
        self.customerno = customerno
        self.orderdate = orderdate

        productlist = []
        product_dict = {}
        while(True):
            prdt = input("Enter Product: ")
            if(prdt == "#$End$#"):
                break
            else:
                qty = int(input("Enter Qty: "))
                unitcost = int(input("Enter Unit Cost: "))
                product_dict = {
                    "product": prdt, "qty": qty, "unitcost": unitcost, "orderno": orderno
                }
                productlist.append(product_dict)

        itemno = 0
        for product in productlist:
            itemno = itemno+1
            print(product['orderno'],itemno,product['product'],product['qty'],product['unitcost'])
            OrderItem(product['orderno'],itemno,product['product'],product['qty'],product['unitcost'])

class OrderItem:
    def __init__(self,orderno,orditmno,product,qty,unitcost):
        self.orderno = orderno
        self.orditmno = orditmno
        self.product = product
        self.qty = qty
        self.unitcost = unitcost
        self.cost = unitcost * qty


class Shipment:
    def __init__(self,shipno,orderno,address):
        self.shipno = shipno
        self.orderno = orderno
        self.address = address


orderno = input("Enter Order Number: ")
customerno = input("Enter customerno: ")
today = date.today()
o1 = Order(orderno,customerno,today)
