# {% extends 'store/base.html' %}
 
# {% block content %}
# <div class="container mx-auto ">
#     <div class="flex justify-between">
#         <h1 class="text-2xl font-semibold mb-6">Checkout</h1>
#         <a href="{% url 'cart' %}" class="inline-block border border-gray-400 rounded-md py-2 px-4 text-gray-700 hover:bg-gray-100 focus:outline-none mb-4"> ← Back to Shopping
#         </a>
#     </div>
    

#     <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
#         <div class="bg-white rounded-md shadow-md p-6">
#             <h2 class="text-xl font-semibold mb-4">Customer Information</h2>
#             <div class="mb-4">
#                 <label for="name" class="block text-gray-700 text-sm font-bold mb-2">Name</label>
#                 <input type="text" id="name" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Your Name">
#             </div>
#             <div class="mb-4">
#                 <label for="email" class="block text-gray-700 text-sm font-bold mb-2">Email Address</label>
#                 <input type="email" id="email" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Your Email">
#             </div>
#             <div class="mb-4">
#                 <label for="phone" class="block text-gray-700 text-sm font-bold mb-2">Phone Number</label>
#                 <input type="tel" id="phone" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Your Phone">
#             </div>

#             <h2 class="text-xl font-semibold mt-6 mb-4">Shipping Address</h2>
#             <div class="mb-4">
#                 <label for="address" class="block text-gray-700 text-sm font-bold mb-2">Address</label>
#                 <input type="text" id="address" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Street Address">
#             </div>
#             <div class="grid grid-cols-2 gap-4 mb-4">
#                 <div>
#                     <label for="city" class="block text-gray-700 text-sm font-bold mb-2">City</label>
#                     <input type="text" id="city" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="City">
#                 </div>
#                 <div>
#                     <label for="state" class="block text-gray-700 text-sm font-bold mb-2">State/Province</label>
#                     <input type="text" id="state" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="State">
#                 </div>
#             </div>
         

#             <h2 class="text-xl font-semibold mt-6 mb-4">Payment Information</h2>
#             <div class="mb-4">
#                 <label class="block text-gray-700 text-sm font-bold mb-2">Payment Method</label>
#                 <div class="space-y-2">
#                     <label class="inline-flex items-center">
#                         <input type="radio" class="form-radio" name="payment_method" value="credit_card">
#                         <span class="ml-2">Credit Card</span>
#                     </label>
#                     <label class="inline-flex items-center">
#                         <input type="radio" class="form-radio" name="payment_method" value="paypal">
#                         <span class="ml-2">PayPal</span>
#                     </label>
#                     </div>
#             </div>
#             <div id="credit_card_details" class="mt-4">
#                 <div class="mb-4">
#                     <label for="card_number" class="block text-gray-700 text-sm font-bold mb-2">Card Number</label>
#                     <input type="text" id="card_number" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="Card Number">
#                 </div>
#                 <div class="grid grid-cols-2 gap-4 mb-4">
#                     <div>
#                         <label for="expiry_date" class="block text-gray-700 text-sm font-bold mb-2">Expiry Date</label>
#                         <input type="text" id="expiry_date" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="MM/YY">
#                     </div>
#                     <div>
#                         <label for="cvv" class="block text-gray-700 text-sm font-bold mb-2">CVV</label>
#                         <input type="text" id="cvv" class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline" placeholder="CVV">
#                     </div>
#                 </div>
#             </div>
#         </div>

#         <div class="bg-white rounded-md shadow-md p-6">
#             <h2 class="text-xl font-semibold mb-4">Order Summary</h2>
#             <ul class="divide-y divide-gray-200">
#                 <li class="py-3 flex justify-between items-center">
#                     <span>Product 1 x 1</span>
#                     <span class="font-semibold">$20.00</span>
#                 </li>
#                 <li class="py-3 flex justify-between items-center">
#                     <span>Another Item x 2</span>
#                     <span class="font-semibold">$30.00</span>
#                 </li>
#                 <li class="py-3 flex justify-between items-center font-semibold">
#                     <span>Subtotal</span>
#                     <span>$50.00</span>
#                 </li>
#                 <li class="py-3 flex justify-between items-center font-semibold">
#                     <span>Shipping</span>
#                     <span>$5.00</span>
#                 </li>
#                 <li class="py-3 flex justify-between items-center font-bold text-lg">
#                     <span>Total</span>
#                     <span>$55.00</span>
#                 </li>
#             </ul>
#             <button class="bg-green-500 hover:bg-green-600 text-white font-semibold py-3 px-6 rounded-md w-full mt-6 focus:outline-none focus:shadow-outline">
#                 Place Order
#             </button>
#         </div>
#     </div>
# </div>

# <script>
#     document.addEventListener('DOMContentLoaded', function() {
#         const creditCardDetails = document.getElementById('credit_card_details');
#         const creditCardRadio = document.querySelector('input[name="payment_method"][value="credit_card"]');
#         const paypalRadio = document.querySelector('input[name="payment_method"][value="paypal"]');

#         if (creditCardRadio && creditCardDetails) {
#             creditCardDetails.style.display = 'none'; // Initially hide credit card details

#             creditCardRadio.addEventListener('change', function() {
#                 creditCardDetails.style.display = this.checked ? 'block' : 'none';
#             });

#             paypalRadio.addEventListener('change', function() {
#                 creditCardDetails.style.display = this.checked ? 'none' : 'block';
#             });
#         }
#     });
# </script>
# {% endblock content %}

# # 