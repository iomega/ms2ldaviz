
# Improve db insert speed

```sql
-- queries on feature table without index
-- load_dict_functions.py:add_feature_set():69
-- load_dict_functions.py:add_document_words_set():146  
CREATE INDEX basicviz_feature_name_featureset ON basicviz_feature (name,featureset_id);
```

## mass2motif table

```sql
explain analyze verbose SELECT "basicviz_mass2motif"."id", "basicviz_mass2motif"."name", "basicviz_mass2motif"."experiment_id", "basicviz_mass2motif"."metadata", "basicviz_mass2motif"."linkmotif_id" FROM "basicviz_mass2motif" WHERE ("basicviz_mass2motif"."experiment_id" = 2 AND "basicviz_mass2motif"."name" = 'motif_149');
                                                     QUERY PLAN                                                      
---------------------------------------------------------------------------------------------------------------------
 Seq Scan on public.basicviz_mass2motif  (cost=0.00..8.50 rows=1 width=60) (actual time=0.016..0.075 rows=1 loops=1)
   Output: id, name, experiment_id, metadata, linkmotif_id
   Filter: ((basicviz_mass2motif.experiment_id = 2) AND ((basicviz_mass2motif.name)::text = 'motif_149'::text))
   Rows Removed by Filter: 299
 Planning time: 0.052 ms
 Execution time: 0.084 ms
```

```
CREATE INDEX basicviz_mass2motif_idname_i ON basicviz_mass2motif (experiment_id, name);
```

```sql
explain analyze verbose SELECT "basicviz_mass2motif"."id", "basicviz_mass2motif"."name", "basicviz_mass2motif"."experiment_id", "basicviz_mass2motif"."metadata", "basicviz_mass2motif"."linkmotif_id" FROM "basicviz_mass2motif" WHERE ("basicviz_mass2motif"."experiment_id" = 2 AND "basicviz_mass2motif"."name" = 'motif_149');
                                                                        QUERY PLAN                                                                        
----------------------------------------------------------------------------------------------------------------------------------------------------------
 Index Scan using basicviz_mass2motif_idname_i on public.basicviz_mass2motif  (cost=0.27..8.29 rows=1 width=60) (actual time=0.011..0.012 rows=1 loops=1)
   Output: id, name, experiment_id, metadata, linkmotif_id
   Index Cond: ((basicviz_mass2motif.experiment_id = 2) AND ((basicviz_mass2motif.name)::text = 'motif_149'::text))
 Planning time: 0.120 ms
 Execution time: 0.022 ms

```

## featureinstance

```
explain analyze verbose SELECT "basicviz_featureinstance"."id", "basicviz_featureinstance"."document_id", "basicviz_featureinstance"."feature_id", "basicviz_featureinstance"."intensity" FROM "basicviz_featureinstance" WHERE ("basicviz_featureinstance"."document_id" = 721 AND "basicviz_featureinstance"."feature_id" = 8407);
                                                                             QUERY PLAN                                                                             
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Index Scan using basicviz_featureinstance_860d1885 on public.basicviz_featureinstance  (cost=0.29..8.85 rows=1 width=20) (actual time=0.019..0.022 rows=1 loops=1)
   Output: id, document_id, feature_id, intensity
   Index Cond: (basicviz_featureinstance.document_id = 721)
   Filter: (basicviz_featureinstance.feature_id = 8407)
   Rows Removed by Filter: 44
 Planning time: 0.162 ms
 Execution time: 0.032 ms
(7 rows)
```

```
CREATE INDEX basicviz_featureinstance_docfeat_i ON basicviz_featureinstance (document_id, feature_id);
```

```
explain analyze verbose SELECT "basicviz_featureinstance"."id", "basicviz_featureinstance"."document_id", "basicviz_featureinstance"."feature_id", "basicviz_featureinstance"."intensity" FROM "basicviz_featureinstance" WHERE ("basicviz_featureinstance"."document_id" = 721 AND "basicviz_featureinstance"."feature_id" = 8407);
                                                                             QUERY PLAN                                                                              
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Index Scan using basicviz_featureinstance_docfeat_i on public.basicviz_featureinstance  (cost=0.29..8.31 rows=1 width=20) (actual time=0.027..0.028 rows=1 loops=1)
   Output: id, document_id, feature_id, intensity
   Index Cond: ((basicviz_featureinstance.document_id = 721) AND (basicviz_featureinstance.feature_id = 8407))
 Planning time: 0.151 ms
 Execution time: 0.039 ms
(5 rows)
```
```
DROP INDEX basicviz_featureinstance_docfeat_i;
```