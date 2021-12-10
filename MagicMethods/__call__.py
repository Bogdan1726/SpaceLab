class CallArea:

    def __call__(self, *args, **kwargs):
        return sum(args)


area = CallArea()
print(f'Method _call__ - {area(3, 5, 4)}')


