class Med:
  def __init__(self,medicineId,medicineName,expiryTime,price):
    self.medicineId=medicineId
    self.medicineName=medicineName
    self.expiryTime=expiryTime
    self.price=price
class Medicine:
  def countMedicineByMedicine(arr,medicineName):
    c=0
    for m in arr:
      if m.medicineName.lower()==medicineName.lower():
        c+=1
    return  c
arr=[]
print("Enter number of the values to enter")
n=int(input())
for i in range(n):
  print("enter medicine id,name ,expirytime,price")
  medicineId=int(input())
  medicineName=input()
  expiryTime=int(input())
  price=float(input())
  m = Med(medicineId, medicineName, expiryTime, price)
  arr.append(m)
print("Enter the search value")
search=input()
print(Medicine.countMedicineByMedicine(arr,search))
  
        ```
Enter number of the values to enter
4
enter medicine id,name ,expirytime,price
101
Paracetamol
2027
50.5
102
Dolo
2028
30.0
103
Paracetamol
2029
45.0
104
Crocin
2027
60.0
paracetamol
enter medicine id,name ,expirytime,price
enter medicine id,name ,expirytime,price
enter medicine id,name ,expirytime,price
Enter the search value
2
```
        
