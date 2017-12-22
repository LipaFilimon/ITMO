SELECT SalesOrderID
FROM Sales.SalesOrderHeader
WHERE OrderDate>ALL
(Select OrderDate
FROM 
Sales.SalesOrderHeader OH
JOIN
Sales.SalesOrderDetail OD
ON
OH.SalesOrderID=OD.SalesOrderID
WHERE OD.LineTotal>1000)

--11)Получить номера заказов, созданные позже, 
--чем все заказы с промежуточными итогами за продукт меньше 1000
--ответ 976 строк
