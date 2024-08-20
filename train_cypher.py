# Birkaç örnek sorgu ve modelleme yapılandırması.

# parts etiketine sahip düğümlerden part.id'si "19999" olan parçanın ayrıntılarını gösterir. part_name ve part_description özelliklerini birleştirip döndürür ve sonucu response olarak adlandırır.
# part.id'si "19999" olan parçanın tedarikçisini bulur.
# part_id'si "19999" olan parçanın alternatif parçalarını gösterir.

examples = """"
MATCH (p:Parts) WHERE p.part_id = "03109-39" RETURN 'Part Name: ' + p.part_name + ' | Bom Level: ' + p.bom_level AS response

MATCH (p:Parts)-[:SUPPLIED_BY]->(s:Supplier) WHERE p.vendor_id = "VEN-001" RETURN Vendor Name: ' + s.vendor_name AS response LIMIT 1

MATCH (p1)-[:ALTERNATE_TO]->(p2) WHERE b.part_id = "03109-40" RETURN 'Alternate Part: ' + p1.part_id + ' | Part Name: ' + p2.part_name AS response
"""

#  Veritabanındaki düğümlerin hangi özelliklere sahip olacağını ve hangi etiketlerle işaretleneceğini tanımlar.

node_properties = """
[
    {
        "properties": [
            "sku_number",
            "part_id",
            "part_name",
            "qty_persku",
            "currency",
            "part_cost_perunit",
            "total_part_cost_per_sku",
            "part_status",
            "alternate_part_id"
            "bom_level",
            "vendor_id"
        ],
        "labels": "Parts"
    },
    {
        "properties": [
            "sku_number",
            "sku_name",
            "sku_description",
        ],
        "labels": "Sku"
    },
    {
        "properties": [
            "vendor_id",
            "vendor_name",
        ],
        "labels": "Supplier"
    }
]
"""

# Düğümler arasındaki ilişkileri tanımlar.
# source kaynak düğüm türü, target hedef düğüm türüdür.

relationships_props = """
[
    {
        "source": "Parts",
        "relationship": "ALTERNATE_TO",
        "target": [
            "Parts"
        ]
    },
    {
        "source": "Parts",
        "relationship": "SUPPLIED_BY",
        "target": [
            "Supplier"
        ]
    },
    {
        "source": "Supplier",
        "relationship": "HAS",
        "target": [
            "Sku"
        ]
    }
]
"""


# Soru: VEN-001 parçasının vendor name'i nedir
# Cevap: MATCH (p:Parts)-[:SUPPLIED_BY]->(s:Supplier) WHERE p.vendor_id = "VEN-001" RETURN 'Vendor Name: ' + s.vendor_name AS response LIMIT 1

# [
# 0:"Vendor Name: Jstrs"    # 0 ilk cevap olduğunu belirtir. 
# ]