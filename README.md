# cacharreo-web
Otro proyecto web sin más

## Propósito

Para practicar programación (cosas básicas o como máximo de complejidad media).
También quiero probar temas de observabilidad con Open Telemetry, métricas, trazas, etc.

# Herramientas
Seguramente cambie en el futuro, pero de momento:

* Docker
* Docker compose
* Redis
* Postgres
* Prometheus
* Grafana
...

## ¿Y la app?
Para empezar a practicar, la app será un gestor de torneos de cartas de Yugioh, pero podría valer para cualquier TCG, pero muy a largo plazo.

## Criterios del torneo
1. Gestión de Jugadores
    * Número de jugadores: Aunque no está pensada para torneos grandes (más de 50 personas) se pondrá un máximo de 2049. Las rondas se configuran así:

    | Nº de jugadores           | Nº de rondas (Sistema Suizo)                | Top Cut |
    |-------------------------|-----------------------------------|------------------------------------|
    | 4 - 8                   | 3 Rounds of Swiss                 | Top 1                              |
    | 9 - 16                  | 4 Rounds of Swiss                 | Top 4                              |
    | 17 - 32                 | 5 Rounds of Swiss                 | Top 4                              |
    | 33 - 64                 | 6 Rounds of Swiss                 | Top 8                              |
    | 65 - 128                | 7 Rounds of Swiss                 | Top 8                              |
    | 129 - 256               | 8 Rounds of Swiss                 | Top 16                             |
    | 257 - 512               | 9 Rounds of Swiss                 | Top 16                             |
    | 513 - 1024              | 10 Rounds of Swiss                | Top 32                             |
    | 1025 - 2048             | 11 Rounds of Swiss                | Top 32                             |
    | 2049                    | 12 Rounds of Swiss                | Top 64                             |

2. Puntuación y pairing:
* Victoria: 2 puntos
* Empate: 1 punto
* BYE: Si el número de jugadores es impar, el jugador que se quede fuera tendrá una victoria.

3. Gestión de mazos

En cada torneo cada jugador subirá su deck decklist en formato PDF oficial de Konami. El sistema comprobará que el mazo cumple con los requisitos.

4. Documentación técnica
* [Base de datos](docs/postgres-config.md)

## Enlaces de interés

* [YGOPRODECK API](https://ygoprodeck.com/api-guide/) -> Permite buscar cartas, estado (prohibidas, limitada, semilimitadas o normales).
* [Políticas de Konami](https://www.yugioh-card.com/en/events/organizedplay/) -> Aquí se tiene la documentación oficial