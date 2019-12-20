options validvarname=upcase;
%let WORK_DIR = D:\AlfaPythonToMM\pywd;
%let PYTHON_PATH = C:\ProgramData\Anaconda3\python.exe;

/*options mprint mprintnest mlogic mlogicnest symbolgen spool;*/

libname worklib "&WORK_DIR\pydump";

%macro utl_submit_py64(pgm_path);
  filename rut pipe "&PYTHON_PATH "&pgm_path" ""&_MM_TrainResultFolder"" ""&WORK_DIR\pydump""";
  data _null_;
    file print;
    infile rut;
    input;
    put _infile_;
  run;
  filename rut clear;
%mend utl_submit_py64;

data worklib.train;
   set &_MM_InputDS;
run;
 
%utl_submit_py64("&WORK_DIR\train.py");
