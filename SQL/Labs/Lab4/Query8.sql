SELECT 
       UnitMeasureCode AS Code,
	   COUNT(*) AS Count
FROM 
       Production.BillOfMaterials

GROUP BY UnitMeasureCode
HAVING UnitMeasureCode = 'EA' OR UnitMeasureCode = 'OZ'