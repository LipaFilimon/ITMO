Select O1.CustomerID, O1.OrderDate, O1.SalesOrderID
FROM Sales.SalesOrderHeader O1
WHERE OrderDate = 
(Select MAX (OrderDate)
From Sales.SalesOrderHeader
WHERE CustomerID=O1.CustomerID)
ORDER BY O1.CustomerID, O1.SalesOrderID

--5)	Определить для каждого покупателя все заказы (ID),
-- сформированные в день оформления последнего заказа, отсортировать 
-- по идентификационному номеру покупателю

--19127 – для всех покупателей сразу
--последний заказ, полученный чел. = 40
--все заказы на последнюю дату – 103
