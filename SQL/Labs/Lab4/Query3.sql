SELECT 
       One.SalesPersonID AS First, 
	   Two.SalesPersonID AS Second  
FROM 
       Sales.SalesPerson AS One
JOIN 
       Sales.SalesPerson AS Two
ON
       One.CommissionPct=Two.CommissionPct
WHERE 
       One.SalesPersonID <> Two.SalesPersonID