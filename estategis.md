# EstateGIS Master GIScience
Incontro EstateGIS Master GIScience


## Pillole di Python

### Tipi di dati

**stringhe**

```
master = 'Master GIScience'
university = 'UNIPD'
print(master, university)
```

*operazioni con le stringhe*  

```
print(len(master))
print(master.split())
```

**numeri**

I numeri possono essere di vario tipo, i più comuni sono i numeri:  
* interi: integer  
* decimali: float

```
pop_maschile = 170
pop_femminile = 240

area = 45.6
print(type(area))

print (pop_maschile+ pop_femminile)

densita = (pop_maschile+pop_femminile)/area

print(densita)
```

**liste**
Le liste sono degli oggetti che contengono degli elementi, a differenza delle tuple, si possono aggiornare e modificare. in Python le liste si scrivono tra parentesi quadre []. le Liste possono contenere elementi diversi come numeri, stringhe, anche duplicati, o contenere altre liste etc.  


```
citta = ['Padova', 'Lamon', 'Ispra', 'Sevilla']
print(citta)
```
E' possibile accedere agli elementi della lista  
```
print(citta[0])
print(citta[-1])
```

e aggiungere elementi  

```
citta.append('Torino')
print(citta)

citta.append(4)
print(citta)
```


**tuple**

Le tuple, a differenza delle liste, sono immutabili. Non possono modificare gli elementi presenti in una tupla se non sovrascrivendola. La tupla viene definita usando parentesi tonde ().  

```
lat = 45.4072378
lon = 11.8933948

coordinate = (lat, lon)
print('dove è la sede del Master? ', coordinate)

y= coordinate[0]
x= coordinate[1]

print(y, x)
```

**dizionario**

Un dizionario è un oggetto che ha chiavi e valori, si scrive tra parentesi graffe {}. Si accede agli elementi del dizionario usando la chiave corrispondente.

```
master = {'citta': 'Padova', 'indirizzi':7, 'coordinate':(45.4072378, 11.8933948)}
print(master[citta])
```


### Cicli e condizioni

**Ciclo for**  

I cicli servono ad iterare delle operazioni in una sequenza. La sequenza può essere definita come lista, stringa, tupla o dizionario.  
```
citta = ['Padova', 'Lamon', 'Ispra', 'Sevilla']

for i in citta:
  print(i)
```

**If**


### Funzioni

