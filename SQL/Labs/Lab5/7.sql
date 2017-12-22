SELECT ProductID
FROM Production.Product
WHERE Style NOT IN (
  SELECT Style
  FROM Production.Product
  WHERE ProductSubcategoryID = 1
)

--Select ProductID
--FROM Production.Product
--WHERE Style <> ALL
--(SELECT Style
--FROM Production.Product
--WHERE ProductSubcategoryID=1)

--7)Получить ID продуктов, стиль которых не относится к подкатегории 1
--мне кажется, что нужно сменить не = 1 а неравно 1
--7 строк
