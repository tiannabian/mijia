from mijia_app.page.base_page import BasePage
from mijia_app.page.product import Product

from mijia_app.page.business import Business


class Search(BasePage):
    """搜索页PO"""
    def goto_business(self):
        """
        进入商
        :return:
        """
        pass
        return Business(self.driver)

    def goto_store(self):
        """
        进入店
        :return:
        """
        pass

