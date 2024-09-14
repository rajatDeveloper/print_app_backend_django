from django.urls import path , include 
from my_app.api.views import HistroyListView , PrintCartListView , ProductListView , ProductCreateView , ProductDeleteUpdate , PrintCartCreateView , PrintCartDeleteUpdate , HistoryCreateView
urlpatterns = [

    #histroy url 

    path(
        "history/",
        HistroyListView.as_view(),
        name="history-list",
    ),

      path(
        "history/create/",
        HistoryCreateView.as_view(),
        name="history-create",
    ),


    #product - urls 

    path(
        "products/create/",
        ProductCreateView.as_view(),
        name="product-create",
    ),

    path(
        "products/<int:pk>/",
        ProductDeleteUpdate.as_view(),
        name="product-delete",
    ),
     path(
        "products/",
        ProductListView.as_view(),
        name="product-list",
    ),

    #print -cart url 


    path(
        "print-cart/",
        PrintCartListView.as_view(),
        name="print-cart",
    ),


    path(
        "print-cart/create/",
        PrintCartCreateView.as_view(),
        name="print-cart-create",
    ),

      path(
        "print-cart/<int:pk>/",
        PrintCartDeleteUpdate.as_view(),
        name="print-cart-delete",
    ),

    

   

]


# urlpatterns = [
    
#     path(
#         "users/<int:user_id>/addresses/",
#         AddressListUpdateView.as_view(),
#         name="address-create-get",    
#     ),
#     path(
#         "categories/",
#         CategoryListCreateView.as_view(),
#         name="category-create-get", )   , 
#     path(
#         "rent-request/",
#         RentRequestListCreateView.as_view(),
#         name="rentrequest-create-get", )   , 
#     path(
#         "users/<int:user_id>/rent-post/",
#         RentPostListView.as_view(),
#         name="rent-post-get",    
#     ),
#     path(
#         "users/<int:user_id>/rent-post/create/",
#         RentPostCreateView.as_view(),
#         name="rent-post-create",    
#     ),
#     path(
#         "rent-post/<int:pk>/",
#         RentPostGetSingleView.as_view(),
#         name="rent-single-view",    
#     ),
#     path(
#         "users/<int:user_id>/rent-order/create/",
#         RentOrderCreateView.as_view(),
#         name="rent-post-create",    
#     ),
#     path(
#         "rent-order/<int:pk>/",
#         RentOrderGetUpdateSingleView.as_view(),
#         name="rent-order-view",    
#     ),
#     path(
#         "users/<int:user_id>/rent-order/",
#         RentOrderListView.as_view(),
#         name="rent-order-list-view",    
#     ),
#     path(
#         "users/<int:user_id>/rent-order/owner-user/",
#         RentOrderListOwnerUserView.as_view(),
#         name="rent-order-list-owner-user-view",    
#     ),
#     path(
#         "rent-posts/",
#         RentPostLisAlltView.as_view(),
#         name="rent-post-get-all",    
#     ),

    
#  ] 