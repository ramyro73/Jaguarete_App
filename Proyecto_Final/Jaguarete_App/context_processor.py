
def importe_total_carrito(request):
       total=0
       if 'carrito' in request.session:
              if request.user.is_authenticated:
                     for key, value in request.session["carrito"].items():
                            total= total+float(value["precio"])
                     
                     return {"importe_total_carrito":total}
       
       return {"importe_total_carrito":total}