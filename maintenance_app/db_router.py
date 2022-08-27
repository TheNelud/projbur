from .models import *

ROUTED_MODELS = [ToRepairs, ToServices, ToShedule]


class MyDBRouter(object):

    def db_for_read(self, model, **hints):
        if model in ROUTED_MODELS:
            return 'tor'
        return None

    def db_for_write(self, model, **hints):
        if model in ROUTED_MODELS:
            return 'tor'
        return None