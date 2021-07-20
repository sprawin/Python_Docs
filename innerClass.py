class Order:
    def __init__(self,orderno,customer,product,quantity,cost,shipmentno,shipaddress,pincode,shipquantiy):
        self.orderno = orderno
        self.customer = customer
        self.orderitem = self.OrderItem(product,quantity,cost)
        self.shipment = self.Shipment(shipmentno,shipaddress,pincode,shipquantiy)
       
    class OrderItem:
        def __init__(self,product,quantity,cost):
            self.product = product
            self.quantity = quantity
            self.cost = cost
    
    class Shipment:
        def __init__(self,shipmentno,shipaddress,pincode,shipquantiy):
            self.shipno = shipmentno
            self.shipaddr = shipaddress
            self.pcode = pincode
            self.shipqty = shipquantiy

orderarray = []         
c1 = Order("N001254","Praveen","A001451",5,3,"S025102","C537 Kurichi Housing Unit Phase 2","641021",5)
orderarray.append(c1)
c1 = Order("N001254","Praveen","H56818",10,898,"S025103","C537 Kurichi Housing Unit Phase 2","641021",5) 
orderarray.append(c1)

for order in orderarray:
    print("Order Detail")
    print(order.orderno, order.customer) 
    print("Order Item Detail")
    print(order.orderitem.product, order.orderitem.quantity, order.orderitem.cost)
    print("Shipment Detail")
    print(order.shipment.shipno, order.shipment.shipaddr,order.shipment.pcode, order.shipment.shipqty)
    print("\n")
            
            