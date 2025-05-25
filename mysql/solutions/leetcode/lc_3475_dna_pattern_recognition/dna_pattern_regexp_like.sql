SELECT
    sample_id,
    dna_sequence,
    species,
    REGEXP_LIKE(dna_sequence, "^ATG.*$") AS has_start,
    REGEXP_LIKE(dna_sequence, "^.*?(TAA|TAG|TGA)$") AS has_stop,
    REGEXP_LIKE(dna_sequence, "^.*?ATAT.*$") AS has_atat,
    REGEXP_LIKE(dna_sequence, "^.*?G{3,}.*$") AS has_ggg
FROM
    Samples