#Project Overview
    The project entails a simplified Tetris engine that models a 10-unit wide grid into which Tetris pieces fall under gravity. The pieces come to rest when they come into contact with the grid floor or an already-resting block. When an entire row is filled, it is cleared and pieces above it are dropped down to fill the gap. The grid starts in an empty start for each line of the input file.

#Dependencies
There are no dependencies.

#How to Run
The Tetris engine can be run by two ways:
    - One option is to run the below command line in your terminal after navigating to the folder containing tetris_engine.py
        python3 tetris_engine.py<input.txt>output.txt 
    - Another option is to run the shell script as indicated below in your terminal after navigating to the folder containing tetris_shell.sh
        ./tetris_shell.sh

Please ensure the python script keyclasses.py which contains important functions for the engine is in the same folder as tetris_engine.py. 

The input file consists of a string of commands structured line by line. Each individual command within a given line represents a Tetris piece placement. For example with "Q0" the first letter represents the type of piece to be generated and the integer 0 indicates where on the grid the piece will fall from.

The output file consists of a collection of integers which represent the heights of the resulting blocks after each line of the input has been run by the engine.

#Design Architecture
    I chose to structure the engine by classes to allow for more efficient control of the various operations such as piece generation, piece movement, line clearing, contact checking and height computation. I also separated the classes into two python files to enhance the clarity and organization of the engine code. The first file keyclasses.py primarily handles the generation of the custom pieces while tetris_engine.py handles the operations of the pieces on the engine grid.

#Assumptions
- The input meets expected guidelines and there is no need to validate the file format
- The grid width is fixed at 10 units 
- The stack height does not exceed 100 units for any test case

#Testing
    I built a unit test to test three key core operations of the engine which include the stack height computation, the custom piece generation, and row clearing. For these operations I tested multiple scenarios and edge cases to ensure the engine could perform its duties in variant circumstances.

There are two ways to run the unit test. 
    - One option is to run the below command line in your terminal after navigating to the folder containing enginecoretests.py
        python3 -m unittest -v enginecoretests.py 
    - Another option is to run the shell script as indicated below in your terminal after navigating to the folder containing unit_tests.sh
        ./unit_tests.sh
        
