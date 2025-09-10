# Bioinformatics AI Agent

A powerful bioinformatics tool for DNA and protein sequence analysis built with Biopython.

## Features

- **DNA Analysis**
  - Calculate GC content
  - Get reverse complement
  - Transcribe DNA to RNA
  - Translate DNA to protein
  - Calculate molecular weight

- **Protein Analysis**
  - Calculate molecular weight
  - Determine isoelectric point (pI)
  - Analyze amino acid composition
  - Visualize amino acid distribution

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd bioinformatics-agent
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command Line Interface

```bash
# Analyze a DNA sequence
python -m bio_agent.cli ATGCGATAGCTAGCTAGCTAGCATCGATCGATCGATCGATCGATCGATCGA --type dna

# Get reverse complement of a DNA sequence
python -m bio_agent.cli ATGCGATAGCTAGCTAGCTAGCATCGATCGATCGATCGATCGATCGATCGA --type dna --reverse-complement

# Analyze a protein sequence
python -m bio_agent.cli MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN --type protein
```

### Jupyter Notebook Example

See the `examples/DNA_Protein_Analysis_Demo.ipynb` notebook for interactive examples of using the BioAgent.

## Python API

```python
from bio_agent.core import BioAgent, SequenceType

# Initialize the agent
agent = BioAgent()

# Analyze a DNA sequence
dna_result = agent.analyze_sequence("ATGCGATAGCTAGCTAGCTAGCATCGATCGATCGATCGATCGATCGATCGA", SequenceType.DNA)
print(f"GC Content: {dna_result.gc_content:.2f}%")
print(f"Protein Translation: {dna_result.translation}")

# Analyze a protein sequence
protein_result = agent.analyze_sequence("MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN", SequenceType.PROTEIN)
print(f"Molecular Weight: {protein_result.molecular_weight:.2f} g/mol")
print(f"Isoelectric Point: {protein_result.isoelectric_point:.2f}")
```

## Project Structure

```
bioinformatics-agent/
├── bio_agent/
│   ├── __init__.py
│   ├── core.py           # Core BioAgent implementation
│   └── cli.py            # Command-line interface
├── examples/
│   └── DNA_Protein_Analysis_Demo.ipynb  # Example usage
├── tests/                # Unit tests (to be implemented)
├── requirements.txt      # Dependencies
└── README.md             # This file
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
