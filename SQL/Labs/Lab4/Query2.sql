SELECT FirstCard.ContactID, FirstCard.CreditCardID  AS FirstCardID,
       SecondCard.CreditCardID AS SecondCardID
FROM 
     Sales.ContactCreditCard AS FirstCard
JOIN 
     Sales.ContactCreditCard AS SecondCard
ON 
     FirstCard.ContactID = SecondCard.ContactID
WHERE 
     FirstCard.CreditCardID <> SecondCard.CreditCardID
