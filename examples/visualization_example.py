#!/usr/bin/env python3
"""
Amino Acid Composition Visualization Example

This script demonstrates how to use the BioAgent to visualize
amino acid composition of a protein sequence.
"""

from bio_agent.core import BioAgent, SequenceType

# Example protein sequence (Human insulin A chain)
PROTEIN_SEQUENCE = "MALWMRLLPLLALLALWGPDPAAAFVNQHLCGSHLVEALYLVCGERGFFYTPKTRREAEDLQVGQVELGGGPGAGSLQPLALEGSLQKRGIVEQCCTSICSLYQLENYCN"

def main():
    # Initialize the BioAgent
    agent = BioAgent()
    
    # Analyze the protein sequence
    print(f"Analyzing protein sequence: {PROTEIN_SEQUENCE}")
    result = agent.analyze_sequence(PROTEIN_SEQUENCE, SequenceType.PROTEIN)
    
    # Print basic information
    print(f"\nProtein Analysis Results:")
    print(f"Length: {result.length} amino acids")
    print(f"Molecular Weight: {result.molecular_weight:.2f} g/mol")
    print(f"Isoelectric Point (pI): {result.isoelectric_point:.2f}")
    
    # Visualize the amino acid composition
    print("\nDisplaying amino acid composition chart...")
    agent.plot_amino_acid_composition(result.amino_acid_composition)
    
    print("\nVisualization complete!")

if __name__ == "__main__":
    main()
