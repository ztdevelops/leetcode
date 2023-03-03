# Rank functions determine the rank of the value being passed in based on the order.
# dense_rank() is used over rank() because of the 3rd condition.

SELECT s.score,
        dense_rank() over (
                            ORDER BY s.score DESC
                            ) as "rank"
FROM Scores as s;
