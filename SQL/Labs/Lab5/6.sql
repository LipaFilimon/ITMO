SELECT ProductID
FROM Production.Product
WHERE Size > ANY (
  SELECT Size
  FROM Production.Product
    JOIN Purchasing.ProductVendor
      ON Product.ProductID = ProductVendor.ProductID
  WHERE ProductVendor.VendorID = 90
)

--SELECT ProductID
--FROM Production.Product
--Where Size> ANY
--(Select Size
--FROM
--Production.Product P
--JOIN 
--Purchasing.ProductVendor PV
--ON
--P.ProductID=PV.ProductID
--WHERE VendorID=95)

--6)	Получить идентификационные номера продуктов, чьи размеры больше,
-- чем у одного из продуктов, поставляемых поставщиком ID=90

--у него все размеры NULL => ответ 0 строк
--23 строки для Vendor ID95
--нужно select ProductionNumber у которых размероность 35 кол-во продуктво, не равно Null,
-- а значению Null соответствуют все продукты с ID=90
