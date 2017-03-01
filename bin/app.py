# -*- coding: utf-8 -*-

import web
import json

list_products = []
urls = ('/', 'Carrinho',
        '/carrinho/(?P<item_id>\d+)/', 'CarrinhoItem')

class Carrinho:
    def GET(self):
        if list_products:
            return json.dumps(
                    {'content': list_products})
        else:
            return json.dumps(
                {'content': "No items found"})

    def POST(self):
        product_id = int(web.input().get('product_id'))
        qtd = int(web.input().get('qtd'))
        item_id = len(list_products) + 1
        if product_id and qtd:
            item = {
                'product_id': product_id,
                'qtd': qtd,
                'item_id': item_id
            }
            list_products.append(item)
            return json.dumps(
                    {'content': item})

class CarrinhoItem:
    def get_item(self, item_id):
        item_id = int(item_id)
        for item in list_products:
            if item['item_id'] == item_id:
                return item
        return None

    def GET(self, item_id):
        item = self.get_item(item_id)
        if item:
            return json.dumps(
                {'content': item})
        else:
            return json.dumps(
                {'content': "Item not found"})

    def DELETE(self, item_id):
        item = self.get_item(item_id)
        if item:
            list_products.remove(item)
            return json.dumps(
                {'content': "ok"})
        return json.dumps(
            {'content': "Item not found"})

    def PUT(self, item_id):
        item = self.get_item(item_id)
        qtd = int(web.input().get('qtd'))
        if item:
            if qtd:
                item['qtd'] = qtd
                return json.dumps(
                    {'content': item})
        return json.dumps(
            {'content': "Item not found"})


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
