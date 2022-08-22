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

## Penalización a la recarga de energía por contaminación
```
y = 0,09x^0,8

y: Penalización (%)

x: Contaminación (uds)
```
> **Nota:** A partir de radiación ```48,5``` el tiempo de recarga es mayor que el tiempo de trabajo automático ```(2%, 12 seg)```, por lo que se deja de conseguir oro.

## Obtención de experiencia de nivel por diferentes actividades

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

## Capacidad de fábricas de recursos por nivel y recurso

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

## Obtención de experiencia laboral por energía trabajada

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