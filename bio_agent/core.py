from Bio.Seq import Seq
from Bio.SeqUtils import molecular_weight, gc_fraction
from Bio.SeqUtils.ProtParam import ProteinAnalysis
from typing import Union, Dict, Tuple, List
import matplotlib.pyplot as plt
from dataclasses import dataclass
from enum import Enum

class SequenceType(Enum):
    DNA = "DNA"
    PROTEIN = "Protein"

@dataclass
class AnalysisResult:
    sequence_type: SequenceType
    sequence: str
    length: int
    gc_content: float = None
    molecular_weight: float = None
    isoelectric_point: float = None
    amino_acid_composition: Dict[str, float] = None
    transcription: str = None
    translation: str = None

class BioAgent:
    """
    A bioinformatics agent for DNA and protein sequence analysis.
    """
    
    def __init__(self):
        self.sequence = None
        self.sequence_type = None
    
    def analyze_sequence(self, sequence: str, seq_type: SequenceType) -> AnalysisResult:
        """
        Analyze a DNA or protein sequence.
        
        Args:
            sequence: The input sequence (DNA or protein)
            seq_type: Type of sequence (DNA or PROTEIN)
            
        Returns:
            AnalysisResult containing various sequence properties
        """
        self.sequence = sequence.upper()
        self.sequence_type = seq_type
        
        result = AnalysisResult(
            sequence_type=seq_type,
            sequence=self.sequence,
            length=len(self.sequence)
        )
        
        if seq_type == SequenceType.DNA:
            self._analyze_dna(result)
        elif seq_type == SequenceType.PROTEIN:
            self._analyze_protein(result)
            
        return result
    
    def _analyze_dna(self, result: AnalysisResult) -> None:
        """Perform DNA-specific analysis."""
        seq = Seq(self.sequence)
        
        # Basic DNA analysis
        result.gc_content = gc_fraction(seq) * 100
        
        # Transcription and translation
        result.transcription = str(seq.transcribe())
        result.translation = str(seq.translate())
        
        # Molecular weight (approximate)
        result.molecular_weight = molecular_weight(seq, 'DNA')
    
    def _analyze_protein(self, result: AnalysisResult) -> None:
        """Perform protein-specific analysis."""
        protein = ProteinAnalysis(self.sequence)
        
        # Basic protein analysis
        result.molecular_weight = protein.molecular_weight()
        result.isoelectric_point = protein.isoelectric_point()
        result.amino_acid_composition = protein.get_amino_acids_percent()
    
    def plot_amino_acid_composition(self, composition: Dict[str, float]) -> None:
        """Plot amino acid composition as a bar chart."""
        if not composition:
            raise ValueError("No amino acid composition data available")
            
        plt.figure(figsize=(12, 6))
        plt.bar(composition.keys(), composition.values())
        plt.title('Amino Acid Composition')
        plt.xlabel('Amino Acid')
        plt.ylabel('Percentage')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    def get_reverse_complement(self, dna_sequence: str) -> str:
        """Get the reverse complement of a DNA sequence."""
        return str(Seq(dna_sequence).reverse_complement())
    
    def calculate_gc_content(self, sequence: str) -> float:
        """Calculate GC content percentage of a DNA sequence."""
        return gc_fraction(sequence) * 100
