from django.apps import AppConfig
# from django.apps import apps


class PagesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pages'
    


# # Get the Product model from your app
# Product = apps.get_model('pages', 'Product')
