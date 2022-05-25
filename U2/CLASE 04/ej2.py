''' La empresa dedicada a la venta de zapatos, ha decidido fabricar zapatos de hombre para la venta online. Los zapatos tienen un valor de $20.000 (cualquier número), pero podría variar según la demanda. 

Si la compra es igual o superior a $40.000 el envío es gratis, en caso contario, debe cancelar un monto extra de $3.000 

Determine el total a pagar por una persona que requiere X cantidad de zapatos. '''

print("VENTA DE ZAPATOS DE HOMBRE")

valorZapato = 20000

compra1 = int(input("Cuántos zapatos desea comprar?"))

compraTotal = compra1 * valorZapato

if compraTotal >= 40000:
  print("total a pagar: ", compraTotal)
  print("envío: $0")
else:
  compraTotal = compraTotal+3000
  print("subtotal productos: $", compraTotal-3000)
  print("envío: $3000")
  print("total a pagar: $", compraTotal)
