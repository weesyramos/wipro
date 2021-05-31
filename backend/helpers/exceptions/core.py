
class CoreException(Exception):

    def __init__(self, *args, **kwargs):
        setattr(self, 'args', args)
        for arg in kwargs:
            setattr(self, arg, kwargs[arg])

    def __str__(self):
        return self.__unicode__()

    def __unicode__(self):
        return self.__doc__
