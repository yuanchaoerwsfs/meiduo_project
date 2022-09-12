from poium import Page, PageElement


class poium_BaiduPage(Page):
    """Baidu层"""
    search_input = PageElement(id="kw")
    search_button = PageElement(id="su")
