SELECT DISTINCT VendorID
FROM Purchasing.ProductVendor
WHERE ProductID IN (
  SELECT ProductID
  FROM Production.Product
  WHERE Style IN ('W', 'M')
)

--SELECT DISTINCT  PV.VendorID
--FROM Purchasing.ProductVendor PV
--JOIN Production.Product P
--ON PV.ProductID=P.ProductID
--WHERE Style='W'
--AND EXISTS 
--(SELECT P1.ProductID
--FROM Purchasing.ProductVendor PV1
--JOIN Production.Product P1
--ON PV1.ProductID=P1.ProductID
--WHERE Style='M'
--AND PV.VendorID=PV1.VendorID)

--8)Найти тех производителей(ID) товаров для женщин, 
--которые также производят товары для мужчин
--ответ 1 строка, но подписано 102
