# LOAD CSV WITH HEADERS FROM "file:///rfn_parts.csv" AS row
# CREATE (n:Parts)
# SET n = row;

# LOAD CSV WITH HEADERS FROM "file:///rfn_sku.csv" AS row
# CREATE (n:Sku)
# SET n = row;

# LOAD CSV WITH HEADERS FROM "file:///rfn_suppliers.csv" AS row
# CREATE (n:Supplier)
# SET n = row;

# MATCH (p:Parts),(s:Supplier)
# WHERE p.vendor_id = s.vendor_id
# CREATE (p)-[:SUPPLIED_BY]->(s);

# MATCH (p1:Parts), (p2:Parts) 
# WHERE p1.part_id = p2.alternate_part_id 
# CREATE (p2)-[:ALTERNATE_TO]->(p1);