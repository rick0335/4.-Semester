from sharpify import httpGet;

class TestController:

    @httpGet
    def Index():
        return "asd";