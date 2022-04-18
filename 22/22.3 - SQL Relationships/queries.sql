-- write your queries here
-- SELECT * FROM owners JOIN vehicles v ON v.id <> 0;
  -- This Selects all rows regardless of whether there is an owner_id

-- SELECT o.first_name, o.last_name, COUNT(v.owner_id) FROM owners o
-- JOIN vehicles v
-- ON v.ownder_id = o.id
-- GROUP BY o.id
-- ORDER BY o.first_name;
  -- This counts the number of vehicles per owner, ordering them alphabetically from first name A-Z. Let's go!

-- SELECT o.first_name, o.last_name, COUNT(v.owner_id), ROUND(AVG(v.price)) as avg_vehicle_price FROM owners o
-- JOIN vehicles v
-- ON v.owner_id = o.id
-- GROUP BY o.id
-- ORDER BY o.first_name;
  -- This time it adds the average vehicle price of the user :p