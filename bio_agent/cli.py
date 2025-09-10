import argparse
from typing import Optional
from .core import BioAgent, SequenceType, AnalysisResult

def print_analysis(result: AnalysisResult) -> None:
    """Print the analysis results in a readable format."""
    print("\n=== Sequence Analysis Results ===")
    print(f"Sequence Type: {result.sequence_type.value}")
    print(f"Sequence: {result.sequence}")
    print(f"Length: {result.length} nucleotides")
    
    if result.sequence_type == SequenceType.DNA:
        print(f"\nDNA Analysis:")
        print(f"GC Content: {result.gc_content:.2f}%")
        print(f"Molecular Weight: {result.molecular_weight:.2f} g/mol")
        print(f"\nTranscription (RNA): {result.transcription}")
        print(f"Translation (Protein): {result.translation}")
    
    elif result.sequence_type == SequenceType.PROTEIN:
        print(f"\nProtein Analysis:")
        print(f"Molecular Weight: {result.molecular_weight:.2f} g/mol")
        print(f"Isoelectric Point (pI): {result.isoelectric_point:.2f}")
        
        if result.amino_acid_composition:
            print("\nAmino Acid Composition (Top 5):")
            sorted_aa = sorted(
                result.amino_acid_composition.items(),
                key=lambda x: x[1],
                reverse=True
            )
            for aa, percentage in sorted_aa[:5]:
                print(f"{aa}: {percentage*100:.1f}%")

def main():
    parser = argparse.ArgumentParser(description='Bioinformatics DNA and Protein Analysis Tool')
    
    # Required arguments
    parser.add_argument('sequence', type=str, help='Input DNA or protein sequence')
    
    # Optional arguments
    parser.add_argument('--type', type=str, choices=['dna', 'protein'], required=True,
                       help='Type of sequence (dna or protein)')
    parser.add_argument('--reverse-complement', action='store_true',
                       help='Get reverse complement (DNA only)')
    
    args = parser.parse_args()
    
    agent = BioAgent()
    
    try:
        if args.type == 'dna':
            if args.reverse_complement:
                rc = agent.get_reverse_complement(args.sequence)
                print(f"Reverse complement: {rc}")
            else:
                result = agent.analyze_sequence(args.sequence, SequenceType.DNA)
                print_analysis(result)
        
        elif args.type == 'protein':
            result = agent.analyze_sequence(args.sequence, SequenceType.PROTEIN)
            print_analysis(result)
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

if __name__ == "__main__":
    main()
