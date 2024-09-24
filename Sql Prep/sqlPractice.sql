-- Querie 1 : Return the first names and cities of users with specific permissions and access to the dashboard.
select first_name, city 
from users
where permission="admin"
and access="dashboard"; 

-- Querie 2 : Write a query to find all users who have access to a certain feature.
SELECT user_id
FROM UserFeatures
WHERE feature_name = 'premium_feature'
AND has_access = true;

-- Querie 3: Return a list of users with multiple roles.
SELECT user_id 
FROM UserRoles
GROUP BY user_id
HAVING COUNT(DISTINCT role)>1;

-- Querie 4: Write a SQL query to find the total amount spent by each customer who has made more than 5 orders.
SELECT customer_id, SUM(amount) AS total_spent
FROM Orders
GROUP BY customer_id
HAVING COUNT(order_id) > 5;



