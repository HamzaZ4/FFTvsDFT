# FFT vs DFT Comparison Project

This project aims to compare the Fast Fourier Transform (FFT) and the Discrete Fourier Transform (DFT) in terms of execution time and the resulting frequency domain representation of audio signals.

## Installation

To run this project, you need to have Python installed along with the following libraries:

- NumPy
- SciPy
- Matplotlib

You can install the required libraries using pip:

```bash
pip install numpy scipy matplotlib
```

## Usage

Place your audio file (e.g., tuba-55(0.2).wav) in the appropriate directories for both FFT and DFT scripts.

Run the FFT script to compute and visualize the FFT of the audio signal:
```bash
python fft_script.py
```
Run the DFT script to compute and visualize the DFT of the audio signal:
```bash
python dft_script.py
```

## Code Structure 
The project consists of two main folders: FFT and DFT, each containing a script for the respective Fourier transform method.

### FFT Implementation

The FFT implementation reads a .wav file and computes its FFT. The code can be seen in Fast/anEasyFFT.py

### DFT Implementation

The DFT implementation reads a .wav file and computes its DFT. The code can be seen in DFT/DFTdeFrappe.py



## Results
The results of the project will include:
- Execution time for both FFT and DFT.
- Plots showing the frequency domain representation of the audio signal for both FFT and DFT methods.
## Example Output
- FFT Execution Time: X seconds
- DFT Execution Time: Y seconds

Plots will be generated by the code also.

## Conclusion
This project demonstrates the efficiency of the FFT algorithm compared to the traditional DFT in terms of computation speed and ease of use. By analyzing the execution times and frequency domain plots, we can observe the significant advantages of using FFT for larger datasets.
