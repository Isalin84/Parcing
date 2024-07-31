import scrapy

class LightingSpider(scrapy.Spider):
    name = "lightingspider"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/svet"]

    def parse(self, response):
        # Создаём переменную, в которую будет сохраняться информация
        products = response.css('div[data-testid="product-card"]')
        # Настраиваем работу с каждым отдельным источником освещения в списке
        for product in products:
            # Используем оператор "yield" для извлечения данных
            yield {
                # Извлекаем название источника освещения
                'name': product.css('span[itemprop="name"]::text').get(),
                # Извлекаем цену источника освещения
                'price': product.css('meta[itemprop="price"]::attr(content)').get(),
                # Извлекаем ссылку на источник освещения
                'url': product.css('a.ui-GPFV8.qUioe.ProductName.ActiveProductName::attr(href)').get()
            }

