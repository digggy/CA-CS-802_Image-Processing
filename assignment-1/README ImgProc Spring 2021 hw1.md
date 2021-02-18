Image Processing (ImgProc) 
Image Processing Course Spring 2021
Homework 1 "MORPHOLOGICAL OPENING AND CLOSING"


HANDED OUT: 10-FEB-2021
DUE DATE / TIME: 20-FEB-2021, 23:59 h


SUBMISSION MODE:
Send your homework implementation and results, following the submission requirements as explained below, via e-mail to: 
h.hahn@jacobs-university.de

!PLEASE READ THIS INSTRUCTIONS FILE COMPLETELY BEFORE SUBMITTING THE HOMEWORK!

This homework is a 'team homework' meant to be done by two students together. If you want, you are allowed to do the homework alone. See additional regulations below.


TASKS:

* Write a (command line) program that performs either an erosion or a dilation of a two-dimensional gray-scale image 'f' with respect to a (symmetric, odd-sized) structuring element 'SE'. The program should accept four command line arguments: 
 - one switch to choose between erosion and dilation (alternatively, you can implement two programs, one for each operation):

   d = dilation 

   e = erosion 
- a first file name argument (SE).
  The structuring element SE shall follow the CSV (comma separated values, text file) format, cf. below, and must be a binary image with odd pixel size (e.g. 3x3, 3x1, 5x5, etc.)
 - a second file name argument (f).  The input file f shall follow the CSV format, cf. below.
 - a third file name argument (f_out).  The output file shall follow the CSV format, cf. below.

* Hint for gray-scale operations (as compared to the binary versions discussed during the first lecture): Move the SE to a respective position and compute at the anchor coordinate (where you moved the SE center) the minimum (maximum, respectively) of all pixel values under the shifted SE elements for gray-scale erosion (dilation, respectively).

* Generate (e.g. manually with a text editor) the required SE text files (SE1.txt, SE2.txt, etc.) for the 11+4 "EXPERIMENTS" listed below. Provide the chosen SE files with your hw submission.

* On output, provide a single CSV file for the eroded/dilated image in the same format and same definition and value domains as the input image 'f'. The output file names for the 12 experiments are defined below.
 
* Further hints: 
 - The center of the (odd sized) SE definition domain corresponds (by convention) to vertex (0,0).
 - Assume t_max (maximum gray value) outside of the definition domain of f in case of erosion for simple border handling
 - Assume 0 (minimum gray value) outside of the definition domain of f in case of dilation for simple border handling

* For the large image 'f3.txt', also a png-version is available for your convenience. Try to display the processing results of f3 also as a gray value graphics, in order to assess the plausibility of the result. Submit a screenshot or additional png (or other std graphics file format) file with the result.

* All SEs defined below are symmetric and contain the origin (0,0). Choose one asymmetric SE at your choice not containing the origin and demonstrate at the example of opening or closing that the chosen border handling then can introduce artifacts. Describe your actions and findings in the report file.

* Finally, do meaningful openings and closings on at least three photographs or 2D images of your choice (min. size: 64x64 pixels). 'Meaningful': Shall be motivated and useful from a real-world perspective. The three chosen problems shall be very different in nature. Write in the report (cf. below) a description of each of the three problems, purpose of the operations to be applied, choice of structuring elements, and provide the output as graphics file.


FILE FORMAT 'comma separated values (CSV)', for example (5x3 definition domain, with origin at the center):
1, 2, 3, 4, 5\n
5, 3, 0, 0, 0\n
1, 3, 5, 7, 5\n
\end-of-file


EXPERIMENTS: 11+4 pairs of input image f and SE to apply (output file names specified after '->') for erosions and dilations:

* erosion of f1 by square of size 3 (-> ef1_e1.txt)
* erosion of f2 by vertical line (|) of length 3 (-> ef2_e2.txt)
* erosion of f3 by horizontal line (-) of length 3 (-> ef3_e2.txt)
* erosion of f3 by square of size 5 (-> ef3_e3.txt)
* erosion of f3 by backward diagonal (\) of length 9 (-> ef3_e4.txt)
* erosion of f3 by forward diagonal (/) of length 9 (-> ef3_e5.txt)
* dilation of f3 by square of size 5 (-> df3_d3.txt)
* dilation of f3 by backward diagonal of length 9 (-> df3_d4.txt)
* dilation of f3 by forward diagonal of length 9 (-> df3_d5.txt)
* dilation of 'ef3_e3.txt' by square of size 5 (-> of3_o3.txt, which is then the opening of f3 by the square of size 5)
* dilation of 'ef3_e4.txt' by backward diagonal of length 9 (-> of3_o4.txt, which is then the opening of f3 by the backward diagonal of length 9)
* one self-chosen experiment with an asymmetric SE not containing the center (cf. above, add input/output file names to the respective report section)
* at least three self-chosen images and experiments (cf. above, add input/output file names to the respective report section)

Hints: 
 - the first experiment would be called from the command line as follows: "YourProgram e SE1.txt f1.txt ef1_e1.txt"
 - the combination of erosion using a SE followed by dilation using the same (but reflected) SE is called 'opening'. See what it does by comparing original and result, and try different combinations and sizes for your own interest. 


PROGRAMMING LANGUAGES ALLOWED:
C, C++, Python


SUBMISSION REQUIREMENTS / COMMENTS:

* Name your archive file as follows: "<Surname[s]>_IP_hw1.zip" which should have the following folder subfolders:
   1. "src"  - folder with your source code and Makefile etc.
   2. "input" - folder with initial input images plus your SE files and the additional self-chosen input files (cf. above)
   3. "output" - folder with all result files 
   4. "report" - add one file "<Surname[s]>_IP_hw1_report.txt" comprising descriptions and references/source URLs of the chosen experiments/problems from the internet, and, if applicable, references to any used material and help (cf. below). If done in a team of two, a statement of contribution must be included as well (which parts were done by which teammate?)

* Strictly adhere to the specified format for output files, in order to facilitate automated result comparison.
	
* Regarding the coding style, commented code with a clear structure and without unnecessary code doubling is preferred. (no influence on the grade)

* Please include a simple Makefile that will be capable to recompile your code, regenerate your results and place them in the output folder, by just typing make.

* Even though the homework is meant to be done by a team of two, students can work on it alone ('solo submission'), and mention this in the report file. 

* You are required to implement the full core part of the homework (algorithm, data structures) yourself (alone or in the team of two) without help from other people, without copying code from somewhere else, and without calling ready-made library functions that already do parts of the core task. 

* You are allowed to accept help on the non-algorithmic parts (loading and writing of files, parsing the command line input, writing a Makefile), but this help must be clearly referenced in the source code as well as in the report file, similar to any other information source used (for example open source libraries for data input or output). 

* There will be no extension of the deadline. Late submissions will receive zero score. The same (plus possibly more severe measures) applies for any kind of cheating.

* For teams of two, both team members will receive the same grade (except one team member did not contribute, then the score of that person will be zero)

* For solo submission, we will be somewhat more tolerant in our grading regarding missing items, such that a 100% score can already be reached with a slightly incomplete submission.


Feel free to ask any questions, through Piazza.
-Horst