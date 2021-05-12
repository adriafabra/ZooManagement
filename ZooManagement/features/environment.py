from splinter.browser import Browser
from ZooWeb.models import Sector 

def before_all(context):
    context.browser = Browser('chrome', headless=False)

def before_scenario(context, scenario):
    Sector.objects.create(name='Freshwater', area_in_square_meters=200)
    Sector.objects.create(name='Mountain', area_in_square_meters=200)

def after_all(context):
    context.browser.quit()
    context.browser = None