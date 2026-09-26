# DNA-SEQUENCE-ANALYZER
python interface for analyzing large datasets of DNA sequences.
 

## Project Overview
DNA Sequence Analyzer is a Python command-line project for basic DNA sequence analysis which can help in analyzing large datasets within seconds.Its main application is there in the healthcare industry. Its functions includes counting nucleotides, calculating GC content, finding complements, transcribing DNA to mRNA, translating mRNA to protein, and searching for DNA patterns.

## Features
- DNA validation
- Nucleotide counting
- calculation of GC content 
- Complementary strand
- Reverse complement
- DNA to mRNA transcription
- mRNA to protein translation
- DNA pattern search

## Technologies / Tools Used
- Python 3
- Command Prompt / Terminal
- Git
- GitHub

## Project Structure

DNA-Sequence-Analyzer/
├── README.md
├── statement.md
├── main.py
├── validation.py
├── analysis.py
├── genetics.py
├── pattern_search.py
├── menu.py
├── constants.py
├── test_dna.py
├── sample_output.txt
└── screenshots
```

## Installation
Clone the repository and enter the folder:
```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
cd DNA-Sequence-Analyzer
```
Check Python:
```bash
python --version
```
On Windows, if needed:
```bash
py --version
```

## How to Run
```bash
python main.py
```
On Windows, you can also use:
```bash
py main.py
```

Do not type only `main.py` as a Command Prompt command.

## How to Run
1. Run `main.py`.
2. Choose option 1.
3. Enter a DNA sequence such as `ATGCGTAC`.
4. Select an operation from the menu.
5. Read the result.
6. Choose option 9 to exit.

## Testing
Run:
```bash
python test_dna.py
```
Expected message:
```text
All basic tests passed.
```

## Screenshots
It includes the output interface like main menu, DNA input, nucleotide count, GC content, complement, mRNA, protein translation, and pattern search.

## Limitations
This is an introductory, basic level beginner friendly educational project. It does not currently include advanced genomic analysis, external biological databases, large FASTA-file processing, or a graphical interface.

## Future Enhancements
- FASTA file support
- DNA sequence comparison
- Mutation detection
- Amino acid frequency analysis
- Restriction site detection
- ORF detection
- Saving results to files
- Graphical user interface
- Biological database connection

## Conclusion
The project demonstrates how basic Python programming concepts can be applied to a simple bioinformatics problem through a command-line application.
