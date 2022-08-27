from .models import *

ROUTED_MODELS = [RefEquip, RefObj, RefSys]


class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS:
            return 'guide'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS:
            return 'guide'
        return None