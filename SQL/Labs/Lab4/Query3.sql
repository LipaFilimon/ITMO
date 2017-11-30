SELECT SP1.SalesPersonID AS First_SalesPerson,
       SP2.SalesPersonID AS Second_SalesPerson	   
FROM 
     Sales.SalesPerson AS SP1
JOIN 
     Sales.SalesPerson AS SP2
ON
     SP1.CommissionPct=SP2.CommissionPct
WHERE
     SP1.SalesPersonID <> SP2.SalesPersonID 