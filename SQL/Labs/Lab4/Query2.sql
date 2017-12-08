SELECT 
       First.CardNumber AS FirstCreditCard, 
	   Second.CardNumber AS SecondCreditCard,
	   ContactID
FROM 
       Sales.CreditCard AS First
JOIN
       Sales.CreditCard AS Second
ON     
       First.CreditCardID=Second.CreditCardID
JOIN 
       Sales.ContactCreditCard AS CCC
ON     
       Second.CreditCardID=CCC.CreditCardID
WHERE  
       First.CardNumber <> Second.CardNumber


       