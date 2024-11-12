# Zahra_project
Nuclear Area Analysis using Python (Image Analysis and Statistical Analysis)
## Aim
The aim of this project is to assess the nuclear area stability between two groups of nucleus images: Nucleus24 and Nucleus38. The project includes steps such as image loading, preprocessing, segmentation, contour detection, area measurement, statistical analysis, and result visualization.
## Project Overview
This Python-based project analyzes and compares the nuclear areas between two groups of nuclei, Nucleus24 and Nucleus38. The analysis involves the following steps:
- Loading grayscale `.tif` images from folders.
- Preprocessing images with Gaussian Blur to reduce noise.
- Segmentation using Otsu's thresholding to separate the nuclei from the background.
- Contour detection to find the outlines of nuclei.
- Measurement of nucleus areas.
- Statistical comparison using a t-test.
- Visualization of the nucleus size distribution.
- Results and visualizations are saved to a PDF report.
### Dependencies
This project requires the following Python libraries:
- OpenCV`: For image processing and contour detection.
- NumPy`: For array operations and statistical calculations.
- Matplotlib`: For plotting histograms and visualizations.
- SciPy`: For statistical analysis.
- glob`: For reading image files from folders.
- ReportLab`: For generating PDF reports.

### File Structure
- images: Folder containing nucleus24 and nucleus38 images
- Code: Main Python script with image analysis and result generation
- Results.pdf: PDF file containing analysis results

## Usage
1. Clone the repository or download the files.
2. Install dependencies as mentioned above.
3. Run the script by specifying the folders containing your `.tif` images:
   ```bash   python main_script.py
4. The script will load images from the specified folders, perform the analysis, and generate a PDF file (`results.pdf`) with the results and visualizations.

## Methods
1. Image Loading
Images are loaded from user-specified folders using OpenCV. The images are read in grayscale format.
2. Image Preprocessing
Gaussian blur is applied to reduce image noise.
3. Image Segmentation
Otsu's thresholding is used to binarize the images, allowing clear separation between the nucleus and the background.
4. Contour Detection
Contours are detected using OpenCV's `findContours` method, which identifies the boundaries of the nuclei.
5. Area Measurement
The area of each detected contour (nucleus) is calculated using OpenCV's `contourArea` function.
6. Statistical Comparison
A t-test is performed to statistically compare the nucleus areas between the two groups, Nucleus24 and Nucleus38, using SciPy's `ttest_ind` function.
7. Results Visualization
Histograms are plotted to show the distribution of nuclear areas for each group. The results, including the t-test statistic and p-value, are saved to a PDF file.
## Results
T-statistic: Measures the statistical difference between the two groups of nucleus areas.
P-value: Indicates the significance of the results (whether the difference is statistically significant).
- A histogram of the nucleus size distribution is also included in the PDF report.
## License
This project is open-source and free to use.

