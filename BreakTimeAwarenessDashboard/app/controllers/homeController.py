from sharpify import httpGet, View;

class HomeController:

    @httpGet
    def Index():
        return View();