class StackOverflowMiddleware(object):
    def process_exception(self, request, exception):
        print '\n\n\n\nhello\n\n\n\n'
        return None