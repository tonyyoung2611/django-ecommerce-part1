
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('cart/', views.view_cart, name='view_cart'),
    path(
        'add-to-cart/<int:product_id>/',
        views.add_to_cart,
        name='add_to_cart'
    ),
    path(
        'remove-from-cart/<int:product_id>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),
    path('checkout/', views.checkout, name='checkout'),
    path('register/', views.register, name='register'),


    path(
        'login/',
        auth_views.LoginView.as_view(template_name='shop/login.html'),
        name='login'
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page='product_list'),
        name='logout'
    ),

    path(
        'order-confirmation/<int:order_id>/',
        views.order_confirmation,
        name='order_confirmation'
    ),
    
    path(
        'review/<int:product_id>/',
        views.add_review,
        name='add_review'
    ),

    path(
        'vendor-dashboard/',
        views.vendor_dashboard,
        name='vendor_dashboard'
    ),

    path(
        'create-store/',
        views.create_store,
        name='create_store'
    ),

    path(
        'create-product/',
        views.create_product,
        name='create_product'
    ),

    path(
        'edit-product/<int:product_id>/',
        views.edit_product,
        name='edit_product'
    ),

    path(
        'delete-product/<int:product_id>/',
        views.delete_product,
        name='delete_product'
    ),

    path(
        'edit-store/<int:store_id>/',
        views.edit_store,
        name='edit_store'
    ),

    path(
        'delete-store/<int:store_id>/',
        views.delete_store,
        name='delete_store'
    ),

    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='shop/password_reset.html',
            email_template_name='shop/password_reset_email.html',
            success_url='/password-reset/done/'
        ),
        name='password_reset'
    ),

    path(
        'password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='shop/password_reset_done.html'
        ),
        name='password_reset_done'
    ),

    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='shop/password_reset_confirm.html',
            success_url='/reset/done/'
        ),
        name='password_reset_confirm'
    ),

    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='shop/password_reset_complete.html'
        ),
        name='password_reset_complete'
    ),
]
