Select MAX (P1.DaysToManufacture), P1.ProductLine
FROM Production.Product P1
GROUP BY P1.ProductLine
HAVING MIN (P1.DaysToManufacture)<
(SELECT MAX (P2.DaysToManufacture)
FROM Production.Product P2
Where Style='U')

--10)	Определить максимальное количество дней на изготовление
-- продукта по линейкам продуктов такое, чтобы оно было меньше 
-- максимального количества дней на изготовление продуктов универсального стиля
--для каждой линейки
--если для каждой линейки 5 строк
--унив. 4
