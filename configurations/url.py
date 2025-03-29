class URL:
    @staticmethod
    def basic_url():
        return "https://letcode.in/"


    @staticmethod
    def alert_url():
        return URL.basic_url()+"alert"

    @staticmethod
    def dropdown_url():
        return URL.basic_url()+"dropdowns"

    @staticmethod
    def element_url():
        return URL.basic_url()+"elements"

    @staticmethod
    def frame_url():
        return URL.basic_url()+"frame"

    @staticmethod
    def window_url():
        return URL.basic_url()+"window"