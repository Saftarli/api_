from flask_restx import Resource,Namespace


order_namespace = Namespace('orders', description="Namspace for orders")



@order_namespace.route('/orders')
class OrderGetCreate(Resource):

    def get(self0):
        """
            Get all orders
        """
        pass

    def post(self):
        """
            Create a new order  
        """
        pass 

@order_namespace.route('/orders/<int:order_id>')

class GetUpdateDelete(Resource):
    
    def get(self,order_id):
        """
            Retirieve an order by id
        """

        pass


    def put(self,order_id):
        """
            Update an order by id
        """

        pass

    def delete(self,order_id):
            """
                Delete an order wit
            """

            pass
    
@order_namespace.route('/user/<int:user_id>/order/<int:order_id>/')

class GetSpecificOrderByUser(Resource):
     def get(self,user_id,order_id):
          """
            Get a user's specific order 
          """
          pass 
     

@order_namespace.route('/user/<int:user_id>/orders')
class UserOrders(Resource):
     
     def get(self,user_id):
          """
          >Get all order by a specific 
          """

          pass
     
@order_namespace.route('/orders/status/<int:order_id>/')
class UpdateOrdersStatus(Resource):
     def patch(self,order_id):
          """
            Update an order's status
          """

          pass 