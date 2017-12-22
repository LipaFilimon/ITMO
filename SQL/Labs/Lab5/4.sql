SELECT VendorID, COUNT (ProductID)
FROM Purchasing.ProductVendor
GROUP BY VendorID
HAVING COUNT (ProductID)>
(Select COUNT (ProductID)
FROM Purchasing.ProductVendor
Where MaxOrderQty IN
(Select Max (MinOrderQty)
From Purchasing.ProductVendor))

--SELECT VendorID
--FROM Purchasing.ProductVendor
--WHERE OnOrderQty > all (
--  SELECT max(MinOrderQty)
--  FROM Purchasing.ProductVendor
--)


--Ответ 16 строк
--4)	Получить список поставщиков (id), поставляющих товаров больше,
-- чем поставщик с максимальной величиной минимально возможного количеств
-- а товара в заказе
--//сделано : min вел??? Max вомзожность
