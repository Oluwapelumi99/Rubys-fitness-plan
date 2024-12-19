from shop.models import Shop

class Cart():
    def __init__(self, request):
        self.session = request.session

        #get the session key for old users
        cart = self.session.get('session_key')
        
        #if the user is new, create a new session key
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        #Make sure cart is available on all pages
        self.cart = cart

    def add(self, shop):
        shop_id = str(shop.id)
        if shop_id in self.cart:
            pass
        else:
            self.cart[shop_id] = {'price': str(shop.price)}

        self.session.modified = True


    def __len__(self):
        return len(self.cart)


    def get_items(self):
        shop_ids = self.cart.keys()
        shops = Shop.objects.filter(id__in=shop_ids)
        return shops
