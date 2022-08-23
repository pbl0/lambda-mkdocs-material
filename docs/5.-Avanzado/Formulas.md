# Fórmulas

## Daño
```
[1 + Índice militar/20 
+ Sistema de Misiles/400 
+ Puerto naval/400 
+ Aeropuerto/400 
+ Academia militar/400 
+ Fuerza/100 
+ Bonus de Nación X 3 
+ (Educación + Aguante + Nivel)/200]
* [α-daño](/4.-Guerras/Daño-alpha/) de las tropas
```



> Por otro lado se resta la penalización por distancia y se multiplica por la variable de error cuyo valor es aleatorio ```(+/- 12,5%)```.

## Penalización por distancia

```
y = 0,017683x^0,9

y: Penalización (%)

x: Distancia (km)

Distancia máxima sin penalización: 500km
```

## Penalización por contaminación
```
y = 0,09x^0,8

y: Penalización (%)

x: Contaminación (uds)
```
> **Nota:** A partir de radiación ```48,5``` el tiempo de recarga es mayor que el tiempo de trabajo automático ```(2%, 12 seg)```, por lo que se deja de conseguir oro.

## Experiencia de nivel

### Trabajo

```
y = 100x

y: Experiencia de nivel (Exp)

x: Energía trabajada (E)
```
### Stats

```
y = 100x

y: Experiencia de nivel (Exp)

x: Nuevo nivel conseguido del stat (uds)
```
### Guerra

```
y = x/3

y: Experiencia de nivel (Exp)

x: Daño producido (uds)
```

## Capacidad de fábricas

### Petróleo

```
y = 40.000.000x

y: Capacidad de la fábrica (bbl)

x: Nivel de la fábrica (uds)
```
### Mineral
```
y = 40.000.000x

y: Capacidad de la fábrica (kilo)

x: Nivel de la fábrica (uds)
```
### Uranio
```
y = 5.000.000x

y: Capacidad de la fábrica (g)

x: Nivel de la fábrica (uds)
```
### Diamante
```
y = 50.000x

y: Capacidad de la fábrica (pcs)

x: Nivel de la fábrica (uds)
```
> **Nota:** Ninguna de ellas presenta un límite de almacenaje de dinero (€).

## Experiencia laboral

- Sin mentores (normal): ```y = x/10```

- Un mentor: ```y = 4x/10```

- Dos mentores: ```y = 6x/10```
```
Experiencia laboral (Exp lab)

x: Energía trabajada (E)
```

> **Nota:** Está fórmula es aplicable tanto para recursos como para oro.

## Bonus de nación por puntos nacionales trabajados en cada categoría de los departamentos
```
x = a/b x 10%

x: Bonus nacional (%)

a: Puntos de tu nación (uds)

b: Puntos de la nación con más puntos (uds)
```

## Daño alpha
```
y = 2.500 x (a + 20)

y: Daño Alpha (uds)
a: Nivel de experiencia (uds)
```

## Almacén

```
y = x * (1 + a/198) * (b) * (1 + (c - 100)/200)

y: Almacenamiento
x: Capacidad inicial
a: Nivel de casa (uds)
b: Nivel de experiencia (uds)
c: Nivel de Resistencia (uds)
```
### Capacidad inicial para Recursos 
- Petróleo:  ```7.200.000```
- Mineral: ```7.200.000```
- Uranio: ```480.000```
- Diamantes: ```1.200```
- Oxigeno Líquido: ```960.000```
- Helio3: ```10.800```

### Capacidad inicial para Recursos:
- AntiRadiación: ```1200```
- Naves Espaciales: ```48```

### Capacidad inicial para Armamento:
- Tanques: ```180.000```
- Aviones de Combate: ```24.000```
- Bombarderos: ```2250```
- Misiles:  ```No Aplica```
- Acorazados: ```900```
- Tanques Lunares: ```900```
- Estación Espacial:  ```360```


## Huecos por nivel de fábrica
> Calculada por **Joan Rovira**
```
y = 0,28x + 0,98

y: Huecos de la fábrica (usuarios)
x: Nivel de fábrica (uds)
```


## Daño inicial en un frente
```
x = 450.000c
y = 50.000a + 100.000b + 450.000c

x: Daño inicial en ataque 
y: Daño inicial en defensa
a: Número de edificios totales (sin viviendas ni academias ni bases militares)
b: Bases militares
c: Academias militares
```

## Coste de construcción de edificios

### Hospitales
- Dinero: ```y = 5.196x^1,5```
- Oro: ```y = 100.388x^1,5```
- Petróleo: ```y = 2.024x^1,5```
- Mineral: ```y = 854x^1,5```

### Bases militares
- Dinero: ```y = 5.196x^1,5```
- Oro: ```y = 100.388x^1,5```
- Petróleo: ```y = 2.024x^1,5```
- Mineral: ```y = 854x^1,5```

### Escuelas
- Dinero: ```y = 5.196x^1,5```
- Oro: ```y = 100.388x^1,5```
- Petróleo: ```y = 2.024x^1,5```
- Mineral: ```y = 854x^1,5```

### Viviendas
- Dinero: ```y = 164x^1,5```
- Oro: ```y = 3.175x^1,5```
- Petróleo: ```y = 64x^1,5```
- Mineral: ```y = 27x^1,5```

### Misiles
- Dinero: ```y = 31.623x^1,5```
- Oro: ```y = 2.415x^1,5```
- Petróleo: ```y = 32x^1,5```
- Mineral: ```y = 32x^1,5```
- Diamantes: ```y = 5x^1,5```

### Aeropuertos
- Dinero: ```y = 31.623x^1,5```
- Oro: ```y = 2.415x^1,5```
- Petróleo: ```y = 32x^1,5```
- Mineral: ```y = 32x^1,5```
- Diamantes: ```y = 5x^1,5```

### Puertos
- Dinero: ```y = 31.623x^1,5```
- Oro: ```y = 2.415x^1,5```
- Petróleo: ```y = 32x^1,5```
- Mineral: ```y = 32x^1,5```
- Diamantes: ```y = 5x^1,5```

### Puertos espaciales
- Dinero: ```y = 464.758x^1,5```
- Oro: ```y = 2.415x^1,5```
- Petróleo: ```y = 164x^1,5```
- Mineral: ```y = 125x^1,5```
- Uranio: ```y = 164x^1,5```
- Diamantes: ```y = 5x^1,5```

### Plantas de energía
- Dinero: ```y = 89.443x^1,5```
- Oro: ```y = 854x^1,5```
- Petróleo: ```y = 125x^1,5```
- Mineral: ```y = 125x^1,5```
- Uranio: ```y = 89x^1,5```
- Diamantes: ```y = 3x^1,5```

```
y: Coste de un edificio más 
x: Número del edificio construido
```