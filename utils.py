from timeit import default_timer as timer


class Timer():

    def __enter__(self):
        self.start = timer()

    def __exit__(self, *ex):
        self.result = timer() - self.start
