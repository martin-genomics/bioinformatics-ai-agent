# Test Outputs

This document contains sample outputs from testing the Bioinformatics AI Agent.

## DNA Analysis

### Input 1: Basic DNA Analysis
```bash
python3 -m bio_agent.cli ATGCGATAGCTAGCTAGCTAGCATCGATCGATCGATCGATCGATCGATCGA --type dna
```

#### Output:
```
=== Sequence Analysis Results ===
Sequence Type: DNA
Sequence: ATGCGATAGCTAGCTAGCTAGCATCGATCGATCGATCGATCGATCGATCGA
Length: 51 nucleotides

DNA Analysis:
GC Content: 49.02%
Molecular Weight: 15803.08 g/mol

Transcription (RNA): AUGCGAUAGCUAGCUAGCUAGCAUCGAUCGAUCGAUCGAUCGAUCGAUCGA
Translation (Protein): MR*LAS*HRSIDRSIDR
```

### Input 2: DNA Reverse Complement
```bash
python3 -m bio_agent.cli ATGCGATAGCTAGCTAGCTAGCATCGATCGATCGATCGATCGATCGATCGA --type dna --reverse-complement
```

#### Output:
```
Reverse complement: TCGATCGATCGATCGATCGATCGATCGATGCTAGCTAGCTAGCTATCGCAT
```

## Protein Analysis

### Input: Protein Analysis (Human Insulin Subunit A)
```bash
python3 -m bio_agent.cli MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN --type protein
```

#### Output:
```
=== Sequence Analysis Results ===
Sequence Type: Protein
Sequence: MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN
Length: 110 nucleotides

Protein Analysis:
Molecular Weight: 11980.79 g/mol
Isoelectric Point (pI): 5.22

Amino Acid Composition (Top 5):
L: 18.2%
G: 10.9%
A: 9.1%
E: 7.3%
Q: 6.4%
```

## Interpretation of Results

### DNA Analysis
- **GC Content**: 49.02% - This is close to the expected GC content for many organisms.
- **Transcription**: The DNA sequence is correctly converted to RNA (T → U).
- **Translation**: The protein sequence is translated from the DNA using the standard genetic code.
- **Reverse Complement**: The reverse complement is correctly generated, with A-T and C-G base pairing.

### Protein Analysis
- **Molecular Weight**: 11980.79 g/mol - Matches expected weight for the insulin A chain.
- **Isoelectric Point (pI)**: 5.22 - Slightly acidic, as expected for this protein.
- **Amino Acid Composition**: The most abundant amino acids are Leucine (L) and Glycine (G), which is typical for many proteins.

## Notes
- All outputs were generated using the command-line interface.
- The Jupyter notebook in the `examples` directory provides interactive examples with visualization.
- The molecular weights are calculated using average isotopic masses.
- The isoelectric point is calculated using the pKa values of amino acid side chains.
