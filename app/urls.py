from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
#Imported to use django made authentication system
from django.contrib.auth import views as auth_views
from .forms import LoginForm, UserPasswordChangeForm,UserPasswordResetForm,UserSetPasswordForm
urlpatterns = [

    path('',views.ProductView.as_view(),name="home"),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(),name='product-detail'),

    #For Cart 
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    # path('pluscart/',views.plus_cart),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.Profileview.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    
    #Password Change 
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='app/passwordchange.html',form_class=UserPasswordChangeForm, success_url='/passwordchangedone/'),name="passwordchange"),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name='passwordchangedone'),
   
    # Password Reset Urls(Forgot Password)
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='app/password_reset.html',form_class=UserPasswordResetForm),name='password_reset'),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='app/password_resetdone.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='app/password_resetconfirm.html',form_class=UserSetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='app/password_resetcomplete.html'),name='password_reset_complete'),
    
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('topwear/', views.topwear, name='topwear'),
    path('topwear/<slug:data>', views.topwear, name='topwear'),
    path('bottomwear/', views.bottomwear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottomwear, name='bottomwear'),

    #Django Made authentication system
    path('registration/',views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path('accounts/login/',auth_views.LoginView.as_view(template_name='app/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    
    
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
