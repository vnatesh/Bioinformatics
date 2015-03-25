# Bioinformatics

This Repository contains bioinformatic analysis and data extraction scripts.

- SNP_mod.sh and SNP_processing.py files are scripts that take in as input, a file containing the following variables, separated by a space: 
- CHROM	POS	REF	ALT	FILTER	VariantType	Samples	SNPEFF_EFFECT	SNPEFF_IMPACT	SNPEFF_FUNCTIONAL_CLASS	SNPEFF_AMINO_ACID_CHANGE	SNPEFF_GENE_NAME	SNPEFF_TRANSCRIPT_ID	rs_dbSNP141	Ancestral_allele	SIFT_pred	Polyphen2_HDIV_pred	Polyphen2_HVAR_pred	LRT_pred	MutationTaster_pred	MutationAssessor_pred	FATHMM_pred	RadialSVM_pred	LR_pred	Reliability_index	VEST3_rankscore	CADD_phred	REGULOME_SCORE	1000Gp1_AF	ESP6500_AA_AF	ESP6500_EA_AF	HGMD_ID	clinvar_rs	clinvar_clnsig	clinvar_trait	MIM_id	Pathway-ConsensusPathDB	Function_description	Disease_description	MIM_phenotype_id	MIM_disease	Trait_association-GWAS	Expression-egenetics	Expression-GNF_Atlas	P_HI	P_rec	Known_rec_info	Essential_gene	MGI_mouse_gene	MGI_mouse_phenotype	ZFIN_zebrafish_gene	ZFIN_zebrafish_structure	ZFIN_zebrafish_phenotype_quality	ZFIN_zebrafish_phenotype_tag	132.GT	132.AD

-The goal with these two scripts was to narrow down the huge gene variant list to just those variants that were found in our the DNA of patients in the severe-blindness cohort (n=20). 









