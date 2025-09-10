"""
Bioinformatics Agent - A powerful tool for DNA and protein sequence analysis.

This package provides a BioAgent class that can analyze DNA and protein sequences,
calculate various properties, and visualize the results.
"""

__version__ = "0.1.0"

from .core import BioAgent, SequenceType, AnalysisResult

__all__ = ['BioAgent', 'SequenceType', 'AnalysisResult']
