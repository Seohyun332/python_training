#!/bin/bash

sample=$1

fq1=${sample}_1.fastq.gz
fq2=${sample}_2.fastq.gz

ls -l ${fq1} ${fq2}
# PROGRAM
BWA="/usr/bin/bwa"
SAMTOOL="/usr/bin/samtools"
PICARD="/home/seohyun/etc/picard/picard.jar"
GATK="/home/seohyun/etc/gatk/gatk-4.5.0.0/gatk-package-4.5.0.0-local.jar"
snpEff="/home/seohyun/etc/snpEff/snpEff.jar"
# REF
REFERENCE="/home/seohyun/etc/reference/chr21.fa.gz"

#files
mapped_sam="${sample}.chr21.sam"
mapped_bam="${sample}.chr21.bam"
sort_bam="${sample}.chr21.sort.bam"
markdup_bam="${sample}.chr21.markdup.bam"
gvcf="${sample}.chr21.g.vcf.gz"
vcf="${sample}.chr21.vcf.gz"
ann_vcf="${sample}.chr21.ann.vcf.gz"
#MAPPING
${BWA} mem -t 1 -R "@RG\tID:sample\tSM:sample\tPL:platform" ${REFERENCE} ${fq1} ${fq2} > ${mapped_sam}

# Change Bam
${SAMTOOL} view -Sb ${mapped_sam} > ${mapped_bam}

# Bam Sort 
${SAMTOOL} sort ${mapped_bam} -o ${sort_bam}

#BAM file INDEXING
${SAMTOOL} index ${sort_bam}

#PICARD - markdup
java -jar ${PICARD} MarkDuplicates -I ${sort_bam} -O ${markdup_bam} -M ${sample}.metrics.txt

#BAM file indexing 
${SAMTOOL} index ${markdup_bam}

#GATK
java -jar ${GATK} HaplotypeCaller -I ${markdup_bam} -O ${gvcf} -R ${REFERENCE} -ERC GVCF 
java -jar ${GATK} GenotypeGVCFs -V ${gvcf} -O ${vcf} -R ${REFERENCE}

#SNPEff

java -jar -Xmx4000m ${snpEff} -v hg38 ${vcf} > ${ann_vcf}
echo " END : `date` " >> ${sample}_log.txt
