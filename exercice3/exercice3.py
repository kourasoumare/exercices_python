temperatures = [12.5, 14 , 9.5 ,17 , 21 ,19.5 , 11]

#la myenne a 2 decimal 
moy = sum(temperatures) / len(temperatures)
print(f"la Moyenne : {moy:.2f}")

# le minnimum
#min = temperatures[0]
#for i in range (1,7):
 #   if temperatures[i] < temperatures[0]:
   #     min = temperatures[i]


print("Min = ",min(temperatures))
print("Max = ",max(temperatures))

# jour au dessus de 15 °C

compt = 0
for temperature in temperatures:
    if temperature > 15 :
        compt = compt + 1

print("jours > 15 °C : ",compt)        

fahrenheit = []
for temperature in temperatures : 
    fartemp = (temperature * 9/5 + 32)  
    fahrenheit.append(fartemp)
print("fahrenheit : ",fahrenheit)
#enumarate des jours et leur temperature
#for temperature in temperatures:
   # print

for i, temperature in enumerate(temperatures):
    print("jour ",i+1, ": ",temperature, "°C")