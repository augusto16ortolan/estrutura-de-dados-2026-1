from Marca import Marca
from Produto import Produto

produto1 = Produto("Camiseta Internacional 2026", 399.90, 10000, Marca("Adidas", "Fornecedor teste"))
print(produto1.nome)
print(produto1.marca.nome)
produto1.vender(9999)
print(produto1.quantidade)