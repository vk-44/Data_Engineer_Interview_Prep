SELECT category, product, sum_rev
FROM (
    SELECT 
        category,
        product,
        SUM(revenue) AS sum_rev,
        ROW_NUMBER() OVER (PARTITION BY category ORDER BY SUM(revenue) DESC) AS rn
    FROM products
    GROUP BY category, product
) t
WHERE rn <= 3;
